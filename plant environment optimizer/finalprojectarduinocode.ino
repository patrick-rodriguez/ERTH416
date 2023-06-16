#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;

unsigned long delayTime = 2000;
int moistureSensor = A0;

void setup() {
    Serial.begin(9600); // initialize the serial communication between Arduino & laptop
    while(!Serial);    // time to get serial running

    unsigned status;
    
    status = bme.begin(0x76); // initialize BME280 sensor with I2C address

    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        while (1) delay(10);
    }
}

void loop() { 
    Serial.print(bme.readTemperature()); // read BME280 temperature sensor
    Serial.print(",");
    Serial.print(bme.readHumidity()); // read BME280 humidity sensor
    Serial.print(",");
    Serial.println(analogRead(moistureSensor)); // read value from Grove moisture sensor
    delay(delayTime); // delay by 2 seconds to ensure consistency and stability between reads
}