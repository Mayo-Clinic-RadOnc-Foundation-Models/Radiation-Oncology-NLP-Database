import csv
import re

# Open the text file and read its lines into a list
with open('Oncology Question.txt', 'r') as f:
    lines = f.readlines()

# Prepare an empty list to store the questions and answers
data = []

# Iterate over the lines of the file
for line in lines:
    # If the line starts with a number, it is a question
    if re.match(r"^\d", line):
        question = line.split(". ", 1)[1].strip()  # remove the leading number and dot
    # If the line starts with "a.", it is an answer
    elif line.startswith('a. '):
        answer = line[3:].strip()  # remove the leading "a. "
        data.append([question, answer])  # add the question-answer pair to the data

# Write the question-answer pairs to a CSV file
with open('Oncology-Question.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Question", "Answer"])  # write the header
    writer.writerows(data)  # write the data
