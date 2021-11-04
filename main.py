import cv2
import mediapipe as mp
import serial
import time



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def findPosition(img, handNo=0):
    lmList = []
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]

        for id, lm in enumerate(myHand.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
    return lmList

tmpstore = 0
# For webcam input:
listTotalFinger = []
tipIds = [4, 8, 12, 16, 20]
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        lmList = findPosition(image)

        if len(lmList) != 0:
            fingers = []
            if (lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[1][1] < lmList[17][1]) or (
                    lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[1][1] > lmList[17][1]):
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):  # y axis
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)
            listTotalFinger.append(totalFingers)
            if len(listTotalFinger) > 20:
                result = listTotalFinger.count(listTotalFinger[0]) == len(listTotalFinger)
                if result:
                    serialcomm = serial.Serial('COM1', 9600)
                    serialcomm.timeout = 1
                    tmp = listTotalFinger[0]
                    if tmp == 5 and tmpstore != 5:
                        tmpstore = 5
                        i = 'on'
                        serialcomm.write(i.encode())
                        print("active")
                        time.sleep(0.5)
                        print(serialcomm.readline().decode('ascii'))

                    if tmp == 0 and tmpstore != 0:
                        tmpstore = 0
                        i = 'off'
                        serialcomm.write(i.encode())
                        print("inactive")
                        time.sleep(0.5)
                        print(serialcomm.readline().decode('ascii'))

                    serialcomm.close()
                listTotalFinger.clear()

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
