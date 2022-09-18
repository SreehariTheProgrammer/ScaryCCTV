import cv2
import winsound
import pyautogui
import random

pyautogui.FAILSAFE = False

cam = cv2.VideoCapture(0)
while cam.isOpened():
    for i in range(2):
        pyautogui.moveTo(0, i * 7)
        pyautogui.press("shift")

    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)

        rn = random.randrange(1, 10009089267283272743)

        ss = pyautogui.screenshot()
        ss.save(f"img{rn}.png")
        
    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow('Frame', frame1)