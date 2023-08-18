import matplotlib.pyplot as plt
import os
import pandas as pd
import time

# Reading the CSV file
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
# Reading the CSV file

data = pd.read_csv(

data['field1'] = pd.to_datetime(data['field1'], format='%Y-%m-%dT%H:%M:%S%z')
data.set_index('field1', inplace=True)

# Resampling data to get mean values for each minute for temperature, humidity, and CO2
temperature_means = data['field2'].resample('T').mean()
humidity_means = data['field3'].resample('T').mean()
co2_means = data['field4'].resample('T').mean()
temperature_dht_means = data['field5'].resample('T').mean()
humidity_dht_means = data['field6'].resample('T').mean()

# temperature_means = data['field2'].resample('2T').mean()
# humidity_means = data['field3'].resample('2T').mean()
# co2_means = data['field4'].resample('2T').mean()
# temperature_dht_means = data['field5'].resample('2T').mean()
# humidity_dht_means = data['field6'].resample('2T').mean()


def setLabelSize(size):
    for label in plt.legend().get_texts():
        label.set_fontsize(size)


def setTicksSize(size):
    plt.xticks(fontsize=size)
    plt.yticks(fontsize=size)


def create_folder(base_folder_name):
    folder_name = f"{base_folder_name}_{getCurrentTime()}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def getCurrentTime():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
    return current_time


def saveSCD40AndDHTTogether():
    # Plotting temperature and humidity
    plt.figure(figsize=(15, 8))

    # Temperature plot
    plt.plot(temperature_means.index, temperature_means,
             label='Temperature - SCD40', marker='o', color='red')
    # Temperature DHT11 plot
    plt.plot(temperature_dht_means.index, temperature_dht_means,
             label='Temperature - DHT11', marker='o', color='tomato')

    # humidity plot
    plt.plot(humidity_means.index, humidity_means,
             label='Humidity - SCD40', marker='o', color='royalblue')
    # humidity DHT11 plot
    plt.plot(humidity_dht_means.index, humidity_dht_means,
             label='Humidity - DHT11', marker='o', color='lightblue')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('SCD40 and DHT11 Data', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    plt.tight_layout()
    # plt.show()

    # Saving the plot as a photo
    plt.savefig(
        f'{folder_name}/SCD40AndDHT11Data{getCurrentTime()}.png')
    plt.close()


def saveTempAndDHTTempTogether():
    # Plotting temperature and humidity
    plt.figure(figsize=(15, 8))

    # Temperature plot
    plt.plot(temperature_means.index, temperature_means,
             label='Temperature - SCD40', marker='o', color='red')
    # Temperature DHT11 plot
    plt.plot(temperature_dht_means.index, temperature_dht_means,
             label='Temperature - DHT11', marker='o', color='tomato')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('Temperature and Temperature DHT11 Data Together', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(18)
    plt.tight_layout()

    # Saving the plot as a photo
    plt.savefig(
        f'{folder_name}/TemperatureAndTemperatureDHT11DataTogether_{getCurrentTime()}.png')
    plt.close()


def saveHumidityAndDHTHumidityTogether():
    # Plotting temperature and humidity
    plt.figure(figsize=(15, 8))

    # humidity plot
    plt.plot(humidity_means.index, humidity_means,
             label='Humidity - SCD40', marker='o', color='royalblue')
    # humidity DHT11 plot
    plt.plot(humidity_dht_means.index, humidity_dht_means,
             label='Humidity - DHT11', marker='o', color='lightblue')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('Humidity and Humidity DHT11 Data Together', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(18)
    plt.tight_layout()

    # Saving the plot as a photo
    plt.savefig(
        f'{folder_name}/HumidityAndHumidityDHT11DataTogether{getCurrentTime()}.png')
    plt.close()


def saveSCD40AndDHTTogetherWithOutMeanSampling():
    plt.figure(figsize=(15, 8))

    # Plotting raw data from the DataFrame columns
    plt.plot(data.index, data['field2'],
             label='Temperature - SCD40', marker='o', color='red')
    plt.plot(data.index, data['field5'],
             label='Temperature - DHT11', marker='o', color='tomato')
    plt.plot(data.index, data['field3'],
             label='Humidity - SCD40', marker='o', color='royalblue')
    plt.plot(data.index, data['field6'],
             label='Humidity - DHT11', marker='o', color='lightblue')

    # plt.plot(data.index, data['field4'],
    #          label='co2_means', marker='o', color='grey')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Value', fontsize=20)
    plt.title('SCD40 and DHT11 Data With Out Mean Sampling', fontsize=20)
    plt.grid(True)
    plt.legend()
    setLabelSize(20)
    setTicksSize(18)
    plt.tight_layout()
    # plt.show()
    plt.savefig(
        f'{folder_name}/SCD40AndDHT11DataWithOutMeanSampling_{getCurrentTime()}.png')
    plt.close()


if __name__ == "__main__":
    folder_name = create_folder(
        f"{current_directory}/saveSCD40AndDHTComparision")
    saveSCD40AndDHTTogether()
    saveTempAndDHTTempTogether()
    saveHumidityAndDHTHumidityTogether()
    # Set the initial x-axis limits (you can change these values based on your data)
    saveSCD40AndDHTTogetherWithOutMeanSampling()
