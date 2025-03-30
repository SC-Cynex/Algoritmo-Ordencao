from algoritmos.strategy import OrdenacaoStrategy
from multiprocessing import Pool, cpu_count

class BubbleSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        n = len(dados)
        if n < 1000:
            return BubbleSort().ordenar(dados)
            
        with Pool(cpu_count()) as pool:
            for i in range(n):
                pool.apply(self._bubble_pass, (dados, n-i-1))
                
        comparacoes = n * (n - 1) // 2
        trocas = self._count_swaps(dados)
        return dados, comparacoes, trocas

    def _bubble_pass(self, dados, end):
        for j in range(end):
            if dados[j] > dados[j+1]:
                dados[j], dados[j+1] = dados[j+1], dados[j]

    def _count_swaps(self, dados):
        return sum(1 for i in range(len(dados)-1) if dados[i] > dados[i+1])

# from algoritmos.strategy import OrdenacaoStrategy


# class BubbleSort(OrdenacaoStrategy):
#     def ordenar(self, dados):
#         n = len(dados)
#         comparacoes = 0
#         trocas = 0
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 comparacoes += 1
#                 if dados[j] > dados[j+1]:
#                     dados[j], dados[j+1] = dados[j+1], dados[j]
#                     trocas += 1
#         return dados, comparacoes, trocas