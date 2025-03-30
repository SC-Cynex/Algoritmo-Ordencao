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
from opentelemetry.sdk.resources import Resource, SERVICE_NAME

# Configuração do OpenTelemetry
resource = Resource.create({
    SERVICE_NAME: "sorting-algorithms"
})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

def executar_algoritmo(strategy, dados):
    with tracer.start_as_current_span(f"{strategy.__class__.__name__}") as span:
        span.set_attribute("array_size", len(dados))
        inicio = time.time()
        dados_ordenados, comparacoes, trocas = strategy.ordenar(dados.copy())
        fim = time.time()
        tempo_execucao = (fim - inicio) * 1000
        
        span.set_attributes({
            "comparisons": comparacoes,
            "swaps": trocas,
            "execution_time_ms": tempo_execucao
        })
        
        print(f"\nEstatísticas do {strategy.__class__.__name__}:")
        print(f"  - Tamanho do array: {len(dados)}")
        print(f"  - Comparações: {comparacoes}")
        print(f"  - Trocas: {trocas}")
        print(f"  - Tempo de execução: {tempo_execucao:.2f} ms")

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
        "Insertion Sort": InsertionSort(),
        "Quick Sort": QuickSort(),
        "Merge Sort": MergeSort(),
    }

    for nome, algoritmo in algoritmos.items():
        print(f"\n=== Executando {nome} ===")
        dados_ordenados, tempo_execucao, comparacoes, trocas = executar_algoritmo(algoritmo, dados)
        print(f"Resultado para {nome}:")
        print(f"Tempo: {tempo_execucao:.2f} ms | Comparações: {comparacoes} | Trocas: {trocas}")

algoritmos = {
    "Bubble Sort": BubbleSort(),
    "Insertion Sort": InsertionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
}

def testar_tamanhos_diferentes():
    tamanho = 10000
    nome_arquivo = f'data/dados_{tamanho}.txt'
    if not os.path.exists(nome_arquivo):
        print(f"\nArquivo {nome_arquivo} não encontrado. Gerando dados...")
        gerar_dados(tamanho, nome_arquivo)
    
    dados = ler_dados(nome_arquivo)
    print(f"\n=== TESTE COM {tamanho} ELEMENTOS ===")
    
    for nome, algoritmo in algoritmos.items():
        print(f"\nExecutando {nome} com {tamanho} elementos...")
        dados_ordenados, tempo_execucao, comparacoes, trocas = executar_algoritmo(algoritmo, dados)
        print(f"{nome: <20} | Tempo: {tempo_execucao:8.2f} ms | Comparações: {comparacoes:8} | Trocas: {trocas:6}")

if __name__ == "__main__":
    testar_tamanhos_diferentes()