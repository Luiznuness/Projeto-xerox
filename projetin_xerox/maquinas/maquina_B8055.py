from selenium.webdriver.common.by import By
from projetin_xerox.programa.busca_elemento import click_sem_indice, retorna_text_indice_time

def maquina_B8055(driver):
    click_sem_indice(driver, locator=(By.ID, 'details-button'))
    click_sem_indice(driver, locator=(By.ID, 'proceed-link'))
    click_sem_indice(driver, locator=(By.ID, 'section-header-3-btn'))
    toner =  retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'tableDiv'), indice=1).strip()
    cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'tableDiv'), indice=3).strip()
    fusor = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'tableDiv'), indice=5).strip()
    return [toner, cilindro, fusor]