import requests


def process_response(chatgpt_headers, chatgpt_url,curr_system_info,prompt):
    messages = [
        {"role": "system", "content": curr_system_info},
        {"role": "user", "content": prompt}
    ]
    chatgpt_payload = {
        "model": "gpt-3.5-turbo-16k",
        "messages": messages,
        "temperature": 0.6
    }
    response = requests.request("POST", chatgpt_url, json=chatgpt_payload, headers=chatgpt_headers)
    response = response.json()
    return response


def initiatize_gpt():
    openaikey = "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"  # Replace with your actual OpenAI API key
    chatgpt_url = "https://api.openai.com/v1/chat/completions"
    chatgpt_headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {openaikey}"
    }
    return chatgpt_headers, chatgpt_url
