import pandas as pd

# read csv file
df = pd.read_csv('Logic_Reasoning.csv')

# read gpt4-response.txt file and split by space, then take the last item (the response)
with open('gpt4-response.txt', 'r') as f:
    gpt4_responses = [line.strip().split(' ')[-1] for line in f]

# read chatgpt-response.txt file and split by space, then take the last item (the response)
with open('chatgpt-response.txt', 'r') as f:
    chatgpt_responses = [line.strip().split(' ')[-1] for line in f]

correct_responses_gpt4 = 0
correct_responses_chatgpt = 0
# incorrect_predictions = []

for idx, row in df.iterrows():
    # Assuming the 'Answer' column contains the correct answers
    if row['Answer'].lower() == gpt4_responses[idx].lower():
        correct_responses_gpt4 += 1
    if row['Answer'].lower() == chatgpt_responses[idx].lower():
        correct_responses_chatgpt += 1
    # else:
    #     incorrect_predictions.append((row['Question'], gp4_responses[idx], row['Answer']))

accuracy_gpt4 = correct_responses_gpt4 / len(df)
accuracy_chatgpt = correct_responses_chatgpt / len(df)
print(f'Accuracy of GPT-4: {accuracy_gpt4 * 100}%')
print(f'Accuracy of ChatGPT: {accuracy_chatgpt * 100}%')
# print(f'\nIncorrect predictions:\n')
# for question, predicted, correct in incorrect_predictions:
#     print(f"Question: {question}\nPredicted: {predicted}\nCorrect: {correct}\n")
