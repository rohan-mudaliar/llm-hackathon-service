import json

def get_product_title_scoring_prompt(title):
    prompt_prefix = f"""
    --------------------------
    Score the given {title}. Give me output in below format:

    Section_Title((Overall,Clarity_and_Relevance,Keyword_Usage,Conciseness, Unique_Selling_Point or Engagement_and_Appeal)), Score, Reason

    Give the score and how much it is out of for each section.Eg. Score - 16/25

    Strictly output in JSON format. The JSON should have the following format:"""

    # typescript interface
    sample_interface = """interface Response {
         data: Array<{ Section_Title: string, Score: string, Reason: string }>;
    }"""

    prompt = prompt_prefix + json.dumps(sample_interface)
    return prompt



def get_product_description_scoring_prompt(product_description):
    prompt_prefix = f"""
    --------------------------
    Score the given {product_description}. Give me output in below format:

    Section_Title(Overall, Components_Section,Rules_Section,Structure_Section), Score, Reason

    Give the score and how much it is out of for each section.Eg. Score - 4.5/10

    Strictly output in JSON format. The JSON should have the following format:"""

    # typescript interface
    sample_interface = """interface Response {
         data: Array<{ Section_Title: string, Score: string, Reason: string }>;
    }"""

    prompt = prompt_prefix + json.dumps(sample_interface)
    return prompt


def get_translation_prompt(original_text):
    prompt_prefix = f"""
    --------------------------
    Translate given {original_text} to English or Japanese depending on the input language. 
    If input language is english translate to japanese and if input language is japanese, then
    translate to english.
    Strictly output in JSON format. The JSON should have the following format:"""

    # typescript interface
    sample_interface = """{
         Original_text: string, Translated_text: string ;
    }"""

    prompt = prompt_prefix + json.dumps(sample_interface)
    return prompt


def get_product_title_generation_prompt(title):
    prompt_prefix = f"""
    --------------------------
    Consider the given {title}. Using the logic to calculate score,
    generate a new product title that has a high score. Give me output in below format:

    Product_Title(Product_Title_Old or Product_Title_New), Score, Reason

    Give me output for both old and new titles. 

    Strictly output in JSON format. The JSON should have the following format:"""

    # typescript interface
    sample_interface = """interface Response {
         data: Array<{ Product_Title: string, Score: string, Reason: string }>;
    }"""

    prompt = prompt_prefix + json.dumps(sample_interface)

    return prompt


def get_product_description_generation_prompt(product_description):
    prompt_prefix = f"""
    --------------------------
    Consider the given {product_description}. Using the logic to calculate score,
    generate a new product descirption that has a high score. Give me output in below format:

    Product_Description(Product_Description_Old or Product_Description_New), Score, Reason

    Strictly output in JSON format. The JSON should have the following format:"""

    # typescript interface
    sample_interface = """interface Response {
         data: Array<{ Product_Description: string, Score: string, Reason: string }>;
    }"""

    prompt = prompt_prefix + json.dumps(sample_interface)
    return prompt