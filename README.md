# IndoorAirQualityEE5003

## Intelligent Indoor Air Quality and Ventilation Management in Confined Spaces using IoT

### Problem Statement

- In recent years, energy-efficient homes have become more airtight, leading to decreased ventilation and potential health concerns.
- We don’t know at what time CO2 levels are high 
- Everyone cannot operate windows/ventilators often to allow fresh air
- No access to data all the time with and without internet

### Main Objective of Project

- Implement an air quality and temperature monitoring system using Raspberry Pi and an Adafruit SCD40 Sensor (CO2, humidity, and temperature).
- Automate responsive actions such as vent control using a servo motor to optimise the indoor environment.
- Provide timely alerts to notify individuals of any potential air quality issues.
- Automate generation of air quality reports in Raspberry Pi (Provided results like how often it's required to allow fresh air or operate ventilation)

### Added Objectives while development

- To add server functionality to the Raspberry Pi and expose APIs to get the data in different formats (JSON, CSV)
- To develop a reliable Android mobile application that shows recent and historical data from ThingSpeak Cloud and Raspberry Sever to continuously provide users with sensor data information.
- To test the project with an additional DHT11 sensor to make a comparative analysis of the performance


## Information about git repository

The entire project code was implemented using different branches, and after each task was completed, the related branch was merged into the master-integration branch. And at final stage that was merged into main branch, so all the latest code can be found in main branch.

***To retain the old changes, No branches were deleted from starting***

### All Branches in the repository

![List of all Branches in the repository](<Screenshot 2023-08-22 at 2.26.05 p.m..png>)

### Project Board

#### Whole project was implemented by following below steps:

- Created a task in the project board and defined what the task is, and updated the progress of the task promptly.
- Created a separate branch from the master-integration branch for each valuable feature.
- Worked on that branch, and when completed, all the changes were merged into the master-integration branch

So each branch will have some additional features or changes right from starting. And all the changes can be seen in the main branch together.

![Project Board View 1](<Screenshot 2023-08-22 at 2.29.04 p.m..png>)

**Another View**

![Project Board Table View 3](<Screenshot 2023-08-22 at 2.29.35 p.m..png>)
