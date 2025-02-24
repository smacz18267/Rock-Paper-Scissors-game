import random
import cv2
import cvzone
import os
from cvzone.HandTrackingModule import HandDetector
import time

background_path = "Images/Background.png"
imgBG_original = cv2.imread(background_path)

ai_image_paths = {i: f"Images/{i}.png" for i in range(1, 4)}

# Initialize Camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]
imgAI = None  # Global AI move image

while True:
    # Make a fresh copy of the background for this frame.
    imgBG = imgBG_original.copy()

    success, img = cap.read()
    if not success or img is None:
        continue  # Skip frame if capture fails

    imgScaled = cv2.resize(img, (400, 420))  # Resize to match background crop

    # Find Hands on the scaled image
    hands, _ = detector.findHands(imgScaled)

    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435),
                        cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    if fingers == [0, 0, 0, 0, 0] or fingers == [1, 0, 0, 0, 0]:
                        playerMove = 1
                    elif fingers == [1, 1, 1, 1, 1] or fingers == [0, 1, 1, 1, 1]:
                        playerMove = 2
                    elif fingers == [0, 1, 1, 0, 0] or fingers == [1, 1, 1, 0, 0]:
                        playerMove = 3

                    if playerMove:
                        randomNumber = random.randint(1, 3)  # AI selects move
                        ai_image_path = ai_image_paths[randomNumber]

                        imgAI = cv2.imread(ai_image_path, cv2.IMREAD_UNCHANGED)

                        # Score Calculation
                        if (playerMove == 1 and randomNumber == 3) or \
                           (playerMove == 2 and randomNumber == 1) or \
                           (playerMove == 3 and randomNumber == 2):
                            scores[1] += 1  # Player Wins
                        elif (playerMove == 3 and randomNumber == 1) or \
                             (playerMove == 1 and randomNumber == 2) or \
                             (playerMove == 2 and randomNumber == 3):
                            scores[0] += 1  # AI Wins

    # Overlay the webcam feed on a specific region of the background
    imgBG[234:654, 795:1195] = imgScaled

    # Overlay AI move if available
    if stateResult:
        if imgAI is not None:
            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    # Display Scores
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("Background", imgBG)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
