import csv
import matplotlib.pyplot as plt

# Read the correct labels from the CSV file
with open('Text_Classification.csv', 'r') as file:
    reader = csv.reader(file)
    correct_labels = [row[1].lower() for row in reader]

# Function to extract the prediction from a line in the text files
def extract_prediction(line):
    return line.split('. ', 1)[1].lower()

# Read the predictions from the chatgpt-response.txt file
with open('chatgpt-response.txt', 'r') as file:
    chatgpt_predictions = [extract_prediction(line.strip()) for line in file]

# Read the predictions from the gpt4-response.txt file
with open('gpt4-response.txt', 'r') as file:
    gpt4_predictions = [extract_prediction(line.strip()) for line in file]

# Calculate the accuracy of the ChatGPT model
chatgpt_correct_predictions = sum([correct_labels[i] == chatgpt_predictions[i] for i in range(len(correct_labels))])
chatgpt_accuracy = chatgpt_correct_predictions / len(correct_labels)

# Calculate the accuracy of the GPT-4 model
gpt4_correct_predictions = sum([correct_labels[i] == gpt4_predictions[i] for i in range(len(correct_labels))])
gpt4_accuracy = gpt4_correct_predictions / len(correct_labels)

# Accuracy results for Logic Reasoning task
accuracy_gpt4_logic_reasoning = 65.55555555555556 / 100  # convert to ratio
accuracy_chatgpt_logic_reasoning = 45.55555555555556 / 100  # convert to ratio

# Initialize a figure and an axes object
fig, ax = plt.subplots()

# Define the labels and the data
labels = ['Logic Reasoning', 'Text Classification']
chatgpt_data = [accuracy_chatgpt_logic_reasoning, chatgpt_accuracy]
gpt4_data = [accuracy_gpt4_logic_reasoning, gpt4_accuracy]

# Define the width of the bars and the positions
width = 0.35
chatgpt_positions = [i - width / 2 for i in range(len(labels))]
gpt4_positions = [i + width / 2 for i in range(len(labels))]

# Create the bars
ax.bar(chatgpt_positions, chatgpt_data, width, label='ChatGPT', color='steelblue')
ax.bar(gpt4_positions, gpt4_data, width, label='GPT-4', color='slategray')

# Add the labels and the legend
ax.set_ylabel('Accuracy')
ax.set_title('Performance of ChatGPT and GPT-4 on Different Tasks')
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels)
ax.legend()

# Add the text on top of the bars
for i in range(len(labels)):
    ax.text(chatgpt_positions[i], chatgpt_data[i] + 0.01, f'{chatgpt_data[i]:.2%}', ha='center', va='bottom')
    ax.text(gpt4_positions[i], gpt4_data[i] + 0.01, f'{gpt4_data[i]:.2%}', ha='center', va='bottom')

# Display the plot
plt.show()
