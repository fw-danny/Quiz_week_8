import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('climate.csv')

# Extract the relevant columns from the Data (e.g., year and temperature)
year_column = 'Year'
temperature_column = 'Temperature'

# Convert the date column to datetime format (if it's not already)
data[year_column] = pd.to_datetime(data[year_column])

# Create a figure and plot the data
plt.figure(figsize=(10, 6))
plt.plot(data[year_column], data[temperature_column], label='Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.grid(True)

# Show the figure
plt.tight_layout()
plt.show()
