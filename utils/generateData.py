import random

def gerar_dados(tamanho, nome_arquivo):
    dados = [random.randint(0, 1000000) for _ in range(tamanho)]
    with open(nome_arquivo, 'w') as f:
        for numero in dados:
            f.write(f"{numero}\n")