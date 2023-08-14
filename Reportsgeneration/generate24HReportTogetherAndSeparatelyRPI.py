import pandas as pd
import matplotlib.pyplot as plt
import time
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
# Reading the CSV file
data = pd.read_csv(f'{current_directory}/sensordata.csv')

# Converting the 'created_at' and 'field1' columns to datetime format
data['created_at'] = pd.to_datetime(data['created_at'])
data['field1'] = pd.to_datetime(data['field1'])

# Setting 'field1' as the index
data.set_index('field1', inplace=True)

# Resampling data to get mean values for each minute for temperature, humidity, and CO2
hourly_temperature_means = data['field2'].resample('T').mean()
hourly_humidity_means = data['field3'].resample('T').mean()
hourly_co2_means = data['field4'].resample('T').mean()


def setLabelSize(size):
    for label in plt.legend().get_texts():
        label.set_fontsize(size)


def setTicksSize(size):
    plt.xticks(fontsize=size)
    plt.yticks(fontsize=size)


def saveCO2andTemperatureHumiditySeparately():
    # Plotting temperature and humidity
    plt.figure(figsize=(15, 8))

    # Temperature plot
    plt.plot(hourly_temperature_means.index, hourly_temperature_means,
             label='Temperature', marker='o', color='tomato')
    # Humidity plot
    plt.plot(hourly_humidity_means.index, hourly_humidity_means,
             label='Humidity', marker='o', color='royalblue')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('Temperature and Humidity Data', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(14)
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

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('CO2 Value', fontsize=20)
    plt.title('CO2 Trends', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(14)
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

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('CO2, Temperature, and Humidity Data Trends', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(14)
    plt.tight_layout()

    # Saving the plot as a photo
    plt.savefig(f'{folder_name}/24_hours_data_{getCurrentTime()}.png')
    # plt.show()
    plt.close()

# Fn to create a new folder for storing plots


def create_folder(base_folder_name):
    folder_name = f"{base_folder_name}_{getCurrentTime()}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
    return current_time


if __name__ == "__main__":
    folder_name = create_folder(
        f"{current_directory}/24hrsDataPlots")
    saveCO2andTemperatureHumiditySeparately()
    saveAllTogether()
