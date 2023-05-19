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
file_path = Path(r'/2-Text Classification/Text_Classification.txt')
data = extract_data(file_path)

# Write the numeric order and description to a new text file, leaving the label empty
with open('Text_Classification_No_Labels.txt', 'w') as file:
    for i in range(len(data)):
        file.write(f"{i+1}, {data[i][0]}\nLabel: _______\n")
