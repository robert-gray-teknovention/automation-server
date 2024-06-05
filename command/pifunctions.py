import time
import controller.config as conf
import RPi.GPIO as gpio


def pump_run(pump, duration, callback):
    print("We are running as PI")
    print("Duration ", duration)
    gpio.output(pump, conf.PUMP_ON)
    time.sleep(duration)
    gpio.output(pump, conf.PUMP_OFF)
    print("We are finished")
    callback()


def light_control(socket, state, callback):
    print("We are turning the lights ", state)
    gpio.output(socket, state)
    callback()


def output_run_duration(pin, on_state, duration, callback):
    print(pin, ' ', on_state, ' ', duration)
    gpio.output(pin, on_state)
    time.sleep(duration)
    if on_state == gpio.LOW:
        gpio.output(pin, gpio.HIGH)
    else:
        gpio.output(pin, gpio.LOW)
    callback()


def output_control(pin, on_off, callback):
    print("Pin", pin, "ON" if on_off else "OFF")
    gpio.output(pin, on_off)
    callback()
