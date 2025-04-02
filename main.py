import time
import os
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
from algoritmos.binary import BinarySearchWithCache

def executar_algoritmo(strategy, dados):
    inicio = time.time()
    dados_ordenados, comparacoes, trocas = strategy.ordenar(dados.copy())
    fim = time.time()
    tempo_execucao = (fim - inicio) * 1000
    
    print(f"\nEstatísticas do {strategy.__class__.__name__}:")
    print(f"  - Tamanho do array: {len(dados)}")
    print(f"  - Comparações: {comparacoes}")
    print(f"  - Trocas: {trocas}")
    print(f"  - Tempo de execução: {tempo_execucao:.2f} ms")

    return dados_ordenados, tempo_execucao, comparacoes, trocas
algoritmos = {
    "Bubble Sort": BubbleSort(),
    "Insertion Sort": InsertionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
    "Binary Search": BinarySearchWithCache()
}
def main():
    nome_arquivo = 'data/dados_1000.txt'
    os.makedirs('data', exist_ok=True)

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado. Gerando dados...")
        gerar_dados(1000, nome_arquivo)

    dados = ler_dados(nome_arquivo)
    dados_ordenados, _, _, _ = executar_algoritmo(MergeSort(), dados)
    
    buscador = BinarySearchWithCache()
    valores_para_buscar = [dados_ordenados[0], dados_ordenados[-1], 
                          dados_ordenados[len(dados_ordenados)//2], 99999]
    
    for valor in valores_para_buscar:
        inicio = time.time()
        indice = buscador.binary_search(dados_ordenados, valor)
        fim = time.time()
        tempo_execucao = (fim - inicio) * 1000
        
        if indice != -1:
            print(f"Valor {valor} encontrado no índice {indice} (tempo: {tempo_execucao:.4f} ms)")
        else:
            print(f"Valor {valor} não encontrado (tempo: {tempo_execucao:.4f} ms)")

    print("\nTestando cache:")
    valor_teste = dados_ordenados[len(dados_ordenados)//2]

    inicio = time.time()
    buscador.binary_search(dados_ordenados, valor_teste)
    fim = time.time()
    print(f"Tempo da primeira busca: {(fim - inicio) * 1000:.4f} ms")

    inicio = time.time()
    buscador.binary_search(dados_ordenados, valor_teste)
    fim = time.time()
    print(f"Tempo da segunda busca: {(fim - inicio) * 1000:.4f} ms")
    
    buscador.clear_cache()
if __name__ == "__main__":
    main()