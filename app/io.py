from time import sleep

from machine import Pin

# From what this page describe it is better to not use GPIO 6,8 and 9
# https://wiki.seeedstudio.com/exp32c3_d9_d6_d8/
bell_switch = Pin(2, Pin.IN, pull=Pin.PULL_DOWN)
door_switch = Pin(3, Pin.IN, pull=Pin.PULL_UP)

bell_ringer = Pin(4, Pin.OUT, value=0, drive=Pin.DRIVE_2)
door_unlocker = Pin(5, Pin.OUT, value=0, drive=Pin.DRIVE_2)


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
