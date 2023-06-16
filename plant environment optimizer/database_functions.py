import mysql.connector
from datetime import date

database = mysql.connector.connect(
    host="ix-dev.cs.uoregon.edu",
    port=3513,
    user="prodrig2",
    password="irodmario@2001"
)

cursor = database.cursor()
cursor.execute("USE erth416plantsdb")


def get_plant_data(name: str):
    query = (f"SELECT *\n"
             f"FROM plants\n"
             f"WHERE plantname = '{name}'")

    cursor.execute(query)
    data = cursor.fetchall()

    return data[0]


def get_moisture_data(name: str):
    data = get_plant_data(name)
    return data[1], data[2]


def get_temp_data(name: str):
    data = get_plant_data(name)

    return data[3], data[4]


def get_humidity_data(name: str):
    data = get_plant_data(name)

    return data[5], data[6]


def get_last_watered(name: str):
    data = get_plant_data(name)

    return data[7]


def update_last_watered(name: str):
    query = (f"UPDATE plants\n"
             f"SET last_watered = '{date.today()}'\n"
             f"WHERE plantname = '{name}'")

    cursor.execute(query)
    database.commit()

    return
