import cv2

def drawCircles(frame, positions):
    """
    Draws cicrles in places where colours are measured
    """

    # Draws Circles
    for square in positions:
        cv2.circle(frame, (square[0],square[1]), 5, (255,255,255), 1)

def drawText(frame, positions: list[tuple], colours):

    """
    Draws text for colours
    """

    for i in range(len(positions)):
        cv2.putText(frame, text=f'{colours[i]}', org=(positions[i][0]-20, positions[i][1]), 
        fontFace=cv2.FONT_HERSHEY_SIMPLEX, thickness=2, color=(255, 255, 255), fontScale=0.5)

def drawSampleSquare(frame, pos, size, colour):
    cv2.rectangle(frame, (pos[0],pos[1]),(pos[0]+size,pos[1]+size), colour, -1)

def drawSide(frame, colours, size, startPos):
    
    gapX = gapY = 3

    for y in range(0, 3):
        for x in range(0, 3):

            xPos = startPos[0] + x*size + x*gapX
            yPos = startPos[1] + y*size + y*gapY
        
            drawSampleSquare(frame, (xPos, yPos), size, colourToCode(colours[x][y]))

def drawUnfoldedCube(frame, colourMat, startPos = (15, 15), cubeSize = 15, gap = 5):
    
    drawSide(frame, startPos=(startPos[0] + 3*(cubeSize+gap), startPos[1]), size=cubeSize, colours=colourMat[0]) # Up
    drawSide(frame, startPos=(startPos[0] + 6*(cubeSize+gap), startPos[1] + 3*(cubeSize+gap)), size=cubeSize, colours=colourMat[1]) # Right
    drawSide(frame, startPos=(startPos[0] + 3*(cubeSize+gap), startPos[1] + 3*(cubeSize+gap)), size=cubeSize, colours=colourMat[2]) # Front
    drawSide(frame, startPos=(startPos[0] + 3*(cubeSize+gap), startPos[1] + 6*(cubeSize+gap)), size=cubeSize, colours=colourMat[3]) # Down
    drawSide(frame, startPos=(startPos[0], startPos[1] + 3*(cubeSize+gap)), size=cubeSize, colours=colourMat[4]) # Left
    drawSide(frame, startPos=(startPos[0] + 9*(cubeSize+gap), startPos[1] + 3*(cubeSize+gap)), size=cubeSize, colours=colourMat[5]) # Bottom


def colourToCode(colour):
        
    match colour:
        case "red": # red
            return (0, 0, 255)
        case "orange": # orange
            return (0, 123, 255)
        case "yellow": # yellow
            return (0, 255, 255)
        case "blue": # blue
            return (199, 13, 0)
        case "green": # green
            return (0, 255, 77)
        case "white": # white
            return (255, 255, 255)

    return (100, 100, 100)