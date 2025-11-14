import cv2
import mediapipe as mp
import numpy as np
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load drum sounds
kick = pygame.mixer.Sound("assets/sounds/kick.wav")
snare = pygame.mixer.Sound("assets/sounds/snare.wav")
hihat = pygame.mixer.Sound("assets/sounds/hihat.wav")
tom = pygame.mixer.Sound("assets/sounds/tom.wav")
crash = pygame.mixer.Sound("assets/sounds/crash.wav")

# Function to play sounds safely
def play_drum(gesture):
    if gesture == "☝ One Finger":
        kick.play()
    elif gesture == "✌ Two Fingers":
        snare.play()
    elif gesture == "🖐 Open Palm":
        crash.play()
    elif gesture == "✊ Fist":
        tom.play()
    elif gesture == "🖕 Middle Finger":
        hihat.play()

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

def get_gesture(landmarks):
    # Finger tip and base landmarks
    thumb_tip, thumb_base = landmarks[4][0], landmarks[2][0]
    index_tip, index_base = landmarks[8][1], landmarks[5][1]
    middle_tip, middle_base = landmarks[12][1], landmarks[9][1]
    ring_tip, ring_base = landmarks[16][1], landmarks[13][1]
    pinky_tip, pinky_base = landmarks[20][1], landmarks[17][1]

    # Detect which fingers are up
    fingers_up = [
        index_tip < index_base,   # Index finger
        middle_tip < middle_base, # Middle finger
        ring_tip < ring_base,     # Ring finger
        pinky_tip < pinky_base    # Pinky finger
    ]
    
    thumb_up = thumb_tip > thumb_base
    thumb_down = thumb_tip < thumb_base

    # Gesture Logic
    if all(fingers_up) and thumb_up:
        return "🖐 Open Palm"
    elif not any(fingers_up) and not thumb_up:
        return "✊ Fist"
    elif thumb_up and not any(fingers_up):
        return "👍 Thumbs Up"
    elif thumb_down and not any(fingers_up):
        return "👎 Thumbs Down"
    elif fingers_up[0] and not any(fingers_up[1:]):
        return "☝ One Finger"
    elif fingers_up[0] and fingers_up[1] and not any(fingers_up[2:]):
        return "✌ Two Fingers"
    elif fingers_up[1] and not any([fingers_up[0], fingers_up[2], fingers_up[3]]):
        return "🖕 Middle Finger"
    elif fingers_up[0] and not fingers_up[1] and not fingers_up[2] and fingers_up[3]:
        return "🤘 Rock"
    elif not fingers_up[0] and not fingers_up[1] and not fingers_up[2] and fingers_up[3] and thumb_up:
        return "🤙 Call Me"
    elif all(fingers_up) and not thumb_up:
        return "👋 Waving"
    elif fingers_up[0] and not any(fingers_up[1:]) and index_tip < index_base - 30:
        return "✍ Writing Motion"
    else:
        return "🤔 Unknown"

# Main loop
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_label in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_label.classification[0].label  # 'Left' or 'Right'
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = image.shape
            landmarks = np.array([[int(p.x * w), int(p.y * h)] for p in hand_landmarks.landmark])

            gesture = get_gesture(landmarks)

            # Play drum sound only when gesture is valid
            play_drum(gesture)

            # Display text
            if label == "Left":
                cv2.putText(image, f"Left: {gesture}", (10, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            else:
                cv2.putText(image, f"Right: {gesture}", (10, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

    cv2.imshow("Two-Hand Gesture Recognition with Drums", image)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
