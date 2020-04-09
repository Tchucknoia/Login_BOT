import platform
import os

def pegar_diretorio():
    diretorio = os.path.dirname(os.path.realpath(__file__)) + '/WebDrivers'
    if platform.system() == 'Linux':
        diretorio = diretorio + '/chromedriver'
    elif platform.system() == 'Windows':
        diretorio = diretorio + '/chromedriver'
    return diretorio

if __name__ == '__main__':
    from selenium import webdriver
    diretorio_WebDriver = pegar_diretorio()

    #username = input('Digite seu email:')
    #password = input('Digite sua senha:')

    from ler_txt import ler_txt
    dados = ler_txt('nome_senha.txt')
    driver = webdriver.Chrome(diretorio_WebDriver)
    driver.get('http://www.facebook.com.br')

    username_textbox = driver.find_element_by_id('email')
    username_textbox.send_keys(dados.get('email'))

    password_textbox = driver.find_element_by_id('pass')
    password_textbox.send_keys(dados.get('senha'))

    login_button = driver.find_element_by_id('u_0_b')
    login_button.submit()
