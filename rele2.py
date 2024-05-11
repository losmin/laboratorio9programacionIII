import serial
import tkinter as tk

# Inicialización de la comunicación serial
arduino = serial.Serial('COM4', 9600, timeout=1)  # Cambia 'COM3' al puerto que estés utilizando

# Funciones para controlar los LEDs
def enviar_comando(comando):
    arduino.write(comando.encode())

def encender_led_verde():
    enviar_comando('1')

def encender_led_rojo():
    enviar_comando('0')

# Cerrar el puerto serial al cerrar la aplicación
def cerrar_serial():
    arduino.close()
    root.destroy()

# Creación de la interfaz gráfica
root = tk.Tk()
root.title("Control de LEDs y Relé")

# Botones para controlar los LEDs
btn_verde = tk.Button(root, text="Encender LED Verde", command=encender_led_verde)
btn_verde.pack(pady=10)
btn_rojo = tk.Button(root, text="Encender LED Rojo", command=encender_led_rojo)
btn_rojo.pack(pady=10)

# Botón para salir y cerrar el puerto serial
btn_cerrar = tk.Button(root, text="Cerrar", command=cerrar_serial)
btn_cerrar.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
