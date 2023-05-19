import openai
from pathlib import Path
import re

# Set your OpenAI API key
openai.api_key = ""

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
        elif line.startswith('Label:'):
            label = line.split(': ', 1)[1]

        if description and label:
            data.append((description, label))
            description = None
            label = None

    return data

def chatgpt_completion(model_new, prompt_new, max_tokens_new=100):
    completion = openai.ChatCompletion.create(
        model=model_new,
        messages=[
            {"role": "user", "content": prompt_new}
        ],
        max_tokens=max_tokens_new,
    )
    return completion.choices[0].message.content

# Extract data from the text file
file_path = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2-Text Classification\Text_Classification.txt')
data = extract_data(file_path)

print(data)

# Build the prompt
prompt = "Learn the format from these first 5 description-label pair examples from radiation oncology:\n"
for i in range(5):
    prompt += f"{data[i][0]}\nLabel: {data[i][1]}\n"
prompt += "\nPredict the labels (the label can only be either 'Proton therapy' or 'Photon therapy'), write the labels one per line, for the following 95 descriptions you see:\n"
for i in range(5, len(data)):
    prompt += f"{data[i][0]}\n"

# Send the prompt to the GPT-3.5-turbo model
response_turbo = chatgpt_completion("gpt-3.5-turbo", prompt, max_tokens_new=1000)

# Write the response to a new text file
with open('response_turbo.txt', 'w') as file:
    file.write(response_turbo)

# Send the prompt to the GPT-4 model
response_4 = chatgpt_completion("gpt-4", prompt, max_tokens_new=1000)

# Write the response to a new text file
with open('response_4.txt', 'w') as file:
    file.write(response_4)
