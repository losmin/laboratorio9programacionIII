import serial
import time
import tkinter as tk

# Configuración del puerto serial, cambia 'COM3' al puerto que estés utilizando
arduino = serial.Serial('COM4', 9600, timeout=1)

def encender_led_verde():
    arduino.write(b'1')

def encender_led_rojo():
    arduino.write(b'0')

def apagar_leds():
    arduino.write(b'0')

def cerrar_serial():
    arduino.close()

# Función para encender el LED verde y activar el relé
def activar():
    encender_led_verde()

# Función para encender el LED rojo y desactivar el relé
def desactivar():
    encender_led_rojo()

# Creación de la interfaz gráfica
root = tk.Tk()
root.title("Control de LEDs y Relé")

# Botones para activar y desactivar
btn_activar = tk.Button(root, text="Activar", command=activar)
btn_activar.pack(pady=10)
btn_desactivar = tk.Button(root, text="Desactivar", command=desactivar)
btn_desactivar.pack(pady=10)

# Botón para cerrar el puerto serial y salir
btn_cerrar = tk.Button(root, text="Cerrar", command=cerrar_serial)
btn_cerrar.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()