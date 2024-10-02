import csv
import pandas as pd

# Method 1: Using the csv module to read temperature data
def read_temperature_with_csv(file_path):
    with open(file_path, mode="r") as data_file:
        data = csv.reader(data_file)
        header = next(data)
        temperature_index = header.index("temp")
        
        temperatures = [int(row[temperature_index]) for row in data]
    
    return temperatures

# temperatures = read_temperature_with_csv("weather_data.csv")
# print(temperatures)

# Method 2: Using pandas to manipulate weather data
def analyze_weather_with_pandas(file_path):
    data = pd.read_csv(file_path)
    temperature_list = data["temp"].tolist()
    
    print("Temperature list:", temperature_list)
    print("Number of temperature readings:", len(temperature_list))
    
    # Calculate the average temperature
    average_temp = sum(temperature_list) / len(temperature_list)
    print("Average temperature:", average_temp)
    
    # Find and print the row with the highest temperature
    max_temp_row = data[data.temp == data["temp"].max()]
    print("Row with max temperature:\n", max_temp_row)
    
    monday = data[data.day == "Monday"]
    print("Monday's data:\n", monday)
    
    # Convert Monday's temperature to Fahrenheit
    monday_temp_fahrenheit = (monday.temp * (9/5) + 32).values[0]
    print("Monday's temperature in Fahrenheit:", monday_temp_fahrenheit)

# Run the pandas analysis function
analyze_weather_with_pandas("weather_data.csv")
