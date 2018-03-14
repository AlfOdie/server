#!/usr/bin/env python
import socket
import serial
import pygame
# replace [serial_item] with output of ls dev/tty*
# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
# second argument is baud rate
ser = serial.Serial('/dev/tty4', 9600)
# to avoid interpreting noise, these are the first two bytes of every command
COMMAND_BYTE_PAIR = bytearray(b'\xFF\xEE')

def sendToArduio(command):
	print(COMMAND_BYTE_PAIR.append(command))
	ser.write(COMMAND_BYTE_PAIR.append(command))
	
# functions to interface with arduino
def button1():
	print("Button 1 command recieved")
	x = bytearray(b'\xB1')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))
	
def button2():
	print("Button 2 command recieved")
	x = bytearray(b'\xB2')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button3():
	print("Button 3 command recieved")
	x = bytearray(b'\xB3')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button4():
	print("Button 4 command recieved")
	x = bytearray(b'\xB4')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button5():
	print("Button 5 command recieved")
	x = bytearray(b'\xB5')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button6():
	print("Button 6 command recieved")
	x = bytearray(b'\xB6')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button7():
	print("Button 7 command recieved")
	x = bytearray(b'\xB7')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button8():
	print("Button 8 command recieved")
	x = bytearray(b'\xB8')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button9():
	print("Button 9 command recieved")
	sx = bytearray(b'\xB9')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button10():
	print("Button 10 command recieved")
	x = bytearray(b'\xB0')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button11():
	print("Button 11 command recieved")
	x = bytearray(b'\xBA')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

def button12():
	print("Button 12 command recieved")
	x = bytearray(b'\xBB')
	print("Sending command %s to arduino", COMMAND_BYTE_PAIR.append(x))
	sendToArduio(x))

	
# byte assignments for commands TODO
commands = {
	b'\xB1': button1,
	b'\xB2': button2,
	b'\xB3': button3,
	b'\xB4': button4,
	b'\xB5': button5,
	b'\xB6': button6,
	b'\xB7': button7,
	b'\xB8': button8,
	b'\xB9': button9,
	b'\xB0': button10,
	b'\xBA': button11,
	b'\xBB': button12,
}


def startServer():
	# start server
	UDP_IP = "127.0.0.1"
	UDP_PORT = 8000
	print("Starting connection with ip %s on port %d" %(UDP_IP, UDP_PORT))
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((UDP_IP, UDP_PORT))
	while True:
		data, addr = sock.recvfrom(1024)
		commands[data]()
		# send response
		sock.sendto(data, addr)



#################### STOLEN FRON CLIENT.PY ###############

# The steelseries gamepad used to set this up has the following characteristics
# When running the controller test program, the axes are as follows:
#
# 0: Left stick's left-to-right. Left is -1, right is 1
# 1: Left stick's up-to-down. Up is -1, down is 1
# **When the mode light on the controller is red
# 2: Right stick's left-to-right. Left is -1, right is 1
# 3: Right stick's up-to-down. Up is -1, down is 1
#
# The buttons are straightforward. Each button has a number on it, n, and
# and number that represents in in the code, m.
# m = n - 1
# If the button says 1 on it, then the code has it as button 0
# There are 12 buttons in this manner
#
#
# This code will be compatible with other controllers, but the behavior is not guaranteed,
# don't go to competition without verifying the controller works the way it is expected to
# in the hardware it is running in
#


def handlebutton(number, value):
    """
    :param number: the number of the button, as represented in the code (m)
    :param value: pressed or released
    :return:
    """
    if value == 0:  # button has been pressed. most methods will activate on this condition
        if number == 0:   # on the steelseries gamepad, this in the top button on the right
            print("1 pressed")
            button1()
        elif number == 1: # on the steelseries gamepad, this in the right button on the right
            print("2 pressed")
            button2()
        elif number == 2: # on the steelseries gamepad, this in the bottom button on the right
            button3()
            senddata(b'\xB3')
        elif number == 3: # on the steelseries gamepad, this in the left button on the right
            print("4 pressed")
            button4()
        elif number == 4: # on the steelseries gamepad, this in the trigger button on the left
            print("5 pressed")
            button5()
        elif number == 5: # on the steelseries gamepad, this in the trigger button on the right
            print("6 pressed")
            button6()
        elif number == 6: # on the steelseries gamepad, this in the bumper button on the left
            print("7 pressed")
            button7()
        elif number == 7: # on the steelseries gamepad, this in the bumper button on the right
            print("8 pressed")
            button8()
        elif number == 8: # on the steelseries gamepad, this is the left middle button
            print("9 pressed")
            button9()
        elif number == 9: # on the steelseries gamepad, this is the right middle button
            print("10 prssed")
            button10()
        elif number == 10: # on the steelseries gamepad, this is pressing the left control stick in
            print("11 pressed")
            button11()
        elif number == 11: # on the steelseries gamepad, this is pressing the right control stick in
            print("12 pressed")
            button12()
        else:
            print("This isn't a supported button!")
            print("This shouldn't do anything")


def handleaxis(number, value):
    if number == 0: # left stick's left to right
        if value < -0.5:
            print("Left stick to the left")
            senddata( b'\xD9')
        elif value > 0.5:
            print("Left stick to the right")
            senddata( b'\xD7')
        #else:
            #   senddata( b'\xD1')
            #   print("Left stick LR neutral")
    elif number == 1: # left stick's up to down
        if value < -0.5:
            print("Left stick forward")
            senddata( b'\xD6')
        elif value > 0.5:
            print("Left stick backward")
            senddata( b'\xD8')
        #else:
        #    senddata( b'\xD5')
        #    print("Left stick UD neutral")
        elif number == 2: # right stick's left to right
            if value < -0.5:
                print("Right stick left")
                senddata( b'\xDE')
            elif value > 0.5:
                print("Right stick right")
                senddata( b'\xDC')
        #else:
        #    senddata( b'\xDA')
        #    print("Right stick LR neutral")
    elif number == 3: # right stick's up to down
        if value < -0.5:
            ## Rightstick_down
            print("Right stick up")
        elif value > 0.5:
             ## Rightstick_down
            print("Right stick down")
        #else:
        #senddata( b'\xDA')
        #    print("Right stick UD neutral") '''


def handlehat(number, value):

    if number == 0: # left stick's left to right
        if value[0] == 0 and value[1] == 1:
            print("DPad up")
            senddata(b'\xD1')
        elif value[0] == 1 and value[1] == 0:
            print("DPad right")
            senddata(b'\xD2')
        elif value[0] == 0 and value[1] == -1:
            print("DPad down")
            senddata(b'\xD3')
        elif value[0] == -1 and value[1] == 0:
            print("DPad left")
            senddata(b'\xD4')


def handlecontrol( number, value, conttype = "button" ):
    """
    :param number: the ID number of the button, axis, or other control
    :param value:   the value inputted. the meaning will depend on control type.
                    button values are down and up for pressed and released
                    respectively
    :param conttype: default is "button". there is also "axis"
    :return:
    """
    if conttype == "button":
        handlebutton(number, value)
    elif conttype == "axis":
        handleaxis(number, value)
    elif conttype == "hat":
        handlehat(number, value)



def manual_overide():  
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # command handling. events should be sent to server
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            handlecontrol(event.axis,event.value,"axis")
        if event.type == pygame.JOYBUTTONDOWN:
            handlecontrol(event.button,0,"button")
        if event.type == pygame.JOYBUTTONUP:
            handlecontrol(event.button,1,"button")
        if event.type == pygame.JOYHATMOTION:
            handlecontrol(event.hat,event.value,"hat")	
	
		
	
pygame.init()  # init pygame
pygame.joystick.init()  # init pygame joysticks
joysticks = pygame.joystick.Joystick(0)
joycount = pygame.joystick.get_count()
print( joycount )
for x in (0, joycount):
print(joysticks)  # print list of connected controllers
while(joycount == 0)
{
	startServer()
	joycount = pygame.joystick.get_count()
}
manual_overide()
