from RpiMotorLib import RpiMotorLib
from RPi.GPIO import RPi.GPIO
import argparse

dirStp = {"U": {"direction": 12, "step": 16},
          "D": {"direction": 18, "step": 32},
          "F": {"direction": 35, "step": 37},
          "R": {"direction": 3, "step": 5},
          "B": {"direction": 7, "step": 11},
          "L": {"direction": 13, "step": 15}}

# Choose pins for each motor; define GPIO pins
GPIO_pins = (-1, -1, -1)

# Instance of each motor (6)
motors = {}
motors["U"] = RpiMotorLib.A4988Nema(dirStp["U"][0], dirStp["U"][1], GPIO_pins, "A4988")
motors["L"] = RpiMotorLib.A4988Nema(dirStp["L"][0], dirStp["L"][1], GPIO_pins, "A4988")
motors["F"] = RpiMotorLib.A4988Nema(dirStp["F"][0], dirStp["F"][1], GPIO_pins, "A4988")
motors["R"] = RpiMotorLib.A4988Nema(dirStp["R"][0], dirStp["R"][1], GPIO_pins, "A4988")
motors["B"] = RpiMotorLib.A4988Nema(dirStp["B"][0], dirStp["B"][1], GPIO_pins, "A4988")
motors["D"] = RpiMotorLib.A4988Nema(dirStp["D"][0], dirStp["D"][1], GPIO_pins, "A4988")


def run(instructions, verbose=False):

    delay = .05
    for inst in instructions:

        if inst[0] in ["U", "L", "R", "D", "B", "F"]:
            if len(inst) == 1:
                motors[inst[0]].motor_go(clockwise=True, steps=100, stepdelay=delay)
            elif inst[1] == "\'":
                motors[inst[0]].motor_go(clockwise=False, steps=100, stepdelay=delay)
            elif inst[1] == "2":
                motors[inst[0]].motor_go(clockwise=True, steps=100, stepdelay=delay)
                
            if verbose:
                print(f"Completing instruction \'{inst}\'")
        else:
            raise TypeError("Incorrect instruction")

def test():

    for motor in motors.values():
        motor.motor_go(stepdelay=.05)
        motor.motor_go(clockwise=False, stepdelay=.05)

def sysArg():

    parser = argparse.ArgumentParser(description="Program for motors")
    options = parser.add_mutually_exclusive_group()
    options.add_argument("-t",  "--test", action="store_true", help="Tests all motors")
    options.add_argument("-r",  "--run", action="store_true", help="Runs program")
    args = parser.parse_args()

    if args.test:
        test()
    elif args.run:
        print("\nNo arguments provided\n")
        parser.print_help()

if __name__ == "__main__":
    sysArg()



