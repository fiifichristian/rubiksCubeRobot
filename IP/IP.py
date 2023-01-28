import cv2, sys, kociemba, argparse
import numpy as np
from random import seed, randint

from colours import getColours, saveData2D, saveData3D
from guiDraw import drawCircles, drawText, drawUnfoldedCube
from matrices import posMat2D, posMat3D_0, posMat3D_1, colMattoStr, getMidColour, colourStrToKociString
from calibration import calibratePositions

def camera():

    colours3D = frame = ["" for i in range(2)]
    currentKey = 50

    # 0 = Up, 1 = Right, 2 = Front, 3 = Down, 4 = Left, 5 = Back 
    cubeColoursCodes = [[[(0, 0, 0) for i in range(0,3)] for j in range(0, 3)] for k in range(0,6)]

    while True:

        _, frame[0] = cams[0].read()
        _, frame[1] = cams[1].read()

        hlsFrame = [cv2.cvtColor(frame[0], cv2.COLOR_BGR2HLS_FULL), cv2.cvtColor(frame[1], cv2.COLOR_BGR2HLS_FULL)]
        
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
    return cubeColoursCodes

def analysis(colourCodes: list):
    
    cubeString = colMattoStr(colourCodes)
    midColour = getMidColour(cubeString)
    kociStr = colourStrToKociString(cubeString, midColour)

    if kociStr == "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB":
        instructions = "already solved"
        return instructions, cubeString

    try:
        instructions = kociemba.solve(kociStr)
    except Exception:
        print("incorrect scanning, try again")
        instructions = None

    return instructions, cubeString

def scramble(instrNum: int = 20):

    seed()

    faces = ('F', 'B', 'L', 'R', 'D', 'U')
    directions = ('', '\'', '2')

    inst = ["F", "B"]
    j = k = randint(0, len(faces) - 1)

    for i in range(instrNum):
        
        while faces[j] == inst[len(inst)-1][0] and faces[j] == inst[len(inst)-2][0]:
            j = randint(0, len(faces) - 1)
        
        k = randint(0, len(directions) - 1)
        inst.append(f"{faces[j]}{directions[k]}")
    
    scramString = " ".join(inst)

    return(scramString)

def printLayout(cubeString: str):
    
    # Kociemba Algorithm
    # 
    #  U1, U2, U3, U4, U5, U6, U7, U8, U9, 
    #  R1, R2, R3, R4, R5, R6, R7, R8, R9, 
    #  F1, F2, F3, F4, F5, F6, F7, F8, F9, 
    #  D1, D2, D3, D4, D5, D6, D7, D8, D9, 
    #  L1, L2, L3, L4, L5, L6, L7, L8, L9,
    #  B1, B2, B3, B4, B5, B6, B7, B8, B9
    
    layout = (f"""
                |************|
                |* {cubeString[0]} * {cubeString[1]} * {cubeString[2]}*|
                |************|
                |* {cubeString[3]}** {cubeString[4]}** {cubeString[5]}*|
                |************|
                |* {cubeString[6]}** {cubeString[7]}** {cubeString[8]}*|
                |************|
    ************|************|************|************
    * {cubeString[36]}** {cubeString[37]}** {cubeString[38]}*|* {cubeString[18]}** {cubeString[19]}** {cubeString[20]}*|* {cubeString[9]}** {cubeString[10]}** {cubeString[11]}*|* {cubeString[45]}** {cubeString[46]}** {cubeString[47]}*
    ************|************|************|************
    * {cubeString[39]}** {cubeString[40]}** {cubeString[41]}*|* {cubeString[21]}** {cubeString[22]}** {cubeString[23]}*|* {cubeString[12]}** {cubeString[13]}** {cubeString[14]}*|* {cubeString[48]}** {cubeString[49]}** {cubeString[50]}*
    ************|************|************|************
    * {cubeString[42]}** {cubeString[43]}** {cubeString[44]}*|* {cubeString[24]}** {cubeString[25]}** {cubeString[26]}*|* {cubeString[15]}** {cubeString[16]}** {cubeString[17]}*|* {cubeString[51]}** {cubeString[52]}** {cubeString[53]}*
    ************|************|************|************
                |************|
                |* {cubeString[27]}** {cubeString[28]}** {cubeString[29]}*|
                |************|
                |* {cubeString[30]}** {cubeString[31]}** {cubeString[32]}*|
                |************|
                |* {cubeString[33]}** {cubeString[34]}** {cubeString[35]}*|
                |************|
    """)

    print(layout)

def sysArg():

    parser = argparse.ArgumentParser(description="Rubik's Cube Solving Program by Group 5")
    options = parser.add_mutually_exclusive_group()
    options.add_argument("-s",  "--scramble", action="store_true", help="Gives a set of instructions for scrambling the cube")
    options.add_argument("-S", "--solve", action="store", help="Uses camera to help solve the cube. Use argument 0 for 2D scanning and 1 for 3D scanning")
    options.add_argument("-p", "--caliCoord", action="store_true", help="Uses camera to calibrate positions of the colours on the cube")
    options.add_argument("-c", "--caliColours", action="store_true", help="Uses camera to calibrate colours read")
    args = parser.parse_args()

    if args.scramble:
        print(scramble(25)) 
    elif args.caliCoord:
        calibratePositions(cams)
    elif args.caliColours:
        pass
    elif args.solve:

        global threeDim
        threeDim = True if args.solve == "1" else False

        i = camera()
        inst, string = analysis(i)

        print(inst)
        # printLayout(string)
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
    cam.set(cv2.CAP_PROP_BRIGHTNESS, 0.1)

np.set_printoptions(threshold=sys.maxsize)
threeDim = False

sysArg()
close()


# a function called calibrate that allows an input o