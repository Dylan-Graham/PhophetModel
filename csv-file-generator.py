import csv
import datetime
import random

# Define the start and end time for the data generation
start_time = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
end_time = start_time + datetime.timedelta(hours=24)

# Define the list of sensor names and descriptions
sensors = ["Sensor1", "Sensor2", "Sensor3"]
descriptions = ["Temperature sensor", "Pressure sensor", "Humidity sensor"]

# Open CSV file for writing
with open("sensor_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sensor", "timestamp", "value", "value_float", "description"])

    # Generate data for each 15-minute interval
    current_time = start_time
    while current_time < end_time:
        for sensor, description in zip(sensors, descriptions):
            # Generate random value for the sensor
            value = random.randint(0, 100)
            value_float = round(random.uniform(0.0, 100.0), 2)

            # Write data to CSV
            writer.writerow(
                [
                    sensor,
                    current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    value,
                    value_float,
                    description,
                ]
            )

        # Move to the next 15-minute interval
        current_time += datetime.timedelta(minutes=15)
