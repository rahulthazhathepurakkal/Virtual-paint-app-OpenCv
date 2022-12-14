
import cv2
import numpy as np
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
myPoints=[]
def fn(x):
    pass
cv2.namedWindow("Tracking Window")
cv2.createTrackbar("LH","Tracking Window",0,179,fn)
cv2.createTrackbar("LS","Tracking Window",0,100,fn)
cv2.createTrackbar("LV","Tracking Window",0,100,fn)
cv2.createTrackbar("UH","Tracking Window",0,179,fn)
cv2.createTrackbar("US","Tracking Window",0,255,fn)
cv2.createTrackbar("UV","Tracking Window",0,255,fn)
while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame2=frame.copy()
    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LH", "Tracking Window")
    l_s = cv2.getTrackbarPos("LS", "Tracking Window")
    l_v = cv2.getTrackbarPos("LV", "Tracking Window")
    u_h = cv2.getTrackbarPos("UH", "Tracking Window")
    u_s = cv2.getTrackbarPos("US", "Tracking Window")
    u_v = cv2.getTrackbarPos("UV", "Tracking Window")
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsvframe, lower, upper)
    cv2.imshow("mask", mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.circle(frame2, (x, y), 5,(0,255,0), -1)
            myPoints.append([x, y])
    for point in myPoints:
        cv2.circle(frame, (point[0], point[1]), 5, (0, 255, 0), -1)
    cv2.imshow("Output", frame2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()