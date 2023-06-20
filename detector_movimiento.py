import cv2
import imutils
import winsound
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_alarma = os.path.join(ruta_actual, 'alarma1.wav')

cap = cv2.VideoCapture(0)

# Parámetros de grabación de video
recording = cv2.VideoWriter(
    "video.avi", cv2.VideoWriter_fourcc(*"XVID"), 10, (640, 480))

# Parámetros de configuración del servidor de correo electrónico
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_from = 'pgmar.257@gmail.com'
email_to = 'paula.gm@hotmail.es'
email_subject = 'Alerta de movimiento detectado'

# Configuración de las credenciales de autenticación del servidor de correo
smtp_username = 'pgmar.257@gmail.com'
smtp_password = 'zuxyrqiijmlzkceg'

while True:
    _, cam = cap.read()
    _, cam2 = cap.read()
    diff = cv2.absdiff(cam, cam2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(cam, (x, y), (x+w, y+h), (0, 0, 255), 2)
        winsound.PlaySound(ruta_alarma, winsound.SND_ASYNC)

    # Grabar video
    recording.write(cam)

    if cv2.waitKey(10) == ord("s"):
        break

    cv2.imshow("Detector de movimiento", cam)

# Liberar recursos y cerrar ventanas
cap.release()
recording.release()
cv2.destroyAllWindows()

# Enviar correo electrónico con el video adjunto
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = email_subject

video_part = MIMEBase('application', 'octet-stream')
video_part.set_payload(open('video.avi', 'rb').read())
encoders.encode_base64(video_part)
video_part.add_header('Content-Disposition', 'attachment', filename='video.avi')
msg.attach(video_part)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_from, email_to, msg.as_string())
