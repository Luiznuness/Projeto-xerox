from projetin_xerox.maquinas.maquina_3320 import maquina_3320
from projetin_xerox.maquinas.maquina_3655 import maquina_3655
from projetin_xerox.maquinas.maquina_4620 import maquina_4620
from projetin_xerox.maquinas.maquina_B405 import maquina_B405
from projetin_xerox.maquinas.maquina_C400 import maquina_C400
from projetin_xerox.maquinas.maquina_C405 import maquina_C405
from projetin_xerox.maquinas.maquina_C7025 import maquina_C7025
from projetin_xerox.maquinas.maquiba_C7030 import maquina_C7030
from projetin_xerox.maquinas.maquina_6655 import maquina_6655
from projetin_xerox.maquinas.maquina_B8055 import maquina_B8055
from projetin_xerox.datafreme.atualizar_datafreme import select_atualizar_planilhas
from projetin_xerox.datafreme.verificar_datafreme import verificar_datafreme
from selenium.webdriver.support.event_firing_webdriver import WebDriverException
import pandas as pd


def buscar(caminho_planilha , driver):
    dados_datafreme = []
    information = pd.read_excel(caminho_planilha)
    verificar_datafreme(information)
    for c in range(0, len(information)):
        indice = information.loc[c]
        ip = indice['Ip']
        modelo = indice['Modelos']
        retorno = acesso(driver, ip, modelo)
        dados_datafreme.append(retorno)
    select_atualizar_planilhas(dados_datafreme, information)

def acesso(driver, ip, modelo):
    try:
        url = 'http://' + ip
        driver.get(url)
        result = verificar(driver, modelo)
        return result
    except WebDriverException:
        return ['Inacessível', 'Inacessível', 'Inacessível']


def verificar(driver, modelo):
    if modelo == 3320:
        ver_resutado = maquina_3320(driver)
    elif modelo == 3655:
        ver_resutado = maquina_3655(driver)
    elif  modelo == 4620:
        ver_resutado = maquina_4620(driver)
    elif modelo == 6655:
        ver_resutado = maquina_6655(driver)
    elif modelo == 'B405':
        ver_resutado = maquina_B405(driver)
    elif modelo == 'C400':
        ver_resutado = maquina_C400(driver)
    elif modelo == 'C405':
        ver_resutado = maquina_C405(driver)
    elif modelo == 'C7025':
        ver_resutado = maquina_C7025(driver)
    elif modelo == 'C7030':
        ver_resutado = maquina_C7030(driver)
    elif modelo == 'B8055':
        ver_resutado = maquina_B8055(driver)
    else:
        ver_resutado = 'Função em andamento'
    return ver_resutado