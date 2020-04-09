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
    driver.get('http://gambolao.net/main.php')

    username_textbox = driver.find_element_by_name('username')
    username_textbox.send_keys(dados.get('email'))

    password_textbox = driver.find_element_by_name('pw')
    password_textbox.send_keys(dados.get('senha'))

    login_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[2]")
    login_button.submit()
