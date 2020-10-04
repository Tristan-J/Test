import cv2
import numpy as np

v_old = "./xvideos.com_7121fe870a966f1a7029417c7b27f90b.mp4"
v_new = "./xvideos.com_7121fe870a966f1a7029417c7b27f90b.rotate.mp4"

reader = cv2.VideoCapture(v_old)

width = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
print(1)
writer = cv2.VideoWriter(v_new,
    fourcc,
    25,
    (height, width))
print(2)

status = True
c = 0
while status:
    status, frame = reader.read()
    frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.waitKey(1)
    c += 1
    if c%2500 == 0:
        print(c)

writer.release()
reader.release()
cv2.destroyAllWindows()