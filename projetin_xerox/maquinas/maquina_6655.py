from selenium.webdriver.common.by import By
from projetin_xerox.programa.busca_elemento import click_sem_indice, retorna_elemento, retorna_elemento_indice, retornar_elemento_completo

def maquina_6655(driver):
    toner = []
    click_sem_indice(driver,locator=(By.ID, 'details-button'))
    click_sem_indice(driver,locator=(By.ID, 'proceed-link'))
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
    driver.switch_to.frame(freme)
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=0)
    driver.switch_to.frame(freme)
    click_sem_indice(driver,locator=(By.ID, 'n5'))
    driver.refresh()
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
    driver.switch_to.frame(freme)
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
    driver.switch_to.frame(freme)
    tbody = retorna_elemento(driver, (By.TAG_NAME, 'tbody'))
    trs = retornar_elemento_completo(tbody, (By.TAG_NAME, 'tr'))
    # TONER PRETO
    tr_preto = trs[1]
    class_preto = retorna_elemento(tr_preto, (By.CLASS_NAME, 'horizTherm'))
    preto = retorna_elemento(class_preto, (By.TAG_NAME, 'img'))
    preto = preto.get_attribute('title')
    toner.append(preto)
    #TONER CIANO
    tr_ciano = trs[2]
    class_ciano = retorna_elemento(tr_ciano, (By.CLASS_NAME, 'horizTherm'))
    ciano = retorna_elemento(class_ciano, (By.TAG_NAME, 'img'))
    ciano = ciano.get_attribute('title')
    toner.append(ciano)
    #TONER MAGENTA
    tr_magenta = trs[3]
    class_magenta = retorna_elemento(tr_magenta, (By.CLASS_NAME, 'horizTherm'))
    magenta = retorna_elemento(class_magenta, (By.TAG_NAME, 'img'))
    magenta = magenta.get_attribute('title')
    toner.append(magenta)
    #TONER AMARELO
    tr_amarelo = trs[4]
    class_amarelo = retorna_elemento(tr_amarelo, (By.CLASS_NAME, 'horizTherm'))
    amarelo = retorna_elemento(class_amarelo, (By.TAG_NAME, 'img'))
    amarelo = amarelo.get_attribute('title')
    toner.append(amarelo)
    # CILINDRO
    cilindro = retorna_elemento_indice(driver, (By.CLASS_NAME, 'horizTherm'), indice=4)
    cilindro = retorna_elemento(cilindro, (By.TAG_NAME, 'img'))
    cilindro = cilindro.get_attribute('title')
    # Fusor
    fusor = retorna_elemento_indice(driver, (By.CLASS_NAME, 'horizTherm'), indice=5 )
    fusor = retorna_elemento(fusor, (By.TAG_NAME, 'img'))
    fusor = fusor.get_attribute('title')
    return [toner, cilindro, fusor]