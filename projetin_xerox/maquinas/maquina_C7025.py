from projetin_xerox.programa.busca_elemento import click_sem_indice, escrever, retorna_text_indice_time
from os import getenv
from selenium.webdriver.common.by import By

def maquina_C7025(driver):
    cilindros = []
    toners = []
    click = click_sem_indice(driver, locator=(By.ID, 'globalnavButton'))
    if click == 'Elemento não encontrado':
        click_sem_indice(driver, locator=(By.ID, 'globalnavButton'))
    click_sem_indice(driver, locator=(By.ID, 'details-button'))
    click_sem_indice(driver, locator=(By.ID, 'proceed-link'))
    escrever(driver, locator=(By.ID, 'loginName'), texto=getenv('LOGIN'))
    escrever(driver, locator=(By.ID, 'loginPsw'), texto=getenv('SENHA'))
    click_sem_indice(driver, locator=(By.ID, 'loginButton'))
    ciano = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=4, time=11)
    if ciano == 'Elemento não encontrado':
        driver.refresh()
    ciano = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=4, time=8)
    if ciano == '':
        preto = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=12)
        amarelo = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=10)
        magenta = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=8)
        ciano = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=6)
    else:
        preto = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=10)
        amarelo = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=8)
        magenta = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=6)
    toners.append(preto)
    toners.append(amarelo)
    toners.append(magenta)
    toners.append(ciano)
    click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
    cilindro1 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=6, time=10)
    cilindro2 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=7)
    cilindro3 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=8)
    cilindro4 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=9)
    fusor = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=11)
    cilindros.append(cilindro1)
    cilindros.append(cilindro2)
    cilindros.append(cilindro3)
    cilindros.append(cilindro4)
    return [toners, cilindros, fusor]