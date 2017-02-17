import time
import uinput

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Runtime error. Try sudo")

KEYS = [uinput.KEY_1, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_7, uinput.KEY_8]
device = uinput.Device(KEYS)

# green, green, yellow, blue, red, pink, black, white
BUTTONS = [13, 6, 20, 19, 12, 16, 21, 5]

prev = [False, False, False, False, False, False, False, False]
curr = [False, False, False, False, False, False, False, False]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUTTONS, GPIO.IN, GPIO.PUD_DOWN)

def buttonPressed():
	for i in range(len(BUTTONS)):
            if GPIO.input(BUTTONS[i]):
                curr[i] = True
                if prev[i] == False:
                    return i
            else:
                curr[i] = False

        return -1

while True:
	try:
            button = buttonPressed()
	    if button >= 0:
                device.emit_click(KEYS[i])

	except KeyboardInterrupt:
            print "\nexiting"
            GPIO.cleanup()

