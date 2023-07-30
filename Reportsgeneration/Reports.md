# Reports generation

## Hourly Reports

**generateHourlyReportsRPI.py** is the file that works perfectly in Raspberry Pi, as there is difference in getting current directory in Mac and RPI.

This code generates the **Temperature, Humidity and CO2** values graphs for each hour data and save as photos in a separate folder

## 24 Hours data Reports

**generate24HReportTogetherAndSeparatelyRPI.py** is the file that works perfectly in Raspberry Pi, as there is difference in getting current directory in Mac and RPI.

This code generates the Temperature, Humidity and CO2 values graphs for whole file data and save as photos in a separate folder.

### CSV files for report generation

**feeds.csv** is the data imported from the ThingSpeak cloud platform.

**random_data.csv** is the file with sample fake data to test the report generation.

**testdata.csv** is the file with some real data followed by fake data to plot until the end of the day to test the report generation.
