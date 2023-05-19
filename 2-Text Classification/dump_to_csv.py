import csv
import openai
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
        elif line.startswith('Label:'):
            label = line.split(': ', 1)[1]

        if description and label:
            data.append((description, label))
            description = None
            label = None

    return data

# Extract data from the text file
file_path = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2-Text Classification\Text_Classification.txt')
data = extract_data(file_path)

# Write data to a CSV file
with open('Text_Classification.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
