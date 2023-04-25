#Importamos las librerias
import serial
arduino = serial.Serial('/dev/ttyACM0',9600) #Creación de objeto que establece la conexión con el puerto de Arduino
print (arduino.name) 
for i in range(7): #Bucle para la lectura de 7 líneas de datos
    x=arduino.readline().decode('utf-8').rstrip() 
    print(x)
arduino.close() #Cerramos la conexión con el Arduino