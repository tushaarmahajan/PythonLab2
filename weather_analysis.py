# Sample weather data from 1st August 2023 to 10th July 2024
weather_data = [
    {"date": "2023-08-01", "max_temp": 31, "min_temp": 22, "humidity": 70},
    {"date": "2023-08-02", "max_temp": 33, "min_temp": 24, "humidity": 65},
    {"date": "2023-08-03", "max_temp": 34, "min_temp": 23, "humidity": 60},
    {"date": "2023-08-04", "max_temp": 35, "min_temp": 25, "humidity": 68},
    {"date": "2023-08-05", "max_temp": 30, "min_temp": 21, "humidity": 75},
    {"date": "2023-08-06", "max_temp": 28, "min_temp": 20, "humidity": 72},
    {"date": "2023-08-07", "max_temp": 27, "min_temp": 19, "humidity": 70},
    {"date": "2023-08-08", "max_temp": 32, "min_temp": 22, "humidity": 67},
    {"date": "2023-08-09", "max_temp": 33, "min_temp": 23, "humidity": 66},
    {"date": "2023-08-10", "max_temp": 34, "min_temp": 24, "humidity": 64},
    
]

def find_highest_and_lowest_temps(weather_data):
    """Find the highest and lowest temperatures recorded during the period."""
    max_temp = max(day["max_temp"] for day in weather_data)
    min_temp = min(day["min_temp"] for day in weather_data)
    return max_temp, min_temp

def count_days_above_30(weather_data):
    """Determine the number of days with temperatures above 30°C."""
    return sum(1 for day in weather_data if day["max_temp"] > 30)

def average_humidity(weather_data):
    """Compute the average humidity over the specified period."""
    total_humidity = sum(day["humidity"] for day in weather_data)
    return total_humidity / len(weather_data)

def main():
    highest_temp, lowest_temp = find_highest_and_lowest_temps(weather_data)
    days_above_30 = count_days_above_30(weather_data)
    avg_humidity = average_humidity(weather_data)

    print(f"Highest Temperature: {highest_temp}°C")
    print(f"Lowest Temperature: {lowest_temp}°C")
    print(f"Number of Days Above 30°C: {days_above_30}")
    print(f"Average Humidity: {avg_humidity:.2f}%")

if __name__ == "__main__":
    main()
