import time
import board
import adafruit_scd4x
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo motor
servo_pin = 22
pwm_frequency = 50
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, pwm_frequency)

# LED
led_pin = 27
GPIO.setup(led_pin, GPIO.OUT)

# SCD40
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("SCD40 Sensor Serial no:", [hex(i) for i in scd4x.serial_number])
# Starting Low periodic measurement.
scd4x.start_low_periodic_measurement()
print("Measuring CO2, Temperature and Humidity Values....")

# ThingSpeak endpoint and API KEY
API_ENDPOINT = "https://api.thingspeak.com/update"
API_KEY = "9MB5PUUHD6AKTA8Z"


def sendDataToCloud(CO2, temperature, humidity, current_time):
    print(CO2)
    print(temperature)
    print(humidity)
    print(current_time)
    print()

    # Creating payload with data and API key
    payload = {
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity,
        "field3": CO2,
        "field4": current_time
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


try:
    # Start the PWM signal with 0 (servo at 0 degrees)
    servo_pwm.start(0)
    while True:
        if scd4x.data_ready:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("current time %s " % current_time)
            print("CO2: %d ppm" % scd4x.CO2)
            print("Temperature: %0.1f *C" % scd4x.temperature)
            print("Humidity: %0.1f %%" % scd4x.relative_humidity)
            print()
            sendDataToCloud(scd4x.CO2, scd4x.temperature,
                            scd4x.relative_humidity, current_time)
            if scd4x.temperature > 23 or scd4x.relative_humidity > 70 or scd4x.CO2 > 900:
                blink_led(num_times=2, delay=0.7)
                print("LED blink sent")
                set_servo_angle(90)
            else:
                set_servo_angle(0)
            print("sleeping...")
            time.sleep(5)

except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()
