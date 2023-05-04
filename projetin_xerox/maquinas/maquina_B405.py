from projetin_xerox.programa.busca_elemento import click_sem_indice, escrever, retorna_text_indice, retorna_text_indice_time
from selenium.webdriver.common.by import By
from os import getenv
from time import sleep

def maquina_B405(driver):
    toner =  retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-1, time=3)
    if '%' in toner:
        click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
        fusor = retorna_text_indice(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=3)
        cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=2)
        if cilindro == toner:
            cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=3)
            fusor = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=4)
        return [toner, cilindro, fusor]
    click_sem_indice(driver, locator=(By.ID, 'globalnavButton'))
    click_sem_indice(driver, locator=(By.ID, 'details-button'))
    click_sem_indice(driver, locator=(By.ID, 'proceed-link'))
    escrever(driver, locator=(By.ID, 'loginName'), texto=getenv('LOGIN'))
    escrever(driver, locator=(By.ID, 'loginPsw'), texto=getenv('SENHA'))
    click_sem_indice(driver, locator=(By.ID, 'loginButton'))
    sleep(5)
    toner =  retorna_text_indice(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-1)
    click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
    sleep(4)
    fusor = retorna_text_indice(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=4)
    cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=3)
    if toner == 'Elemento não encontrado':
        driver.refresh()
        sleep(5)
        toner =  retorna_text_indice(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-1)
        click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
        sleep(3)
        fusor = retorna_text_indice(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=4)
        cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=3)
    return [toner, cilindro, fusor]