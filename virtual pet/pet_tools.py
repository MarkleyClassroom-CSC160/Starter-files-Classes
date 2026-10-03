# pet_tools.py -- starter
# The Virtual Pet's parts, a few helper functions, and the Pet class.
# pet_game.py imports what it needs from this file.

from time import sleep
from gpiozero import LED, Buzzer, Button

# ----- parts -----
lights = {
    "red": LED(17),
    "blue": LED(27),
    "green": LED(22)
}
buzzer = Buzzer(18, active_high=False, initial_value=False)
button = Button(4)

# ----- helper functions (given) -----

def light(color):
    # turn every light off, then turn on only the one named
    for led in lights.values():
        led.off()
    lights[color].on()


def lights_off():
    for led in lights.values():
        led.off()


def chirp():
    for beep in range(2):
        buzzer.on()
        sleep(0.1)
        buzzer.off()
        sleep(0.1)


def make_bar(value):
    # a 10-character bar: make_bar(3) gives [###.......]
    return "[" + "#" * value + "." * (10 - value) + "]"


# ----- the Pet class -----
# Step 1: write the Pet class here.
