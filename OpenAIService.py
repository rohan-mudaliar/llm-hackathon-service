from flask import Flask, request
import prompts,system_info
from Utils import process_response,initiatize_gpt

app = Flask(__name__)

@app.route('/score_title', methods=['POST'])
def score_title():
    chatgpt_headers, chatgpt_url = initiatize_gpt()
    input_title = request.get_json()["input"]
    title_system_info = system_info.get_product_title_scoring_system_info()
    title_prompt = prompts.get_product_title_scoring_prompt(input_title)
    response = process_response(chatgpt_headers, chatgpt_url,title_system_info,title_prompt)
    return response['choices'][0]['message']['content']


@app.route('/score_product_description', methods=['POST'])
def score_product_description():
    chatgpt_headers, chatgpt_url = initiatize_gpt()
    product_description = request.get_json()["input"]
    description_system_info = system_info.get_product_description_scoring_system_info()
    description_prompt = prompts.get_product_description_scoring_prompt(product_description)
    response = process_response(chatgpt_headers, chatgpt_url, description_system_info,description_prompt)
    return response['choices'][0]['message']['content']


@app.route('/translate_text', methods=['POST'])
def translate_text():
    chatgpt_headers, chatgpt_url = initiatize_gpt()
    original_text = request.get_json()["original_text"]
    target_language = request.get_json()["target_language"]
    description_system_info = system_info.get_translation_system_info()
    translation_prompt = prompts.get_translation_prompt(original_text)
    response = process_response(chatgpt_headers, chatgpt_url, description_system_info,translation_prompt)
    return response['choices'][0]['message']['content']


@app.route('/generate_title', methods=['POST'])
def generate_title():
    chatgpt_headers, chatgpt_url = initiatize_gpt()
    input_title = request.get_json()["input"]
    title_system_info = system_info.get_product_title_generation_system_info()
    title_prompt = prompts.get_product_title_generation_prompt(input_title)
    response = process_response(chatgpt_headers, chatgpt_url,title_system_info,title_prompt)
    return response['choices'][0]['message']['content']


@app.route('/generate_product_description', methods=['POST'])
def generate_product_description():
    chatgpt_headers, chatgpt_url = initiatize_gpt()
    product_description = request.get_json()["input"]
    description_system_info = system_info.get_product_description_generator_system_info()
    description_prompt = prompts.get_product_description_generation_prompt(product_description)
    response = process_response(chatgpt_headers, chatgpt_url, description_system_info,description_prompt)
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    app.run(debug=True)
