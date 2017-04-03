# WaterMeter_Sensor
Reading the TI DRV5053 hall effect sensor to detect flow through the city water meter using Python and a Raspberry Pi. The meter I have is the Badger Meter Model 35. The sensor is non-invasive and can be removed if needed.

The sensor VCC is connected to 5V and the output from the sensor is 0V to +2V DC.

The Python script will receive an interrupt and debounce it every time the output of the sensor toggles. 

The script will provide an RPM reading for the meter and determine how much water is being consumed. 
