import time
import board
import adafruit_scd4x

# Initialising the I2C communication with Raspberry Pi
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("SCD40 Sensor Serial no:", [hex(i) for i in scd4x.serial_number])

# Starting Low periodic measurement to get the readings
scd4x.start_low_periodic_measurement()
print("Measuring CO2, Temperature and Humidity Values....")

while True:
    if scd4x.data_ready:
        print(f"CO2: {scd4x.CO2} ppm")
        print(f"Temperature: {scd4x.temperature:.1f} °C")
        print(f"Humidity: {scd4x.relative_humidity:.1f} %")
        print()
    time.sleep(5)
