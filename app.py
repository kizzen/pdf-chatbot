from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

from flask import Flask, render_template, request, jsonify
import os
from config.loader import config_data, api_keys_data

app = Flask(__name__)

# set config variables
app.config['API_KEY'] = api_keys_data["API_GPT4_KEY"]
app.config['UPLOAD_DIR'] = config_data["UPLOAD_DIR"]
app.config['ALLOWED_EXT'] = config_data["ALLOWED_EXT"]
app.config['DOC_SET'] = config_data["DOC_SET"]
app.config['LOCAL_DIRECTORY'] = config_data["LOCAL_DIR"]

def setup_bot(filename = 'data/BitcoinGroup_GB2022_EN.pdf'):
    # load pdf
    pdf_loader = PyPDFLoader(filename)
    pdf_data = pdf_loader.load()

    # split data
    text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
    split_data = text_splitter.split_documents(pdf_data)

    # load var
    openai_key = api_keys_data["API_GPT4_KEY"]
    collection_name = app.config['DOC_SET']
    local_directory = config_data["LOCAL_DIR"]
    persist_directory = os.path.join(os.getcwd(), local_directory)

    # create embeddings and vector db
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    vector_db = Chroma.from_documents(split_data,
                                    embeddings,
                                    collection_name=collection_name,
                                    persist_directory=persist_directory
                                    )
    vector_db.persist()

    # Q&A 
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_bot = ConversationalRetrievalChain.from_llm(
                OpenAI(openai_api_key=openai_key,
                    temperature=0, model_name="gpt-3.5-turbo"), 
                vector_db.as_retriever(), 
                memory=memory)
    
    return qa_bot

# Setting up with the default PDF initially
qa_bot = setup_bot()
chat_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    global qa_bot, chat_history

    file_format = app.config['ALLOWED_EXT']
    if file_format not in request.files:
        return 'No file part'
    file = request.files[file_format]
    if file.filename == '':
        return 'No selected file'
    
    def allowed_file(filename, allowed_ext):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext
    
    if file and allowed_file(file.filename, {'pdf'}):
        filename = os.path.join(app.config['UPLOAD_DIR'], file.filename)
        file.save(filename)
        
        # Now you can load this file instead of the hardcoded one in your setup
        qa_bot = setup_bot(filename)
        chat_history = []  # reset chat history if a new document is uploaded

        return 'PDF uploaded and processed!'
    else:
        return 'Invalid file type. Only PDFs are allowed.'

@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.json['message']

    # Using your chatbot logic to generate a response
    global chat_history
    response = qa_bot({"question": message, "chat_history": chat_history})
    chat_history.append({"user": message, "bot": response["answer"]})

    return jsonify({"answer": response["answer"]})

if __name__ == '__main__':
    # Create the upload directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_DIR']):
        os.makedirs(app.config['UPLOAD_DIR'])
    app.run(host='0.0.0.0', port=8080, debug=True)
