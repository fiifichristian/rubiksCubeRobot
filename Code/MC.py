#import the RpiMotorLib library
import time, argparse, sys
# import RPi.GPIO as GPIO
# from RpiMotorLib import RpiMotorLib
import IP


# #create a list of motors to be controlledrubik 
# motors = ["T", "D", "R", "L", "B", "F"]

# #create a dictionary with the motor names as keys and the corresponding motor objects as values
# motor_dict = {}
# motor_dict[motors[0]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )
# motor_dict[motors[1]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )
# motor_dict[motors[2]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )
# motor_dict[motors[3]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )
# motor_dict[motors[4]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )
# motor_dict[motors[5]] = RpiMotorLib.A4988Nema(motor, direction_pin=2, step_pin=4, mode_pins= )


# def checkInstructions(instructions):

#     print("Checking Instructions")
#     for instruction in instructions:
#         if len(instruction) != 2:
#             print("Error: Invalid instruction format. Each instruction should be a 2 character string.")
#             return
#         if instruction[0] not in ["F", "B", "L", "R", "D", "U"]:
#             print("Error: Invalid face. The first character of each instruction should be one of 'F', 'B', 'L', 'R', 'D' or 'U'.")
#             return
#         if instruction[1] not in [" ", "'", "2"]:
#             print("Error: Invalid direction. The second character of each instruction should be one of ' ', ''', '2'.")
#             return


# def control_motors(instructions): #function to control the motors based on instructions given in an array of strings

#     for instruction in instructions: #loop through each instruction in instructions array

#         face = instruction[0] #store first character of instruction as face variable
#         direction = instruction[1] #store second character of instruction as direction variable
#         RpiMotorLib.motor_go(motor_dict[face],direction)