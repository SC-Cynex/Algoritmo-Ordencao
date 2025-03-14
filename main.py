import time
from algoritmos.bubbleSort import BubbleSort
from algoritmos.bubbleSortPlus import BubbleSortPlus
from algoritmos.insertionSort import InsertionSort
from algoritmos.selectionSort import SelectionSort
from algoritmos.quickSort import QuickSort
from algoritmos.mergeSort import MergeSort
from algoritmos.timSort import TimSort
from algoritmos.heapSort import HeapSort
from utils.generateData import gerar_dados
from utils.readData import ler_dados
from utils.logger import registrar_log

def executar_algoritmo(strategy, dados):
    inicio = time.time()
    dados_ordenados, comparacoes, trocas = strategy.ordenar(dados.copy())
    fim = time.time()
    tempo_execucao = (fim - inicio) * 1000
    return dados_ordenados, tempo_execucao, comparacoes, trocas

def comparar_algoritmos(algoritmos, nome_arquivo, repeticoes=5):
    dados = ler_dados(nome_arquivo)
    resultados = []

    for nome, strategy in algoritmos.items():
        tempos = []
        total_comparacoes = 0
        total_trocas = 0

        for _ in range(repeticoes):
            _, tempo_execucao, comparacoes, trocas = executar_algoritmo(strategy, dados)
            tempos.append(tempo_execucao)
            total_comparacoes += comparacoes
            total_trocas += trocas

        tempo_medio = sum(tempos) / repeticoes
        comparacoes_medias = total_comparacoes // repeticoes
        trocas_medias = total_trocas // repeticoes

        resultados.append((nome, tempo_medio, comparacoes_medias, trocas_medias))

        registrar_log(nome, len(dados), tempo_medio, comparacoes_medias, trocas_medias)

    return resultados

def main():

    nome_arquivo = 'dados/dados_1000.txt'
    try:
        with open(nome_arquivo, 'r'):
            pass
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Gerando dados...")
        gerar_dados(1000, nome_arquivo)

    algoritmos = {
        "Bubble Sort": BubbleSort(),
        "Bubble Sort Melhorado": BubbleSortPlus(),
        "Insertion Sort": InsertionSort(),
        "Selection Sort": SelectionSort(),
        "Quick Sort":  QuickSort(),
        "Merge Sort": MergeSort(),
        "Tim Sort": TimSort(),
        "Heap Sort": HeapSort()
    }

    resultados = comparar_algoritmos(algoritmos, nome_arquivo)

    print("\nResultados:")
    for nome, tempo, comparacoes, trocas in resultados:
        print(f"{nome}: Tempo = {tempo:.2f} ms, Comparações = {comparacoes}, Trocas = {trocas}")

if __name__ == "__main__":
    main()