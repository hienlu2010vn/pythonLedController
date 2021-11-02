import cv2
import mediapipe as mp
import serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM1'
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
            if len(listTotalFinger) > 10:
                result = listTotalFinger.count(listTotalFinger[0]) == len(listTotalFinger)
                if result:
                    ser.open()
                    tmp = listTotalFinger[0]
                    if tmp == 5:
                        ser.write(1)
                        print("active")
                    if tmp == 0:
                        ser.write(0)
                        print("inactive")
                    ser.close()
                listTotalFinger.clear()

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
