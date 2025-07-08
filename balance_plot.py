import pandas as pd
import matplotlib.pyplot as plt
import os

# Define input and output paths
input_csv = "data/my_data.csv"
output_img = "output/balance_plot.png"

# Load CSV
df = pd.read_csv(input_csv)

# Parse date and balance
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")
df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
df = df.sort_values('Date')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Balance'], marker='o', linestyle='-')
plt.title('Balance Over Time')
plt.xlabel('Date')
plt.ylabel('Balance ($)')
plt.grid(True)
plt.tight_layout()

# Save to output folder (also mounted)
plt.savefig(output_img)

print(f"Saved plot to {output_img}")
