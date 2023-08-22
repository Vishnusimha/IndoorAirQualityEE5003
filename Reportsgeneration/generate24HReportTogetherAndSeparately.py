import pandas as pd
import matplotlib.pyplot as plt
import time
import os

# Code to get Full data report, with all (temperature, humidity, and CO2) together and separately without ventilation markings.
# Use this code while running in Raspberry Reportsgeneration/generate24HReportTogetherAndSeparatelyRPI.py

# Reading the CSV file
data = pd.read_csv('IndoorAirQualityEE5003/Reportsgeneration/feeds.csv')

# Converting the 'created_at' and 'field1' columns to datetime format
data['created_at'] = pd.to_datetime(data['created_at'])
data['field1'] = pd.to_datetime(data['field1'])

# Setting 'field1' as the index
data.set_index('field1', inplace=True)

# Resampling data to get mean values for each minute for temperature, humidity, and CO2
# We can also sample the data for 2 minutes and more like below.
# It helps when we have huge data, so we can plot by sampling the values
hourly_temperature_means = data['field2'].resample('T').mean()
hourly_humidity_means = data['field3'].resample('T').mean()
hourly_co2_means = data['field4'].resample('T').mean()


def saveCO2andTemperatureHumiditySeparately():
    # Plotting temperature and humidity
    plt.figure(figsize=(15, 8))

    # Temperature plot
    plt.plot(hourly_temperature_means.index, hourly_temperature_means,
             label='Temperature', marker='o', color='tomato')
    # Humidity plot
    plt.plot(hourly_humidity_means.index, hourly_humidity_means,
             label='Humidity', marker='o', color='royalblue')

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Temperature and Humidity Data')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Saving the plot as a photo
    plt.savefig(
        f'{folder_name}/temperature_humidity_data_{getCurrentTime()}.png')
    plt.close()

    # Plotting CO2 graph
    plt.figure(figsize=(15, 8))

    # CO2 plot
    plt.plot(hourly_co2_means.index, hourly_co2_means,
             label='CO2', marker='o', color='orangered')

    plt.xlabel('Time')
    plt.ylabel('CO2')
    plt.title('CO2 Data')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

  # Saving the plot as a photo
    plt.savefig(f'{folder_name}/co2_data_{getCurrentTime()}.png')
    plt.close()


def saveAllTogether():
    # Plotting all the data together in a single graph for 24 hours
    plt.figure(figsize=(15, 8))

    # Temperature plot
    plt.plot(hourly_temperature_means.index, hourly_temperature_means,
             label='Temperature', marker='o', color='tomato')
    # Humidity plot
    plt.plot(hourly_humidity_means.index, hourly_humidity_means,
             label='Humidity', marker='o', color='royalblue')
    # CO2 plot
    plt.plot(hourly_co2_means.index, hourly_co2_means,
             label='CO2', marker='o', color='red')

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('24 Hours Data')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Saving the plot as a photo
    plt.savefig(f'{folder_name}/24_hours_data_{getCurrentTime()}.png')
    # plt.show()
    plt.close()


def create_folder(base_folder_name):
    # To create a folder with time stamp for each time the code executes
    folder_name = f"{base_folder_name}_{getCurrentTime()}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def getCurrentTime():
    # To get current time in a particular format
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
    return current_time


if __name__ == "__main__":
    # Creating the folder at first and saving all files into it
    folder_name = create_folder(
        f"IndoorAirQualityEE5003/Reportsgeneration/24hrsDataPlots")
    saveCO2andTemperatureHumiditySeparately()
    saveAllTogether()
