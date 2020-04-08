def ler_txt(caminho):
    dados = open(caminho, 'r')
    linhas = dados.readlines()
    for linha in linhas:
        if linha.find('nome') != -1:
            nome = linha.strip('nome:').rstrip()
        if linha.find('senha') != -1:
            senha = linha.strip('senha:').rstrip()
    dados.close()
    return {'email': nome, 'senha': senha}

if __name__ == '__main__':
    print(ler_txt('nome_senha.txt'))
