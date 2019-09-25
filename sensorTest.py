import RPi.GPIO as GPIO
import time
from termcolor import colored

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = GPIO.input(17)
lastX = GPIO.input(23)
lastY = GPIO.input(24)

mode = 0

while True:
    switch_state = GPIO.input(17)
    button_state = GPIO.input(15)
    joystickX = GPIO.input(23)
    joystickY = GPIO.input(24)

    if switch_state == False and switch_state != last_state:
	mode = (mode + 1) % 3
        print("mode: " + str(mode))
        last_state = False
        time.sleep(0.5)

    if switch_state == True and switch_state != last_state:
        mode = (mode + 1) % 3
        print("mode: " + str(mode))
        last_state = True
        time.sleep(0.5)

    if mode == 0:
	if button_state == False:
		print('You are in mode 0! Nice!')
		time.sleep(0.2)

	if joystickX != lastX or joystickY != lastY:
		print(joystickX, joystickY)
		lastX = joystickX
		lastY = joystickY

    if mode == 1:
        if button_state == False:
                print('Mode 1 sucks. Get the hell out of here')
                time.sleep(0.2)

        if joystickX != lastX or joystickY != lastY:
                if joystickX == 0 and joystickY == 0:
			print('o o')
			print('---\n')
		if joystickX == 0 and joystickY == 1:
			print('~ ~')
			print('\_/\n')
		if joystickX == 1 and joystickY == 0:
			print('\ /')
			print('0 0')
			print('---\n')
		if joystickX == 1 and joystickY == 1:
			print('O O')
			print('<=>\n')
                lastX = joystickX
                lastY = joystickY

    if mode == 2:
        if button_state == False:
                print('You unlocked the ~secret hidden mode~. Good job you tryhard')
                time.sleep(0.2)

        if joystickX != lastX or joystickY != lastY:
                if joystickX == 0 and joystickY == 0:
			print colored('blood and fire', 'red')
                if joystickX == 0 and joystickY == 1:
                        print colored('ocean and sky', 'blue')
                if joystickX == 1 and joystickY == 0:
                        print colored('land and earth', 'green')
                if joystickX == 1 and joystickY == 1:
                        print colored('good', 'white'),'and', colored('EVIL', 'grey')
                lastX = joystickX
                lastY = joystickY

