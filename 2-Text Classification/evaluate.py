import csv
import plotly.graph_objects as go

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

# Print the accuracies
print(f'ChatGPT Accuracy: {chatgpt_accuracy * 100}%')
print(f'GPT-4 Accuracy: {gpt4_accuracy * 100}%')

# Create a Plotly bar plot to compare the accuracies
fig = go.Figure(data=[
    go.Bar(name='ChatGPT', x=['ChatGPT'], y=[chatgpt_accuracy], marker_color='rgb(55, 83, 109)', width=[0.4]),
    go.Bar(name='GPT-4', x=['GPT-4'], y=[gpt4_accuracy], marker_color='rgb(26, 118, 255)', width=[0.4])
])

# Add text labels for accuracies on top of the bars
fig.update_layout(
    title_text='Performance of ChatGPT and GPT-4 on the Proton/Photon therapy classification dataset',
    annotations=[
        go.layout.Annotation(
            x='ChatGPT',
            y=chatgpt_accuracy + 0.01,  # Increase y-position to avoid overlap
            text=f'{chatgpt_accuracy:.2%}',
            showarrow=False,
            font=dict(
                size=14
            )
        ),
        go.layout.Annotation(
            x='GPT-4',
            y=gpt4_accuracy + 0.01,  # Increase y-position to avoid overlap
            text=f'{gpt4_accuracy:.2%}',
            showarrow=False,
            font=dict(
                size=14
            )
        )
    ]
)

fig.show()
