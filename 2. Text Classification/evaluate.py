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

def calculate_accuracy(predictions_file, correct_labels):
    with open(predictions_file, 'r') as file:
        predictions = file.readlines()

    correct_count = 0
    for i in range(len(predictions)):
        prediction = predictions[i].strip().split('. ')[1]
        correct_label = correct_labels[i][1]
        if prediction == correct_label:
            correct_count += 1

    accuracy = correct_count / len(predictions)
    return accuracy

# Extract correct labels from the text file
file_path = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2. Text Classification\Text_Classification.txt')
data = extract_data(file_path)
correct_labels = data[5:]

# Calculate accuracy for ChatGPT
chatgpt_predictions_file = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2. Text Classification\chatgpt-response.txt')
chatgpt_accuracy = calculate_accuracy(chatgpt_predictions_file, correct_labels)
print(f'ChatGPT Accuracy: {chatgpt_accuracy * 100}%')

# Calculate accuracy for GPT-4
gpt4_predictions_file = Path(r'C:\Users\zheng\Downloads\Radiation-Oncology-NLP-Database\2. Text Classification\gpt4-response.txt')
gpt4_accuracy = calculate_accuracy(gpt4_predictions_file, correct_labels)
print(f'GPT-4 Accuracy: {gpt4_accuracy * 100}%')
