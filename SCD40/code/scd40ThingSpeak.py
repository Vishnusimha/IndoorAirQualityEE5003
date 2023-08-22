import time
import board
import adafruit_scd4x
import requests

# Initialising the I2C communication with Raspberry Pi
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("SCD40 Sensor Serial no:", [hex(i) for i in scd4x.serial_number])
# Starting Low periodic measurement to get the readings
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
        print(f"CO2: {scd4x.CO2} ppm")
        print(f"Temperature: {scd4x.temperature:.1f} °C")
        print(f"Humidity: {scd4x.relative_humidity:.1f} %")
        print()
        sendDataToCloud(scd4x.CO2, scd4x.temperature, scd4x.relative_humidity)
        time.sleep(30)  # Added delay of 30 seconds between data updates
