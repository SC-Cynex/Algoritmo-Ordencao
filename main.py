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
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

# configurando o OpenTelemetry 
resource = Resource.create({"service.name": "sorting-algorithms"})
trace.set_tracer_provider(TracerProvider(resource=resource))
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer("sorting-algorithms")

def executar_algoritmo(strategy, dados):
    with tracer.start_as_current_span(f"{strategy.__class__.__name__}") as span:
        span.set_attribute("array_size", len(dados))
        inicio = time.time()
        dados_ordenados, comparacoes, trocas = strategy.ordenar(dados.copy())
        fim = time.time()
        tempo_execucao = (fim - inicio) * 1000
        
        # setando os atributos no span para visualizaçao no Jaeger
        span.set_attribute("comparisons", comparacoes)
        span.set_attribute("swaps", trocas)
        span.set_attribute("execution_time_ms", tempo_execucao)

        return dados_ordenados, tempo_execucao, comparacoes, trocas

def main():
    nome_arquivo = 'data/dados_1000.txt'
    os.makedirs('data', exist_ok=True)

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado. Gerando dados...")
        gerar_dados(1000, nome_arquivo)

    dados = ler_dados(nome_arquivo)

    algoritmos = {
        "Bubble Sort": BubbleSort(),
        "Bubble Sort Melhorado": BubbleSortPlus(),
        "Insertion Sort": InsertionSort(),
        "Selection Sort": SelectionSort(),
        "Quick Sort": QuickSort(),
        "Merge Sort": MergeSort(),
        "Tim Sort": TimSort(),
        "Heap Sort": HeapSort()
    }

    for nome, algoritmo in algoritmos.items():
        dados_ordenados, tempo_execucao, comparacoes, trocas = executar_algoritmo(algoritmo, dados)
        print(f"Algoritmo: {nome}")
        print(f"Tamanho do conjunto de dados: {len(dados)}")
        print(f"Tempo de execução: {tempo_execucao:.2f} ms")
        print(f"Comparações: {comparacoes}")
        print(f"Trocas: {trocas}")
        print("-" * 40)

if __name__ == "__main__":
    main()