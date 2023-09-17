# config/loader.py

import json, os
print(os.getcwd())
def load_config(filename):
    with open(f'config/{filename}', 'r') as file:
        return json.load(file)

config_data = load_config('config.json')
api_keys_data = load_config('api_keys.json')
