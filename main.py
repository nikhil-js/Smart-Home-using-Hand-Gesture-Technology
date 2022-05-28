import cv2
import mediapipe as mp
import time
import controller1 as cnt

time.sleep(2.0)
#importing mediapipe utilities
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
#assigning tip ids to fingers
tipIds = [4, 8, 12, 16, 20]
#calling webcam
video = cv2.VideoCapture(1)
#initializing input for hand tracking and number of hands to be tracked
with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5, max_num_hands=1) as hands:
    pTime = 0
    cTime = 0
    while True:
        success, image = video.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
#coverting images from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#creating an object list which will store the number of fingers
        obList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:

                for id, ob in enumerate(hand_landmark.landmark):
#defining the height, width and color for the image frame
                    h, w, c = image.shape



                    cx, cy = int(ob.x * w), int(ob.y * h)
                    obList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers = []
        if len(obList) != 0:
#condition to detect thumb
            if obList[tipIds[0]][1] > obList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
#conditiob to detect fingers
            for id in range(1, 5):
                if obList[tipIds[id]][2] < obList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = fingers.count(1)
#calling the controller for led input here
            cnt.led(total)
#Conditions for fingers
            if total == 0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "OFF ", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 5)
            elif total == 1:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 5)

            elif total == 2:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 5)

            elif total == 3:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 5)

            elif total == 4:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 5)

            elif total == 5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), 1)
                cv2.putText(image, "ON", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0 , 0), 5)



        cv2.imshow("Frame", image)
        interrupt = cv2.waitKey(10)
        if interrupt & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()