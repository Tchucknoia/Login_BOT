import platform
import os
import sys
import time

def ler_txt(caminho):
    dados = open(caminho, 'r')
    nome = ''
    senha = ''
    linhas = dados.readlines()
    for linha in linhas:
        if linha.find('nome') != -1:
            nome = linha.strip('nome:').rstrip()
        if linha.find('senha') != -1:
            senha = linha.strip('senha')
            senha = senha.strip(':').rstrip()
    dados.close()
    return {'email': nome, 'senha': senha}

if __name__ == '__main__':
    from selenium import webdriver
    diretorio = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Linux':
        diretorio_WebDriver = diretorio + '/WebDrivers/chromedriver'
        diretorio_txt = diretorio + '/nome_senha.txt'
    elif platform.system() == 'Windows':
        diretorio_WebDriver = diretorio + '\\WebDrivers\\chromedriver.exe'
        diretorio_txt = diretorio + '\\nome_senha.txt'

    print('Salve, sou Jubiscreison seu BOT para logar no Gambolao.net -_-')
    dados = ler_txt(diretorio_txt)
    print('Peguei alguns dados que estava no arquivo nome_senha.txt:')
    print(f"email:{dados.get('email')}\nsenha:{dados.get('senha')}")
    resposta = input('Confirma eles para mim?(y/(any key)):').lower()
    if resposta != 'y':
        sys.exit()
    print('To abrindo o Chrome...')
    driver = webdriver.Chrome(diretorio_WebDriver)
    driver.get('http://gambolao.net/main.php')
    username_textbox = driver.find_element_by_name('username')
    username_textbox.send_keys(dados.get('email'))
    password_textbox = driver.find_element_by_name('pw')
    password_textbox.send_keys(dados.get('senha'))

    login_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[2]")
    login_button.submit()

    time.sleep(3)
    driver.get('https://gambolao.net/federacao.php?nome=Cazaquistao&mural=sim')
    time.sleep(3)
    driver.get('https://gambolao.net/federacao.php?mural=sim&pag=2&nome=Cazaquistao')
    time.sleep(3)
    driver.get('https://gambolao.net/federacao.php?mural=sim&pag=3&nome=Cazaquistao')
