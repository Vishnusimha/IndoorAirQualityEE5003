import pandas as pd
import matplotlib.pyplot as plt
import time
import os
# Raspberry code to generate hourly reports 
# Reading the CSV file
current_directory = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(f'{current_directory}/feeds.csv')

# Converting the 'created_at' and 'field1' columns to datetime format
data['created_at'] = pd.to_datetime(data['created_at'])
data['field1'] = pd.to_datetime(data['field1'])

# Setting 'field1' as the index
temperature_data = data[['field1', 'field2']]
humidity_data = data[['field1', 'field3']]
co2_data = data[['field1', 'field4']]


def plotEachHourDataAndSavePlots():

    # Extracting each hour unique values from field1
    hours = data['field1'].dt.hour.unique()

    for hour in hours:
        # Filtering data for each current hour
        temperature_hourly_data = temperature_data[temperature_data['field1'].dt.hour == hour]
        humidity_hourly_data = humidity_data[humidity_data['field1'].dt.hour == hour]
        co2_hourly_data = co2_data[co2_data['field1'].dt.hour == hour]

        # Setting the 'field1' column as the index for each separated data
        temperature_hourly_data.set_index('field1', inplace=True)
        humidity_hourly_data.set_index('field1', inplace=True)
        co2_hourly_data.set_index('field1', inplace=True)

        # Resampling data to get mean values for each minute for temperature, humidity, and CO2
        hourly_temperature_means = temperature_hourly_data.resample('T').mean()
        hourly_humidity_means = humidity_hourly_data.resample('T').mean()
        hourly_co2_means = co2_hourly_data.resample('T').mean()

    #    # Resampling data to get mean values for each minute for temperature, humidity, and CO2
    #     hourly_temperature_means = temperature_hourly_data.resample('15T').mean()
    #     hourly_humidity_means = humidity_hourly_data.resample('15T').mean()
    #     hourly_co2_means = co2_hourly_data.resample('15T').mean()

        # Ploting and saving the graphs for temperature, humidity, and CO2
        plt.figure(figsize=(12, 6))

        # Temperature
        plt.subplot(3, 1, 1)
        plt.plot(hourly_temperature_means.index,
                 hourly_temperature_means['field2'], marker='o')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.title(f'Temperature for Hour {hour}')
        plt.grid(True)

        # Humidity
        plt.subplot(3, 1, 2)
        plt.plot(hourly_humidity_means.index,
                 hourly_humidity_means['field3'], marker='o', color='green')
        plt.xlabel('Time')
        plt.ylabel('Humidity')
        plt.title(f'Humidity for Hour {hour}')
        plt.grid(True)

        # CO2
        plt.subplot(3, 1, 3)
        plt.plot(hourly_co2_means.index,
                 hourly_co2_means['field4'], marker='o', color='red')
        plt.xlabel('Time')
        plt.ylabel('CO2')
        plt.title(f'CO2 for Hour {hour}')
        plt.grid(True)

        plt.tight_layout()
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
        # Saving the plots as photos
        plt.savefig(f'{folder_name}/{hour}_{current_time}_hour_data.png')
        plt.close()
        # plt.show()


def create_folder(base_folder_name):
    folder_name = f"{base_folder_name}_{getCurrentTime()}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
    return current_time


if __name__ == "_main_":
    folder_name = create_folder(
        f"{current_directory}/HourlyDataPlots")
    plotEachHourDataAndSavePlots()
