from projetin_xerox.programa.busca_elemento import retorna_text_indice_time, click_sem_indice
from selenium.webdriver.common.by import By

def maquina_C7030(driver):
    cilindros =[]
    toners = []
    preto = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=10, time=3)
    if preto == 'Elemento não encontrado':
         preto = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=10, time=3)
    toners.append(preto)
    amarelo = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-3)
    toners.append(amarelo)
    magenta = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-5)
    toners.append(magenta)
    ciano = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'webui-home-media-text'), indice=-7)
    toners.append(ciano)
    click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
    cilindro1 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=5, time=8)
    cilindros.append(cilindro1)
    cilindro2 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=6)
    cilindros.append(cilindro2)
    cilindro3 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=7)
    cilindros.append(cilindro3)
    cilindro4 = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=8)
    cilindros.append(cilindro4)
    fusor = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=10)
    return [toners, cilindros, fusor]