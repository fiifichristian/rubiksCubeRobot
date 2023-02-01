from colorsys import hls_to_rgb
import numpy as np

def getColours(frame, positions: list[tuple], colName=False):

    """
    Retreives the colours given the current frame (frame - must be in hls format not rgb) at the measurement points (positions) \n
    Returns the colour name ("red", "blue", "green" etc) if ColName is true, else returns colour code in hls format eg. (20,255,130)
    """

    colourData = []
    nameData = []

    for coord in positions:
        pixel = frame[coord[1]][coord[0]].tolist()
        colourData.append(pixel)

    if colName:
        for code in colourData:
            nameData.append(hlsToName(code))
        return nameData

    return colourData

def hlsToName(colour: tuple):

    """
    Converts hls (hue, lightness, saturation) color code to colour name on cube (only works on cube)
    Note: may need some minor adjustments

    REMEMBER:
    normally h is in range of 0 to 360\n
    normally l and s are in the range of 0 to 100% but cv2 scales it to 0 to 255
    """

    unitHls = (colour[0] / 360, colour[1] / 255, colour[2] / 255)
    rgb = hls_to_rgb(unitHls[0], unitHls[1], unitHls[2])

    lum = 0.2126*rgb[0] + 0.7152*rgb[1] + 0.0722*rgb[2]

    if (max(rgb) -  min(rgb)) < 0.21: # and : # white is different as you cant use hue
        return "white"
    if (colour[0] < 8 or colour[0] > 234):
        return "red"
    elif colour[0] < 42 and colour[1] > 100:
        return "orange"
    elif colour[0] < 75:
        return "yellow"
    elif colour[0] < 120:
        return "green"
    elif colour[0] < 191 or (rgb[2] > rgb[1] and rgb[2] > rgb[0]):
        return "blue"

    return "???"

def saveData2D(index, colours, cubeColours):

    x = y = i = 0
    # print(colours)
    # print(f"run with index {index}")

    for y in range(0, 3):
        for x in range(0, 3):

            cubeColours[index][x][y] = f"{colours[i]}"

            i = i + 1

    return cubeColours

def saveData3D(index, colours, cubeColours):

    x = y = i = 0
    # print(colours)
    # print(f"run with index {index}")

    save = [(4, 0, 2), (1, 5, 3)]

    for z in range(0,3):
        for y in range(0, 3):
            for x in range(0, 3):

                    cubeColours[save[index][z]][x][y] = f"{colours[i]}"

                    i = i + 1

    return cubeColours
