import cv2
import mediapipe as mp
from keras.models import load_model
import numpy as np

# TensorFlow versão 2.9.1

# Abra o vídeo
video_path = 'V.mp4'  # Substitua pelo caminho do seu vídeo
cap = cv2.VideoCapture(video_path)

# Inicialize o módulo Hands do MediaPipe
hands = mp.solutions.hands.Hands(max_num_hands=1)

# Carregue o modelo do Keras
classes = ['A', 'B', 'C', 'D']
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Obtenha informações do vídeo de entrada
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = int(cap.get(5))

# Defina o codec e o objeto VideoWriter para salvar o vídeo de saída
output_video_path = '/content/drive/My Drive/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use o codec 'XVID'
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = frame.shape

    if handsPoints is not None:
        for hand in handsPoints:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in hand.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            cv2.rectangle(frame, (x_min - 50, y_min - 50), (x_max + 50, y_max + 50), (0, 255, 0), 2)

            try:
                imgCrop = frame[y_min - 50:y_max + 50, x_min - 50:x_max + 50]
                imgCrop = cv2.resize(imgCrop, (224, 224))
                imgArray = np.asarray(imgCrop)
                normalized_image_array = (imgArray.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)
                indexVal = np.argmax(prediction)
                label = classes[indexVal]

                cv2.putText(frame, label, (x_min - 50, y_min - 65), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5)

            except:
                continue

    out.write(frame)  # Escreva o quadro com os rótulos no vídeo de saída

cap.release()
out.release()
cv2.destroyAllWindows()
