import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

PUMP_ON = gpio.LOW
PUMP_OFF = gpio.HIGH
RACK_PUMP = 22
FLOOR_PLANT_PUMP = 23
LIGHT_ON = gpio.HIGH
LIGHT_OFF = gpio.LOW
LIGHT_SOCKET1 = 5
LIGHT_SOCKET2 = 6
TIMEZONE = 'America/Los_Angeles'
LIGHT_ON_TIME = '13:05'
LIGHT_OFF_TIME = '17:10'
gpio.setup(RACK_PUMP, gpio.OUT)
gpio.setup(FLOOR_PLANT_PUMP, gpio.OUT)
gpio.setup(LIGHT_SOCKET1, gpio.OUT)
gpio.setup(LIGHT_SOCKET2, gpio.OUT)
