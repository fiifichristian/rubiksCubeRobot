import cv2
import guiDraw
import numpy as np

save = [(4, 0, 2), (1, 5, 3)]
posMat = [(0,0) for i in range(27)]

frame = 0
index = 0

def calibratePositions(cams: tuple):
    
    def savePos():
        pass

    def reset():
        pass

    global i, j, k

    cv2.namedWindow("Calibration")
    cv2.setMouseCallback("Calibration", setPosition)
    for cam in cams:

        posMat = [(0,0) for i in range(27)]
        
        for i in range(3):
            for j in range(3):
                for k in range(3):

                    colourRep = [[[(255, 255, 255) for i in range(0,3)] for j in range(0, 3)] for k in range(0,6)]
                    colourRep[save[cams.index(cam)][i]][k][j] = (27, 194, 163)
                    
                    while True:

                        _, frame = cam.read()

                        for circle in posMat:
                            if circle != (0, 0):
                                cv2.circle(frame, circle, 5, (255,255,255), 1)
                            else:
                                break
                        
                        colourRep[save[cams.index(cam)][i]][k][j] = (27, 194, 163)
                        guiDraw.drawUnfoldedCube(frame, cubeSize=15, gap=5, colourMat=colourRep)
                        
                        cv2.imshow("Calibration", frame)
                        key = cv2.waitKey(1)

                        if key == ord('q'):
                            exit()
                        elif key == -1:
                            continue
                        else:
                            break

        np.save(f"posMat{cams.index(cam)}.npy", np.array(posMat))


def setPosition(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        posMat[9*i + 3*j + k] = (x, y)
        print(posMat)
