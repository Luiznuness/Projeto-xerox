from selenium.webdriver.common.by import By
from projetin_xerox.programa.busca_elemento import retorna_elemento_indice, retorna_text_indice

def maquina_4620(driver):
    driver.refresh()
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=1)
    driver.switch_to.frame(freme)
    a = driver.find_elements(By.TAG_NAME,'a')
    for c in a:
        if c.text == 'Consumables':
            c.click()
            break
    driver.refresh()
    freme = retorna_elemento_indice(driver, (By.TAG_NAME,'frame'), indice=-1)
    driver.switch_to.frame(freme)
    toner = retorna_text_indice(driver, locator=(By.CLASS_NAME, 'centeredTextDescriptor'), indice=1)
    cilindro = retorna_text_indice(driver, locator=(By.CLASS_NAME, 'centeredTextDescriptor'), indice=3)
    return [toner, cilindro]