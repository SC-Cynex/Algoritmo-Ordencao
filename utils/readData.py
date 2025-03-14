def ler_dados(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return [int(line.strip()) for line in f]