from selenium.webdriver.common.by import By
from projetin_xerox.programa.busca_elemento import click_sem_indice, retorna_elemento, retorna_elemento_indice, retorna_text_indice
from time import sleep

def maquina_3655(driver):
    toner = ''
    for c in range(0, 3):
        click_sem_indice(driver,locator=(By.ID, 'details-button'))
        click_sem_indice(driver,locator=(By.ID, 'proceed-link'))
        sleep(2)
        freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
        driver.switch_to.frame(freme)
        freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=0)
        driver.switch_to.frame(freme)
        if driver.find_element(By.ID, 'n6').text == 'Suprimentos':
            click_sem_indice(driver, locator=(By.ID, 'n6'))
        else:
            click_sem_indice(driver, locator=(By.ID, 'n5'))
        sleep(2)
        driver.refresh()
        sleep(2)
        freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
        driver.switch_to.frame(freme)
        freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
        driver.switch_to.frame(freme)
        classe = retorna_elemento(driver, locator=(By.CLASS_NAME, 'horizTherm'))
        toner = retorna_elemento(classe, locator=(By.TAG_NAME, 'img'))
        toner = toner.get_attribute('title')
        cilindro = retorna_text_indice(driver, (By.CLASS_NAME,'tableDiv'), indice=5).strip()
        fusor = retorna_text_indice(driver, (By.CLASS_NAME,'tableDiv'), indice=3).strip()
        if toner != '':
            break
    return [toner, cilindro, fusor]