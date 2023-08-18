import time
import board
import adafruit_scd4x
import requests
import RPi.GPIO as GPIO
import csv
import os
import http.server
import socketserver
import threading
import json

# scd40ThingSpeakLEDServoCSVServerEmail code changes below.

# Setting GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Constants
servo_pin = 22
pwm_frequency = 50
led_pin = 27

# configurable values
temperatureThresholdForEmail = 22
co2ThresholdForEmail = 1000
humidityLowerThresholdForEmail = 40

temperatureThresholdForVentilation = 25
co2ThresholdForVentilation = 1000

# ThingSpeak endpoint and API KEY
API_ENDPOINT = "https://api.thingspeak.com/update"
API_KEY = "9MB5PUUHD6AKTA8Z"

# Servo motor initialisation
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, pwm_frequency)

# LED initialisation
GPIO.setup(led_pin, GPIO.OUT)

# SCD40 initialisation
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("SCD40 Sensor Serial no:", [hex(i) for i in scd4x.serial_number])

# Starting Low periodic measurement.
scd4x.start_low_periodic_measurement()
print("Measuring CO2, Temperature and Humidity Values....")

# Getting current directory path
current_directory = os.path.dirname(os.path.abspath(__file__))
# Getting parent directory path
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
print(current_directory)

# CSV file path
CSV_FILE_PATH = f"{grandparent_directory}/Reportsgeneration/sensordata.csv"
print(f"Data saving to Directory -> {CSV_FILE_PATH}")
# creating a CSV file if it not exists in that path


def create_csv_file():
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["created_at", "entry_id", "field1",
                        "field2", "field3", "field4", "field7"])


def get_next_entry_id():
    with open(CSV_FILE_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Reading the contents of the file into a list
        rows = list(reader)
        # Extract existing entry_ids from CSV file
        entry_ids = [int(row[1]) for row in rows if row[1].isdigit()]
        if entry_ids:
            return max(entry_ids) + 1
        else:
            return 1


def save_data_to_csv(created_at, temperature, humidity, co2, isVentilationRequired):
    # Function to save data into  a CSV file
    entry_id = get_next_entry_id()
    with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Add column headings if the file is empty
        if csvfile.tell() == 0:
            writer.writerow(["created_at", "entry_id",
                            "field1", "field2", "field3", "field4", "field7"])
        writer.writerow([created_at, entry_id, created_at,
                        temperature, humidity, co2, isVentilationRequired])


def sendDataToCloud(CO2, temperature, humidity, current_time, isVentilationRequired):
    print(f"Current time: {current_time}")
    print(f"CO2: {CO2} ppm")
    print(f"Temperature: {temperature:.1f} °C")
    print(f"Humidity: {humidity:.1f} %")
    print(f"isVentilationRequired: {isVentilationRequired}")
    print()
    # Creating payload with data and API key
    payload = {
        "api_key": API_KEY,
        "field1": current_time,
        "field2": temperature,
        "field3": humidity,
        "field4": CO2,
        "field7": isVentilationRequired
    }

    # Sending HTTP POST type request to ThingSpeak
    response = requests.post(API_ENDPOINT, params=payload)

    # Printing response status code
    print("Data sent to ThingSpeak Cloud. Status Code:", response.status_code)


def blink_led(num_times, delay):
    print("LED blink intruction arrived")
    for _ in range(num_times):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(delay)


def set_servo_angle(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)


# Checking if the CSV file exists, if not, This will create one
if not os.path.exists(CSV_FILE_PATH):
    create_csv_file()


class CSVHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Geting the request path (endpoint)
        path = self.path

        if path == '/csv':
            # if requested is for CSV data
            self.send_response(200)
            self.send_header('Content-type', 'text/csv')
            self.end_headers()

            csv_filename = "/home/vishnu/Downloads/IndoorAirQualityEE5003/Reportsgeneration/sensordata.csv"
            # Reading CSV data
            with open(csv_filename, 'r') as file:
                csv_data = file.read()

            self.wfile.write(bytes(csv_data, 'utf-8'))

        elif path == '/json':
            # If requested is for JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            csv_filename = "/home/vishnu/Downloads/IndoorAirQualityEE5003/Reportsgeneration/sensordata.csv"

            # Reading CSV data and converting it to a list of dictionaries
            csv_data = []
            with open(csv_filename, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    csv_data.append(row)

            # Converting list of dictionaries to a JSON object
            json_data = json.dumps(csv_data)

            self.wfile.write(bytes(json_data, 'utf-8'))

        else:
            # when the request path is not in options, returning 404 error
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Error 404: Not Found. Request /csv or /json')


def start_server():
    address = ('192.168.1.43', 8000)
    server = socketserver.TCPServer(address, CSVHandler)

    print(f'Server running on http://{address[0]}:{address[1]}/')
    server.serve_forever()


def sendEmailAlert(current_time, CO2, temperature, humidity):
    emailAlertKey = "TAKCvpzE5nuYVf+1Z3b"
    subject = "Indoor Monitoring Alert"
    body = f"Current time: {current_time}\n CO2: {scd4x.CO2} ppm \n Temperature: {scd4x.temperature:.1f} °C \n Humidity: {scd4x.relative_humidity:.1f} %"
    url = "https://api.thingspeak.com/alerts/send"
    headers = {
        "ThingSpeak-Alerts-API-Key": emailAlertKey,
        "Content-Type": "application/json"
    }
    data = {
        "subject": subject,
        "body": body
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Email alert sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send email alert: {e}")


def main():
    try:
        # Start the PWM signal with 0 (servo at 0 degrees)
        servo_pwm.start(0)
        while True:
            if scd4x.data_ready:
                t = time.localtime()
                current_time = time.strftime("%Y-%m-%dT%H:%M:%S%z", t)
                print("Got readings")
                print()
                isVentilationRequired = False
                if scd4x.temperature > temperatureThresholdForVentilation or scd4x.CO2 > co2ThresholdForVentilation:
                    blink_led(num_times=2, delay=0.7)
                    print("Ventilating...")
                    isVentilationRequired = True
                    set_servo_angle(90)
                else:
                    set_servo_angle(0)
                    print()
                save_data_to_csv(current_time, scd4x.temperature,
                                 scd4x.relative_humidity, scd4x.CO2, isVentilationRequired)
                sendDataToCloud(scd4x.CO2, scd4x.temperature,
                                scd4x.relative_humidity, current_time, isVentilationRequired)
                if scd4x.temperature > temperatureThresholdForEmail or scd4x.CO2 > co2ThresholdForEmail or scd4x.relative_humidity < humidityLowerThresholdForEmail:
                    sendEmailAlert(current_time, scd4x.CO2,
                                   scd4x.temperature, scd4x.relative_humidity)

                print("sleeping...")
                time.sleep(5)

    except KeyboardInterrupt:
        servo_pwm.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    # Created and starting server thread
    server_thread = threading.Thread(target=start_server)
    # Setting the thread as daemon this allows it to exit when the main thread exits
    server_thread.daemon = True
    server_thread.start()  # Starting Thread
    main()
