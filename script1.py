import pyautogui
import pygetwindow as gw
import random
import time

# Función para simular un movimiento de ratón suave
def mover_raton_aleatorio():
    # Obtener el tamaño de la pantalla
    pantalla_ancho, pantalla_alto = pyautogui.size()

    # Generar coordenadas aleatorias dentro de los límites de la pantalla
    destino_x = random.randint(0, pantalla_ancho)
    destino_y = random.randint(0, pantalla_alto)

    # Mover el ratón de forma suave a esas coordenadas
    pyautogui.moveTo(destino_x, destino_y, duration=random.uniform(0.5, 1.5))  # Movimiento suave

# Función para realizar un clic simple en la posición actual del ratón
def hacer_click_simple():
    pyautogui.click()

# Función para realizar un doble clic en la posición actual del ratón
def hacer_doble_click():
    pyautogui.doubleClick()

# Función para detectar y cerrar el popup "Pafish RTT Window"
def cerrar_popup_pafish():
    # Buscar todas las ventanas abiertas
    ventanas_abiertas = gw.getWindowsWithTitle('')

    # Iterar sobre las ventanas abiertas
    for ventana in ventanas_abiertas:
        # Comprobar si el título de la ventana es "Pafish RTT Window"
        if 'Pafish RTT window' in ventana.title:
            try:
                ventana.close()  # Cerrar la ventana si es el popup de Pafish
                print("Popup 'Pafish RTT Window' cerrado.")
            except Exception as e:
                print(f"No se pudo cerrar la ventana {ventana.title}: {e}")

# Función para simular las acciones
def ejecutar_simulacion():
    while True:
        # Mover el ratón de manera aleatoria
        mover_raton_aleatorio()

        # Realizar un clic simple en la posición actual
        hacer_click_simple()

        # Esperar un momento antes de realizar el siguiente clic
        time.sleep(random.uniform(1, 1.5))

        # Realizar un doble clic en la posición actual
        hacer_doble_click()

        # Verificar y cerrar el popup "Pafish RTT Window"
        cerrar_popup_pafish()

        # Esperar un poco antes de hacer el siguiente movimiento
        time.sleep(random.uniform(2, 5))  # Intervalo de 2 a 5 segundos

# Iniciar la simulación
if __name__ == '__main__':
    ejecutar_simulacion()
