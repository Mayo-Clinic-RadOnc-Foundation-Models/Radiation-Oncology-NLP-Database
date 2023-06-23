import plotly.express as px
import pandas as pd

# Prepare data
data = {
    'Model': ['Radiology-GPT', 'ChatGPT', 'StableLM', 'Dolly', 'LLAMA', 'Alpaca'],
    'Understandability': [48.5, 47.5, 30, 33, 14.5, 44.5],
    'Coherence': [49, 47.5, 26.5, 33.5, 15.5, 41.5],
    'Relevance': [43, 49.5, 27, 33, 14.5, 37],
    'Conciseness': [48.5, 39.5, 24.5, 29, 15.5, 40],
    'Clinical Utility': [42.5, 40.5, 22, 28.5, 14.5, 37],
}
df = pd.DataFrame(data)

# Melt the DataFrame to the format required by Plotly
df_melt = df.melt(id_vars="Model", var_name="Metric", value_name="Score")

# Specify custom colors
colors = ['#804BF2', '#57C6F2', '#F2B84B', '#F28585', '#FFE569', '#46C2CB']

# Create the plot
fig = px.bar(df_melt,
             x="Metric",
             y="Score",
             color="Model",
             color_discrete_map=dict(zip(df["Model"], colors)),
             barmode="group")

# Add titles
fig.update_layout(title="Averaged Expert Evaluation Scores",
                  yaxis_title="Scores",
                  yaxis=dict(range=[0, 80]))  # Manually set y-axis range

# Show the plot
fig.show()
