from selenium.webdriver import Chrome
from projetin_xerox.programa.selecionar import buscar
from os import getenv

def abrir_driver():
    driver = Chrome()
    driver.maximize_window()
    information = getenv("PLANILHA_FILA_DE_IMPRESSAO")
    buscar(information, driver)
    driver.close()