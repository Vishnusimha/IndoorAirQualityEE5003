import pandas as pd
import matplotlib.pyplot as plt
import time
import os

# Raspberry code to get Full data report, with all (temperature, humidity, and CO2) together and separately with ventilation markings.

# Getting the current directory
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
# We can also sample the data for 2 minutes and more like below.
# It helps when we have huge data, so we can plot by sampling the values

# hourly_temperature_means = data['field2'].resample('T').mean()
# hourly_humidity_means = data['field3'].resample('T').mean()
# hourly_co2_means = data['field4'].resample('T').mean()

# hourly_temperature_means = data['field2'].resample('2T').mean()
# hourly_humidity_means = data['field3'].resample('2T').mean()
# hourly_co2_means = data['field4'].resample('2T').mean()

# hourly_temperature_means = data['field2'].resample('3T').mean()
# hourly_humidity_means = data['field3'].resample('3T').mean()
# hourly_co2_means = data['field4'].resample('3T').mean()

hourly_temperature_means = data['field2']
hourly_humidity_means = data['field3']
hourly_co2_means = data['field4']


def setLabelSize(size):
    # to set the label size in graph
    for label in plt.legend().get_texts():
        label.set_fontsize(size)


def setTicksSize(size):
    # to set the Ticks size on each axes in graph
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
    addVentilationMarkers(plt, data)
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
    addVentilationMarkers(plt, data)

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('CO2 Values', fontsize=20)
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

    addVentilationMarkers(plt, data)

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title(
        'CO2, Temperature, and Humidity Data Trends with Ventilation Marks', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(16)
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


def addVentilationMarkers(axes, data):
    # To add ventilation marking based on field7 values on x axis
    ventilation_required = data['field7']
    ventilation_times = data.index[ventilation_required]
    axes.scatter(ventilation_times, [0] * len(ventilation_times),
                 marker='o', color='green', label='Ventilation Required', zorder=5)


def count_true_values_in_csv():
    # To get the Number of times ventilation was required, with out counting continous true values in data
    true_count = 0
    current_streak = 0

    for value in data['field7']:
        if value:
            current_streak += 1
        else:
            if current_streak > 0:
                true_count += 1
                current_streak = 0

    if current_streak > 0:
        true_count += 1

    return true_count


if __name__ == "__main__":
    # Creating the folder at first and saving all files into it
    folder_name = create_folder(
        f"{current_directory}/24hrsDataPlots")
    saveCO2andTemperatureHumiditySeparately()
    saveAllTogether()
    print(
        f"Number of times ventilation was required: {count_true_values_in_csv()}")
