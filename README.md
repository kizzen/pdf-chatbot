# PDF Chatbot

A simple chatbot GUI that can answer questions about the content of uploaded PDF documents. To see the app in action, click on the image below.

[![Watch the video](https://img.youtube.com/vi/EGfnQUHEpYs/maxresdefault.jpg)](https://www.youtube.com/watch?v=EGfnQUHEpYs)

For further reading, check out this blog post: [How to Create a PDF Chatbot with Langchain and Flask](https://medium.com/@ezzine.khalil/how-to-create-a-pdf-chatbot-with-langchain-and-flask-818646a04ba8). 

## Features

- **Upload PDFs**: Easily upload a PDF and ask the chatbot questions about the content.
- **Search Functionality**: Extracts and indexes the content of PDFs to provide quick and accurate answers.
- **Interactive UI**: A user-friendly interface that facilitates seamless interaction.

## Getting Started

### Prerequisites

Before you start, you must have:

- python
- pip 
- OpenAI API key

### Installation

1. Clone the repository:
    - `git clone https://github.com/kizzen/pdf-chatbot.git`
2. Navigate to the project directory:
    - `cd pdf-chatbot`
3. Create and activate a new virtual environment. Example using conda:
    - `conda create -n chat_pdf_env`
    - `conda activate chat_pdf_env`
4. Install the necessary packages from requirements.txt into the newly create environment:
    - `pip install -r requirements.txt`
5. Launch the Flask app from the Terminal:
    - `python app.py`

### Usage
1. Open a web browser and navigate to http://localhost:8080/.
2. Upload a PDF file using the 'Upload' button.
3. Start asking questions related to the uploaded PDF in the chat interface.

### Contributing
All contributions are welcome! 

## License

[MIT License](https://github.com/kizzen/pdf-chatbot/blob/main/LICENSE)

## Acknowledgments

Inspired by https://abvijaykumar.medium.com/prompt-engineering-retrieval-augmented-generation-rag-cd63cdc6b00.

## Contact
For any queries or feedback, reach out to me at ezzine.khalil@gmail.com or via my [LinkedIn Profile](https://www.linkedin.com/in/kezzine)
. 

