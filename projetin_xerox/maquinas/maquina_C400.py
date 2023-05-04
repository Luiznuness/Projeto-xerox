from projetin_xerox.programa.busca_elemento import click_sem_indice, escrever, retorna_text_indice_time
from os import getenv
from selenium.webdriver.common.by import By
from time import sleep

def maquina_C400(driver):
    toners = []
    for vezes in range(0, 3):
        if vezes > 0:
            driver.refresh()
            toners.clear()
        else:
            click_sem_indice(driver, locator=(By.ID, 'globalnavButton'))
            click_sem_indice(driver, locator=(By.ID, 'details-button'))
            click_sem_indice(driver, locator=(By.ID, 'proceed-link'))
            escrever(driver, locator=(By.ID, 'loginName'), texto=getenv('LOGIN'))
            escrever(driver, locator=(By.ID, 'loginPsw'), texto=getenv('SENHA'))
            if click_sem_indice(driver, locator=(By.ID, 'loginButton')) == 'Elemento não encontrado' or retorna_text_indice_time(driver,(By.CLASS_NAME, 'xux-labelableBox-content'), indice=2) == 'O nome de usuário ou a senha está incorreta.':
                    driver.refresh()
                    escrever(driver, locator=(By.ID, 'loginName'), texto=getenv('LOGIN'))
                    escrever(driver, locator=(By.ID, 'loginPsw'), texto=getenv('SENHA'))
            sleep(11)
            click_sem_indice(driver, locator=(By.ID, 'suppliesDetailButton'))
            preto = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=5, time=11)
            magenta = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=3)
            ciano = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=2)
            amarelo = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=4)
            toners.append(preto)
            toners.append(amarelo)
            toners.append(magenta)
            toners.append(ciano)
            cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=6)
            fusor = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=8)
            if '%' in cilindro:
                break
            else:
                cilindro = retorna_text_indice_time(driver, locator=(By.CLASS_NAME, 'xux-labelableBox-content'), indice=6)
                if '%' in cilindro:
                    break
    return [toners, cilindro, fusor] 