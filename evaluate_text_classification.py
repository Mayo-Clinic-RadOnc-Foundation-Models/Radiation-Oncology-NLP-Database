# import os
# import openai
# import time
# from bs4 import BeautifulSoup
# import pprint
# import tiktoken
#
# openai.api_key = ""
#
# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#     """Returns the number of tokens in a text string."""
#     encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens
#
# def chatgpt_completion(model_new="gpt-3.5-turbo",prompt_new="hi", temperature_new=0.05, top_p_new=1, n_new=1, max_tokens_new=100):
#     Chat_Completion = openai.ChatCompletion.create(
#         model=model_new,
#         messages=[
#             {"role": "user", "content": prompt_new}
#         ],
#         temperature=temperature_new,
#         top_p=top_p_new,
#         n=n_new,
#         # stop=5,
#         max_tokens=max_tokens_new,
#         presence_penalty=0,
#         frequency_penalty=0
#     )
#     return Chat_Completion
#
#     completion = chatgpt_completion(prompt_new=prompt,max_tokens_new=4050-num_tokens)
#     rewrite_finding = completion.choices[0].message.content
#
#     rewrite_file = "/Users/ericliu/Desktop/chatgpt_anonymization/rewrite_no_ditch_long_inputs/" + list_of_files[i] + "_anonymized.txt"
#
#     with open(rewrite_file, "w") as f:
#         f.write(rewrite_finding)
#
#     print("-----------第" + str(i + 1) + "个\n-----------")
#     print("-----------My prompt " + "\n-----------")
#     print(prompt)
#     print("-----------Anonymized " + "\n-----------")
#     print(rewrite_finding)

from pathlib import Path
import re

def extract_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    description = None
    label = None
    for line in lines:
        line = line.strip()
        if re.match(r'\d+,', line):
            description = line.split(', ', 1)[1]
            print(description)
        elif line.startswith('Label:'):
            label = line.split(': ', 1)[1]

        if description and label:
            data.append((description, label))
            description = None
            label = None

    return data

# Usage
file_path = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2. Text Classification\Text_Classification.txt')
data = extract_data(file_path)

# Verify that there are 100 pairs
if len(data) == 100:
    print("There are 100 pairs of descriptions and labels.")
else:
    print(f"There are {len(data)} pairs of descriptions and labels.")

# for description, label in data:
#     print(f'Description: {description}\nLabel: {label}\n')







