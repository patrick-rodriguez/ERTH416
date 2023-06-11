import serial
import time
import csv
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import numpy as np
from datetime import datetime, timedelta

csv_file = r"sensor_data.csv"

#  The following commented lines represent the data collection process.
#  Data was collected for six hours writing to sensor_data.csv
"""
port = "COM3"
baud_rate = 115200
sensor = serial.Serial(port, baud_rate)


header = ("PM1.0 concentration, PM2.5 concentration, PM10 concentration, Pressure(hPa), "  # Header of csv file.
          "Humidity (RH), Temperature (oC), Time")


f = open(csv_file, "w")
f.write(f"{header}\n")  # Write the header to sensor_data.csv
f.close()  # Close to avoid any memory leaks

t_end = time.time() + 60 * 360 # Time from start of execution 6 hours later.


with open(csv_file, "a") as f:
    while time.time() < t_end:  # Run for six hours
        recorded_time = datetime.now().strftime("%H:%M")  # Turn datetime object into string formatted "%H:%M"
        unformatted_data = sensor.readline() 
        formatted_data = unformatted_data.decode("UTF-8").rstrip()  # Decode and rid of escape characters
        f.write(f"{formatted_data},{recorded_time}\n")  # Write sensor data and time it was recorded at to csv
        time.sleep(30)  # Collect every 30 seconds
"""

# The following lines represent interpreting the csv file to be graphed via matplotlib.

# List for each column of data in csv file.
pm10_concentration = []
pm25_concentration = []
pm100_concentration = []
pressure = []
humidity = []
temperature = []
time = []

pm10_concentration_no_smoking = []
pm25_concentration_no_smoking = []
pm100_concentration_no_smoking = []
time_no_smoking = []

with open(csv_file, "r") as f:
    data = csv.reader(f)
    next(data)  # read past header line
    for row in data:
        # cast data into their respective datatypes and append them to their respective arrays
        pm10_concentration.append(int(row[0]))
        pm25_concentration.append(int(row[1]))
        pm100_concentration.append(int(row[2]))

        if int(row[2]) <= 10:
            pm10_concentration_no_smoking.append(int(row[0]))
            pm25_concentration_no_smoking.append(int(row[1]))
            pm100_concentration_no_smoking.append(int(row[2]))

        pressure.append(float(row[3]))
        humidity.append(float(row[4]))
        temperature.append(float(row[5]))
        #  time.append(float(row[6]))

#  formatted time column incorrectly so had to repopulate it
starting_time = datetime(2023, 6, 9, 18, 45, 30, 0)  # start time for data collection
for i in range(699):
    time.append((starting_time + timedelta(seconds=30.8571428571 * i)))
    if i <= 625:
        time_no_smoking.append((starting_time + timedelta(seconds=37.0497427101 * i)))

print(len(time_no_smoking), len(pm100_concentration_no_smoking))

ax1 = plt.subplot()
plt.title("Particle Matter Concentration Over Time (18:45 - 0:45)")
ax1.scatter(time, pm10_concentration, color="blue", s=8, label="PM1.0 Concentration (µg/m^3)")
ax1.scatter(time, pm25_concentration, color="orange", s=8, label="PM2.5 Concentration (µg/m^3)")
ax1.scatter(time, pm100_concentration, color="purple", s=8, label="PM10.0 Concentration (µg/m^3)")
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax1.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

plt.xlabel("Time")
plt.ylabel("PM Concentration (µg/m^3)")
plt.xticks(rotation=45)
plt.xlim(starting_time - timedelta(seconds=1), starting_time + timedelta(seconds=30.8571428571 * 699) -
         timedelta(seconds=1))
plt.legend()
plt.savefig(r"C:\Users\patri\OneDrive\Desktop\ERTH416\ERTH416\Assignment 4\pmconcentration_with_smoking")
plt.show()

ax2 = plt.subplot()
plt.title("Temperature (oC) Over Time (18:45 to 0:45)")
ax2.scatter(time, temperature, s=5, label="Temperature (oC)")
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax2.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

plt.xlabel("Time")
plt.ylabel("Temperature (oC)")
plt.xticks(rotation=45)
plt.xlim(starting_time - timedelta(seconds=1), starting_time + timedelta(seconds=30.8571428571 * 699) -
         timedelta(seconds=1))
plt.legend()
plt.savefig(r"C:\Users\patri\OneDrive\Desktop\ERTH416\ERTH416\Assignment 4\temperature")
plt.show()

ax3 = plt.subplot()
plt.title("Relative Humidity Over Time (18:45 to 0:45)")
ax3.scatter(time, humidity, s=5, label="Relative Humidty (RH)")
ax3.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax3.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

plt.xlabel("Time")
plt.ylabel("Relative Humidity")
plt.xticks(rotation=45)
plt.xlim(starting_time - timedelta(seconds=1), starting_time + timedelta(seconds=30.8571428571 * 699) -
         timedelta(seconds=1))
plt.legend()
plt.savefig(r"C:\Users\patri\OneDrive\Desktop\ERTH416\ERTH416\Assignment 4\humidity")
plt.show()

ax4 = plt.subplot()
plt.title("Environmental Air Pressure Over Time (18:45 to 0:45)")
ax4.scatter(time, pressure, s=5, label="Air Presure (hPa)")
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax4.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

plt.xlabel("Time")
plt.ylabel("Pressure (hPa)")
plt.xticks(rotation=45)
plt.xlim(starting_time - timedelta(seconds=1), starting_time + timedelta(seconds=30.8571428571 * 699) -
         timedelta(seconds=1))
plt.legend()
plt.savefig(r"C:\Users\patri\OneDrive\Desktop\ERTH416\ERTH416\Assignment 4\pressure")
plt.show()

ax5 = plt.subplot()
plt.title("Particle Matter Concentration Over Time (Smoking Filtered)")
ax5.scatter(time_no_smoking, pm10_concentration_no_smoking, color="blue", s=8, label="PM1.0 Concentration (µg/m^3)")
ax5.scatter(time_no_smoking, pm25_concentration_no_smoking, color="orange", s=8, label="PM2.5 Concentration (µg/m^3)")
ax5.scatter(time_no_smoking, pm100_concentration_no_smoking, color="purple", s=8, label="PM10.0 Concentration (µg/m^3)")
ax5.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax5.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

plt.xlabel("Time")
plt.ylabel("PM Concentration (µg/m^3)")
plt.xticks(rotation=45)
plt.xlim(starting_time - timedelta(seconds=1), starting_time + timedelta(seconds=30.8571428571 * 699) -
         timedelta(seconds=1))
plt.legend()
plt.savefig(r"C:\Users\patri\OneDrive\Desktop\ERTH416\ERTH416\Assignment 4\pmconcentration_smoking_filtered")
plt.show()
