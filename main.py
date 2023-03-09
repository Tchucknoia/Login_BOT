import platform
import os
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def ler_txt(caminho):
    dados = open(caminho, 'r')
    nome = ''
    senha = ''
    links = []
    linhas = dados.readlines()
    for linha in linhas:
        if linha.find('nome BOT LOGIN') != -1:
            nome = linha.strip('nome BOT LOGIN:').rstrip()
        if linha.find('senha BOT LOGIN') != -1:
            senha = linha.strip('senha BOT LOGIN')
            senha = senha.strip(':').rstrip()
        if linha.find('links BOT LOGIN') != -1:
            aux = ''
            for letra in linha.strip('links BOT LOGIN:'):
                if letra == ',':
                    links.append(aux)
                    aux = ''
                aux = aux + letra
            for x in range(len(links)):
                links[x] = links[x].strip(',').strip('[').strip(']').strip(' ')
                if links[x].find('http://') == -1 and links[x].find('https://') == -1:
                    raise ValueError('links do \'nome_senha.txt\' inadequados , sem \'http\', etc...')
    if nome == '' or senha == '' or links == '':
        raise ValueError("valores do nome_senha.txt vazios")
    dados.close()
    return {'email': nome, 'senha': senha, 'links': links}

if __name__ == '__main__':
    from selenium import webdriver
    diretorio = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Linux':
        diretorio_WebDriver = os.path.join(diretorio, 'WebDrivers', 'chromedriver')
        diretorio_txt = os.path.join(diretorio, 'nome_senha.txt')
    elif platform.system() == 'Windows':
        diretorio_WebDriver = os.path.join(diretorio, 'WebDrivers', 'chromedriver.exe')
        diretorio_txt = os.path.join(diretorio, 'nome_senha.txt')

    
    dados = ler_txt(diretorio_txt)
    print('Salve, sou Jubiscreison seu BOT para logar no Gambolao.net O.O')
    print('Peguei alguns dados que estava no arquivo nome_senha.txt:')
    print(f"email:{dados.get('email')}\nlinks:{dados.get('links')}")
    print('E agora to abrindo o Chrome...')
    print(diretorio_WebDriver)
    service = Service(diretorio_WebDriver)
    driver = webdriver.Chrome(service=service)

    driver.get('http://gambolao.net/main.php')

    driver.get('http://gambolao.net/main.php')
    from selenium.webdriver.common.by import By

    username_textbox = driver.find_element(By.NAME, 'username')
    username_textbox.send_keys(dados.get('email'))
    password_textbox = driver.find_element(By.NAME, 'pw')
    password_textbox.send_keys(dados.get('senha'))

    login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Entrar']")


    login_button.submit()
    username_textbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    for cont in range(len(dados.get('links'))):
        driver.get(dados.get('links')[cont])
        time.sleep(3)

    driver.quit()
    exit()
