# Reports generation

## Hourly Report generation codes

- [**generateHourlyReportsRPI.py** ](generateHourlyReports.py)code generates the **Temperature, Humidity and CO2** values graphs for each hour data and save as photos in a separate folder with proper time stamp.

## 24 Hours data/Full data Report generation codes

- [**generate24HReportTogetherAndSeparatelyRPI.py**](generate24HReportTogetherAndSeparatelyRPI.py) code generates the **Temperature, Humidity and CO2 values** graphs for whole file data and save as photos in a separate folder.

- [**generate24HReportTogetherAndSeparatelyWithVentilation.py**](generate24HReportTogetherAndSeparatelyWithVentilation.py) code generates the **Temperature, Humidity and CO2 values graphs along with VENTILATION MARKINGS** for whole file data and save as photos in a separate folder.

- [**plotTempHumiditySCD40AndDHT11Comparisions.py**](plotTempHumiditySCD40AndDHT11Comparisions.py) code generates the report for SCD40 and DHT11 sensor data.

## Results of this project

The results that are documneted in the final report were saved in different folders below under **Reportsgeneration** folder

- [Results scenario 1](<Results Scenario 1>) (/IndoorAirQualityEE5003/Reportsgeneration/Results Scenario 1)
- [Results scenario 2](<Results Scenario 2>) (/IndoorAirQualityEE5003/Reportsgeneration/Results Scenario 2)
- Results scenario 3 (/IndoorAirQualityEE5003/Reportsgeneration/[ComparitiveAnalysisResultsBedroom](ComparitiveAnalysisResultsBedroom))


### CSV files for report generation

**feeds.csv** is the data imported from the ThingSpeak cloud platform.

**random_data.csv** is the file with sample fake data to test the report generation. This was just created in the starting and no need to utilise this.

**testdata.csv** is the file with some real data followed by fake data to plot until the end of the day to test the report generation.
