from time import sleep

from machine import Pin

bell_switch = Pin(9, Pin.IN)
door_switch = Pin(10, Pin.IN, pull=Pin.PULL_UP)

bell_ringer = Pin(3, Pin.OUT)
door_unlocker = Pin(4, Pin.OUT)


def unlock_door():
    door_unlocker.on()
    sleep(0.2)
    door_unlocker.off()
    print('Door unlocked')


def ring_bell():
    bell_ringer.on()
    sleep(0.2)
    bell_ringer.off()
    print('Bell rang')


def setup_triggers():
    bell_switch.irq(lambda pin: ring_bell(), Pin.IRQ_RISING)
    door_switch.irq(lambda pin: unlock_door(), Pin.IRQ_RISING)
