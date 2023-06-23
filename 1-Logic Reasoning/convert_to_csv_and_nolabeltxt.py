import csv

def extract_questions_answers(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    questions_answers = []
    question = None
    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '':
            continue  # Ignore blank lines
        elif stripped_line.lower() in ['yes', 'no']:
            if question is not None:
                questions_answers.append([question, stripped_line.lower()])
                question = None  # Reset the question after storing a pair
            else:
                print(f"Error: Found answer with no preceding question: {stripped_line}")
        elif stripped_line[0].isdigit():  # Assume lines starting with a number are questions
            question = stripped_line
        else:
            print(f"Error: Unexpected line format: {stripped_line}")

    return questions_answers

def write_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])
        writer.writerows(data)

def write_txt(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for question, _ in data:
            file.write(question + '\n')
            file.write('______' + '\n')

filename = 'Logic_Reasoning.txt'
data = extract_questions_answers(filename)
write_csv('Logic_Reasoning.csv', data)
write_txt('Logic_Reasoning_No_Labels.txt', data)
