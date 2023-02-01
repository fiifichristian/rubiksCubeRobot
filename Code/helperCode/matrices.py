midX = 640 // 2
midY = 480 // 2

# 2D Settings
gapX = gapY = 75 # forms grid gaps between circles/measurement points

# 3D Settings
cubeGaps = [62, 90]
initGap = 40
startPos = [[midX-initGap, midY+100], [midX, midY-120], [midX+initGap, midY+100], [midX-initGap, midY-80], [midX+150, midY-20], [midX, midY+130]]
adjustment = 4
yGain = 30
topDiag0to8 = 140
topDiag2to6 = 50

# This labels the positions of the measurement points for the circles if you're just looking at one side of the cube (9 squares) - see images/numbering2D.png
posMat2D = [(midX-gapX,midY-gapY), (midX, midY-gapY), (midX+gapX, midY-gapY),
        (midX-gapX, midY), (midX, midY), (midX+gapX, midY),
        (midX-gapX,midY+gapY), (midX, midY+gapY), (midX+gapX, midY+gapY)]

posMat3D_0 = [

    # Side 0
    (startPos[0][0] - 2*cubeGaps[0], startPos[0][1] - cubeGaps[1] - 2*yGain + 2*adjustment), (startPos[0][0] - cubeGaps[0], startPos[0][1] - cubeGaps[1] - yGain + adjustment), (startPos[0][0], startPos[0][1] - cubeGaps[1]), #
    (startPos[0][0] - 2*cubeGaps[0], startPos[0][1] - 2*yGain), (startPos[0][0] - cubeGaps[0], startPos[0][1] - yGain), (startPos[0][0], startPos[0][1]), # Side 0
    (startPos[0][0] - 2*cubeGaps[0], startPos[0][1] + cubeGaps[1] - 2*yGain - 2*adjustment), (startPos[0][0] - cubeGaps[0], startPos[0][1] + cubeGaps[1] - yGain - adjustment), (startPos[0][0], startPos[0][1] + cubeGaps[1]), #

    # Side 1
    (startPos[1][0] - topDiag0to8, startPos[1][1]), (startPos[1][0] - round(0.5*topDiag0to8), startPos[1][1] - round(0.5*topDiag2to6)), (startPos[1][0], startPos[1][1] - topDiag2to6), #
    (startPos[1][0] - round(0.5*topDiag0to8), startPos[1][1] + round(0.5*topDiag2to6)), (startPos[1][0], startPos[1][1]), (startPos[1][0] + round(0.5*topDiag0to8), startPos[1][1] - round(0.5*topDiag2to6)) , # Side 1
    (startPos[1][0], startPos[1][1] + topDiag2to6), (startPos[1][0] + round(0.5*topDiag0to8), startPos[1][1] + round(0.5*topDiag2to6)), (startPos[1][0] + topDiag0to8, startPos[1][1]), #

    # Side 2
    (startPos[2][0], startPos[2][1] - cubeGaps[1]), (startPos[2][0] + cubeGaps[0], startPos[2][1] - cubeGaps[1] - yGain), (startPos[2][0] + 2*cubeGaps[0] + 10, startPos[2][1] - cubeGaps[1] - 2*yGain),
    (startPos[2][0], startPos[2][1]), (startPos[2][0] + cubeGaps[0], startPos[2][1] - yGain), (startPos[2][0] + 2*cubeGaps[0], startPos[2][1] - 2*yGain) , # Side 0
    (startPos[2][0], startPos[2][1] + cubeGaps[1]), (startPos[2][0] + cubeGaps[0], startPos[2][1] + cubeGaps[1] - yGain), (startPos[2][0] + 2*cubeGaps[0] - 10, startPos[2][1] + cubeGaps[1] - 2*yGain)

]

posMat3D_1 = [

    # Side 3
    (startPos[3][0], startPos[3][1] - cubeGaps[1]), (startPos[3][0] - cubeGaps[0], startPos[3][1] - cubeGaps[1] + yGain), (startPos[3][0] - 2*cubeGaps[0] + 10, startPos[3][1] - cubeGaps[1] + 2*yGain),
    (startPos[3][0], startPos[3][1]), (startPos[3][0] - cubeGaps[0], startPos[3][1] + yGain), (startPos[3][0] - 2*cubeGaps[0], startPos[3][1] + 2*yGain) , # Side 0
    (startPos[3][0], startPos[3][1] + cubeGaps[1]), (startPos[3][0] - cubeGaps[0], startPos[3][1] + cubeGaps[1] + yGain), (startPos[3][0] - 2*cubeGaps[0] - 10, startPos[3][1] + cubeGaps[1] + 2*yGain),

    # Side 5
    (startPos[4][0] - 2*cubeGaps[0], startPos[4][1] - cubeGaps[1] - 2*yGain + 2*adjustment), (startPos[4][0] - cubeGaps[0], startPos[4][1] - cubeGaps[1] - yGain + adjustment), (startPos[4][0], startPos[4][1] - cubeGaps[1]), #
    (startPos[4][0] - 2*cubeGaps[0], startPos[4][1] - 2*yGain), (startPos[4][0] - cubeGaps[0], startPos[4][1] - yGain), (startPos[4][0], startPos[4][1]), # Side 0
    (startPos[4][0] - 2*cubeGaps[0], startPos[4][1] + cubeGaps[1] - 2*yGain - 2*adjustment), (startPos[4][0] - cubeGaps[0], startPos[4][1] + cubeGaps[1] - yGain - adjustment), (startPos[4][0], startPos[4][1] + cubeGaps[1]), #

    (startPos[5][0], startPos[5][1] + topDiag2to6), (startPos[5][0] - round(0.5*topDiag0to8), startPos[5][1] + round(0.5*topDiag2to6)), (startPos[5][0] - topDiag0to8, startPos[5][1]),
    (startPos[5][0] + round(0.5*topDiag0to8), startPos[5][1] + round(0.5*topDiag2to6)), (startPos[5][0], startPos[5][1]), (startPos[5][0] - round(0.5*topDiag0to8), startPos[5][1] - round(0.5*topDiag2to6)),
    (startPos[5][0] + topDiag0to8, startPos[5][1]), (startPos[5][0] + round(0.5*topDiag0to8), startPos[5][1] - round(0.5*topDiag2to6)), (startPos[5][0], startPos[5][1] - topDiag2to6)
]

def colMattoStr(cubeColours):
    result = ""

    for i in range(len(cubeColours)):
            for j in range(len(cubeColours[i])):
                for k in range(len(cubeColours[i][j])):

                    result = f"{result}{cubeColours[i][k][j][0]}"

    return result

# def midColToName(array):

#     result = []

#     for col in array:
#         if col == (0, 0, 255): # red
#             result.append("R")
#         elif col == (0, 123, 255): # orange
#             result.append("O")
#         elif col == (0, 255, 255): # yellow
#             result.append("Y")
#         elif col == (199, 13, 0): # blue
#             result.append("B")
#         elif col == (0, 255, 77): # green
#             result.append("G")
#         elif col == (255, 255, 255): # white
#             result.append("W")
#         else:
#             result.append("N")

#     return result

def getMidColour(string):

    midColour = [(0, 0, 0) for i in range(6)]
    for i in range(len(midColour)):
        midColour[i] = string[4 + i*9]

    return midColour

def colourStrToKociString(string, centers):

    newStr = string
    mid = [("U", centers[0]), ("R", centers[1]), ("F", centers[2]), ("D", centers[3]), ("L", centers[4]), ("B", centers[5])]

    for i in range(len(mid)):
        newStr = newStr.replace(mid[i][1], mid[i][0])

    return newStr

