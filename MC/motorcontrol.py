import sys
import RpiMotorLib as mLib
# Must replace with pi path
sys.path.append('C:\\Users\\Fiifi\\OneDrive - Loughborough University\\RubikCube\\IP') 
import IP


motorInfo = {

    "top" : {"direction": 22,
                    "step": 1,
                    "other": (21,21,21)
                    },
    "bottom" : {"direction": 22,
                "step": 1,
                "other": (21,21,21)
                },
    "left" : {"direction": 22,
                    "step": 1,
                    "other": (21,21,21)
                    },
    "right" : {"direction": 22,
                    "step": 1,
                    "other": (21,21,21)
                    },
    "back" : {"direction": 22,
                    "step": 1,
                    "other": (21,21,21)
                    },
    "front" : {"direction": 22,
                    "step": 1,
                    "other": (21,21,21)
                    }
}


motors = {
    "top" : mLib.A4988Nema(motors["left"]["directon"], motors["left"]["step"], (21, 21, 21), "A4988")
}

motors["top"].motor_go()