import requests
import random
import time

# ThingSpeak endpoint and API KEY
API_ENDPOINT = "https://api.thingspeak.com/update"
API_KEY = "9MB5PUUHD6AKTA8Z"


def sendDataToCloud():
    print(temperature)
    print(humidity)

    # Creating payload with sample data and API key
    payload = {
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity}

    # Sending HTTP POST type request to ThingSpeak
    response = requests.post(API_ENDPOINT, params=payload)

    # Printing response status code
    print("Data sent. Status Code:", response.status_code)


try:
    while True:
        # Generating fake random data for testing
        temperature = random.uniform(10.0, 30.0)
        humidity = random.uniform(40.0, 80.0)
        sendDataToCloud()
        time.sleep(15)  # Added delayy for 15 seconds between data updates

except KeyboardInterrupt:
    pass
