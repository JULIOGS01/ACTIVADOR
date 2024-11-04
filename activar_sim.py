from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializar el navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navegar a la página de activación
    driver.get("https://recargamigoweb.telcel.com/distributor/login")

    # Ingresar el número de agente
    campo_agente = driver.find_element(By.ID, "msisdn")
    campo_agente.send_keys("7713033759")

    # Ingresar el usuario
    campo_usuario = driver.find_element(By.ID, "username")
    campo_usuario.send_keys("RAM-09I00919699")

    # Ingresar el NIP
    campo_nip = driver.find_element(By.ID, "password")
    campo_nip.send_keys("1111")

    # Hacer clic en el botón de ingresar (enviando el formulario directamente)
    driver.execute_script("$('#loginForm').submit(); executeLoader();")

    # Esperar unos segundos para la llegada del token
    time.sleep(5)

    # Solicitar el token al usuario (manualmente)
    token = input("Ingresa el token que recibiste en tu teléfono: ")

    # Ingresar el token
    campo_token = driver.find_element(By.NAME, "token")
    campo_token.send_keys(token)

    # Hacer clic en el botón de enviar token (enviando el formulario directamente)
    driver.execute_script("$('#tokenForm').submit(); executeLoader();")

    # Esperar para permitir que la página cargue
    time.sleep(5)

    # Aquí podrías agregar pasos adicionales para automatizar la activación de la SIM si es necesario

finally:
    # Esperar y cerrar el navegador
    time.sleep(5)
    driver.quit()
