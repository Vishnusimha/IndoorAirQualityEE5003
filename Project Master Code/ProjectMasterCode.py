import time
import board
import adafruit_scd4x
import requests

i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("SCD40 Sensor Serial no:", [hex(i) for i in scd4x.serial_number])
# Starting Low periodic measurement.
scd4x.start_low_periodic_measurement()
print("Measuring CO2, Temperature and Humidity Values....")

# ThingSpeak endpoint and API KEY
API_ENDPOINT = "https://api.thingspeak.com/update"
API_KEY = "9MB5PUUHD6AKTA8Z"


def sendDataToCloud(CO2, temperature, humidity):
    print(CO2)
    print(temperature)
    print(humidity)
    print()

    # Creating payload with data and API key
    payload = {
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity,
        "field3": CO2
    }

    # Sending HTTP POST type request to ThingSpeak
    response = requests.post(API_ENDPOINT, params=payload)

    # Printing response status code
    print("Data sent to ThingSpeak Cloud. Status Code:", response.status_code)


while True:
    if scd4x.data_ready:
        print("CO2: %d ppm" % scd4x.CO2)
        print("Temperature: %0.1f *C" % scd4x.temperature)
        print("Humidity: %0.1f %%" % scd4x.relative_humidity)
        print()
        sendDataToCloud(scd4x.CO2, scd4x.temperature, scd4x.relative_humidity)
        time.sleep(30)  # Added delay of 30 seconds between data updates
