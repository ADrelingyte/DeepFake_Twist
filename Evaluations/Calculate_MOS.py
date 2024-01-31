import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
csv_file_path = r'C:\Users\49157\Documents\Plan master\Erasmus\Lorraine Uni\Third semester\Software project\Literature\Subjective evaluation\naive data.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path, delimiter=';')
#print(df.columns) 
#Selected columns
selected_columns = ['Human', 'HifiGan', 'MultiMelgan', 'WaveGrad']
# Calculate the arithmetic mean for each column
mean_values = df[selected_columns].mean()

# Visualize the mean values in a bar chart
c = ['purple', 'pink', 'red', 'pink']
plt.bar(selected_columns, mean_values, color = c)
plt.xlabel('Vocoder clips')
plt.ylabel('MOS')
plt.title('Mean Opinion Score of Vocoders')
plt.show()
