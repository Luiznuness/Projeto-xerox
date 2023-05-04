from selenium.webdriver.common.by import By
from projetin_xerox.programa.busca_elemento import click_sem_indice, retorna_elemento, click_indice, retorna_text
from time import sleep

def maquina_3320(driver):
    for c in range(0, 4):
        if c > 0:
            driver.refresh()
            sleep(5)
        ext_gen190 = retorna_elemento(driver, locator=(By.ID, 'ext-comp-1015'))
        click_sem_indice(ext_gen190, locator=(By.TAG_NAME, 'a'))
        click_indice(driver, locator=(By.CLASS_NAME, 'x-tree-node-anchor'), indice=2)
        toner = retorna_text(driver, locator=(By.CLASS_NAME, 'x-column'))
        if '%' in toner:
            toner = int(toner[85:87])
            cilindro = toner
            break
    return [toner, cilindro]    