from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator
    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False
def click_sem_indice(driver, locator):
    try:
        wdw = WebDriverWait(driver, 5)
        wdw.until(EsperarElemento(locator=(locator)))
        driver.find_element(*locator).click()
    except:
        return 'Elemento não encontrado'
def click_indice(driver, locator, indice):
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        driver.find_elements(*locator)[indice].click()
    except:
        return 'Elemento não encontrado'
def click_indice_time(driver, locator, indice, time=0):
    sleep(time)
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        driver.find_elements(*locator)[indice].click()
    except:
        return 'Elemento não encontrado'    

def retorna_elemento(driver, locator):
    try:
        wdw = WebDriverWait(driver, 5)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_element(*locator)
    except:
        return 'Elemento não encontrado'
def retornar_elemento_completo(driver, locator):
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_elements(*locator)
    except:
        return 'Elemento não encontrado'
def retorna_elemento_indice(driver, locator, indice):
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_elements(*locator)[indice]
    except:
        return 'Elemento não encontrado'

def retorna_text(driver, locator):
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_element(*locator).text
    except:
        return 'Elemento não encontrado'
def retorna_text_indice(driver, locator, indice):
    sleep(5)
    try:
        wdw = WebDriverWait(driver, 2)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_elements(*locator)[indice].text
    except:
        return 'Elemento não encontrado'

def retorna_text_indice_time(driver, locator, indice, time=0):
    sleep(time)
    try:
        wdw = WebDriverWait(driver, 5)
        wdw.until(EsperarElemento(locator=(locator)))
        return driver.find_elements(*locator)[indice].text
    except:
        return 'Elemento não encontrado'
def escrever(driver, locator, texto):
    try:
        wdw = WebDriverWait(driver, 5)
        wdw.until(EsperarElemento(locator=(locator)))
        driver.find_element(*locator).send_keys(texto)
    except:
        return 'Elemento não encontrado'