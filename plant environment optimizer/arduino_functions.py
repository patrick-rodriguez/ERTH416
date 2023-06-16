import serial


def read_data(port, baud):
    with serial.Serial(port, baud, timeout=None) as arduino:
        unformatted_data = arduino.read(size=15)
        formatted_data = unformatted_data.decode("UTF-8").rstrip().split(",")

        temp = float(formatted_data[0])
        humidity = float(formatted_data[1])
        moisture_percentage = round((float(formatted_data[2]) / 625) * 100, 2)
        arduino.close()

        return temp, humidity, moisture_percentage


def read_temp():
    return read_data()[0]


def read_humidity():
    return read_data()[1]


def read_moisture():
    return read_data()[2]
