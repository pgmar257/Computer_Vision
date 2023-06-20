# Alarma detección de movimiento [![Made With Python](https://img.shields.io/badge/Made_With-Python-blue)](http://golang.org)
![](img/opencv.png)

Este proyecto utiliza una cámara (webcam o raspicam) para detectar movimiento en una zona de la pantalla específica. La detección de movimiento se realiza siguiendo las siguientes instrucciones:


## Descripción
El objetivo de este proyecto es utilizar una cámara para detectar movimiento en una zona específica de la pantalla. Esto puede ser útil en aplicaciones de seguridad, monitoreo de espacios o cualquier situación donde se requiera detectar actividad en una región determinada.

El proyecto está desarrollado en Python y hace uso de las siguientes bibliotecas:

- OpenCV: Se utiliza para el procesamiento de imágenes y la detección de movimiento en tiempo real.
- smtplib: Se utiliza para el envío de correos electrónicos con el video que muestra el movimiento detectado.
- winsound: Se utiliza para generar una alarma sonora cuando se detecta movimiento.

