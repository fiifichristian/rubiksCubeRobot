import cv2, sys, kociemba, argparse
import numpy as np
from random import seed, randint

sys.path.insert(1, 'helperCode/')
from colours import getColours, saveData2D, saveData3D
from guiDraw import drawCircles, drawText, drawUnfoldedCube
from matrices import posMat2D, posMat3D_0, posMat3D_1, colMattoStr, getMidColour, colourStrToKociString
from calibration import calibratePositions

class Cube():

    def __init__(self, array):
        self.rawData = array
        self._cubeString = colMattoStr(self.rawData)

    def __str__(self):
        return self._layout
    
    @property
    def cubeString(self):
        return self._cubeString.upper()

    def solve(self):

        if self.koci == "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB":
                instructions = "already solved"
                return instructions

        try:
            instructions = kociemba.solve(self.koci)
        except ValueError:
            print("invalid scramble, try again")
            instructions = None

        return instructions

    @property
    def koci(self):

        midColour = getMidColour(self._cubeString)
        kociStr = colourStrToKociString(self._cubeString, midColour)

        return kociStr

    @classmethod
    def scramble(cls, instrNum: int = 20):

        seed()

        faces = ('F', 'B', 'L', 'R', 'D', 'U')
        directions = ('', '\'', '2')

        inst = [f"{faces[randint(0, len(faces) - 1)]}{directions[randint(0, len(directions) - 1)]}",
        f"{faces[randint(0, len(faces) - 1)]}{directions[randint(0, len(directions) - 1)]}"]
        j = k = randint(0, len(faces) - 1)


        for i in range(instrNum):

            while faces[j] == inst[len(inst)-1][0] or faces[j] == inst[len(inst)-2][0]:
                j = randint(0, len(faces) - 1)

            k = randint(0, len(directions) - 1)
            inst.append(f"{faces[j]}{directions[k]}")

        scramString = " ".join(inst)

        return(scramString)

    @property
    def _layout(self):

        # Kociemba Algorithm
        #
        #  U1, U2, U3, U4, U5, U6, U7, U8, U9,
        #  R1, R2, R3, R4, R5, R6, R7, R8, R9,
        #  F1, F2, F3, F4, F5, F6, F7, F8, F9,
        #  D1, D2, D3, D4, D5, D6, D7, D8, D9,
        #  L1, L2, L3, L4, L5, L6, L7, L8, L9,
        #  B1, B2, B3, B4, B5, B6, B7, B8, B9
        cb = self.cubeString

        layout = (f"""
                     |*************|
                     |* {cb[0]} * {cb[1]} * {cb[2]} *|
                     |*************|
                     |* {cb[3]}** {cb[4]}** {cb[5]} *|
                     |*************|
                     |* {cb[6]}** {cb[7]}** {cb[8]} *|
                     |*************|
        *************|*************|*************|************
        * {cb[36]}** {cb[37]}** {cb[38]} *|* {cb[18]}** {cb[19]}** {cb[20]} *|* {cb[9]}** {cb[10]}** {cb[11]} *|* {cb[45]}** {cb[46]}** {cb[47]}*
        *************|*************|*************|************
        * {cb[39]}** {cb[40]}** {cb[41]} *|* {cb[21]}** {cb[22]}** {cb[23]} *|* {cb[12]}** {cb[13]}** {cb[14]} *|* {cb[48]}** {cb[49]}** {cb[50]}*
        *************|*************|*************|************
        * {cb[42]}** {cb[43]}** {cb[44]} *|* {cb[24]}** {cb[25]}** {cb[26]} *|* {cb[15]}** {cb[16]}** {cb[17]} *|* {cb[51]}** {cb[52]}** {cb[53]}*
        *************|*************|*************|************
                     |*************|
                     |* {cb[27]}** {cb[28]}** {cb[29]} *|
                     |*************|
                     |* {cb[30]}** {cb[31]}** {cb[32]} *|
                     |*************|
                     |* {cb[33]}** {cb[34]}** {cb[35]} *|
                     |*************|
        """)

        return layout.upper()

def camera():

    colours3D = [0 for i in range(2)]
    frame = [np.ndarray(shape=(0,0)) for i in range(2)]
    currentKey = 50

    # 0 = Up, 1 = Right, 2 = Front, 3 = Down, 4 = Left, 5 = Back
    cubeColoursCodes = [[[(0, 0, 0) for i in range(0,3)] for j in range(0, 3)] for k in range(0,6)]

    while True:

        _, frame[0] = cams[0].read()
        _, frame[1] = cams[1].read()

        try:
            hlsFrame = [cv2.cvtColor(frame[0], cv2.COLOR_BGR2HLS_FULL), cv2.cvtColor(frame[1], cv2.COLOR_BGR2HLS_FULL)]
        except Exception as e:
            if str(e).find("215") >= 0:
                print("Cameras not found. Are they connected properly?")
            exit()

        if threeDim:

            colours3D[0] = getColours(hlsFrame[0], posMat3D_0, True)
            drawCircles(frame[0], posMat3D_0)
            drawText(frame[0], posMat3D_0, colours3D[0])

            colours3D[1] = getColours(hlsFrame[1], posMat3D_1, True)
            drawCircles(frame[1], posMat3D_1)
            drawText(frame[1], posMat3D_1, colours3D[1])

        else:
            drawCircles(frame[0], posMat2D)
            colours2D = getColours(hlsFrame[0], posMat2D, True)
            drawText(frame[0], posMat2D, colours2D)

        drawUnfoldedCube(frame[0], cubeSize=15, gap=5, startPos= (15, 15), colourMat=cubeColoursCodes)
        drawUnfoldedCube(frame[1], cubeSize=15, gap=5, startPos= (15, 15), colourMat=cubeColoursCodes)

        key = cv2.waitKey(1)

        if key > 0:
            currentKey = key
        else:
            currentKey = 54

        if threeDim:
            cubeColoursCodes = saveData3D(0, colours3D[0], cubeColoursCodes)
            cubeColoursCodes = saveData3D(1, colours3D[1], cubeColoursCodes)
        elif key > 0 and chr(currentKey).isnumeric() and int(chr(currentKey)) < 7:
            cubeColoursCodes = saveData2D(int(chr(currentKey)) - 1, colours2D, cubeColoursCodes)

        if currentKey == ord('q'):
            break
        elif currentKey == ord('c'):
            cubeColoursCodes = [[[(0,0,0) for i in range(0,3)] for j in range(0, 3)] for k in range(0,6)]

        cv2.imshow("Up, Left, Front", frame[0])
        if threeDim:
            cv2.imshow("Bottom, Back, Right", frame[1])


    cv2.destroyAllWindows()
    return Cube(cubeColoursCodes)

def sysArg():

    parser = argparse.ArgumentParser(description="Rubik's Cube Solving Program by Group 5")
    options = parser.add_mutually_exclusive_group()
    options.add_argument("-s",  "--scramble", action="store_true", help="Gives a set of instructions for scrambling the cube")
    options.add_argument("-S", "--solve", action="store", help="Uses camera to help solve the cube. Use argument 0 for 2D scanning and 1 for 3D scanning")
    options.add_argument("-p", "--caliCoord", action="store_true", help="Uses camera to calibrate positions of the colours on the cube")
    options.add_argument("-c", "--caliColours", action="store_true", help="Uses camera to calibrate colours read")
    args = parser.parse_args()

    if args.scramble:
        print(Cube.scramble(25))
    elif args.caliCoord:
        calibratePositions(cams)
    elif args.caliColours:
        pass
    elif args.solve:

        global threeDim
        threeDim = True if args.solve == "1" else False

        rubikState = camera()
        inst = rubikState.solve()
        print(inst)

    else:
        print("\nNo arguments provided\n")
        parser.print_help()

def close():

    cv2.destroyAllWindows()

    for cam in cams:
        cam.release()

    quit()

cams = (cv2.VideoCapture(0, cv2.CAP_DSHOW), cv2.VideoCapture(1, cv2.CAP_DSHOW))

for cam in cams:
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_BRIGHTNESS, 0)

np.set_printoptions(threshold=sys.maxsize)
threeDim = True

if __name__ == "__main__":
    sysArg()
    close()