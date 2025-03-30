from algoritmos.strategy import OrdenacaoStrategy
import multiprocessing as mp

class MergeSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        with mp.Manager() as manager:
            comparacoes = manager.Value('i', 0)
            trocas = manager.Value('i', 0)
            shared_arr = manager.list(dados)
            
            with mp.Pool(processes=mp.cpu_count()) as pool:
                self._merge_sort_parallel(shared_arr, comparacoes, trocas, pool)
            
            return list(shared_arr), comparacoes.value, trocas.value

    def _merge_sort_parallel(self, dados, comparacoes, trocas, pool=None, depth=0, max_depth=2):
        if len(dados) > 1:
            meio = len(dados) // 2
            esquerda = dados[:meio]
            direita = dados[meio:]
            
            if depth < max_depth and pool is not None:

                res1 = pool.apply_async(self._merge_sort_parallel, 
                                      (esquerda, comparacoes, trocas, None, depth+1, max_depth))
                res2 = pool.apply_async(self._merge_sort_parallel, 
                                      (direita, comparacoes, trocas, None, depth+1, max_depth))
                res1.get()
                res2.get()
            else:
                self._merge_sort_parallel(esquerda, comparacoes, trocas, None, depth+1, max_depth)
                self._merge_sort_parallel(direita, comparacoes, trocas, None, depth+1, max_depth)
            
            self._merge(dados, esquerda, direita, comparacoes, trocas)

    def _merge(self, dados, esquerda, direita, comparacoes, trocas):
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            comparacoes.value += 1
            if esquerda[i] < direita[j]:
                dados[k] = esquerda[i]
                i += 1
            else:
                dados[k] = direita[j]
                j += 1
            k += 1
            trocas.value += 1

        while i < len(esquerda):
            dados[k] = esquerda[i]
            i += 1
            k += 1
            trocas.value += 1

        while j < len(direita):
            dados[k] = direita[j]
            j += 1
            k += 1
            trocas.value += 1

# from algoritmos.strategy import OrdenacaoStrategy

# class MergeSort(OrdenacaoStrategy):
#     def ordenar(self, dados):
#         comparacoes = [0]
#         trocas = [0]
#         self._merge_sort(dados, comparacoes, trocas)
#         return dados, comparacoes[0], trocas[0]

#     def _merge_sort(self, dados, comparacoes, trocas):
#         if len(dados) > 1:
#             meio = len(dados) // 2
#             esquerda = dados[:meio]
#             direita = dados[meio:]

#             self._merge_sort(esquerda, comparacoes, trocas)
#             self._merge_sort(direita, comparacoes, trocas)

#             i = j = k = 0

#             while i < len(esquerda) and j < len(direita):
#                 comparacoes[0] += 1
#                 if esquerda[i] < direita[j]:
#                     dados[k] = esquerda[i]
#                     i += 1
#                 else:
#                     dados[k] = direita[j]
#                     j += 1
#                 k += 1
#                 trocas[0] += 1

#             while i < len(esquerda):
#                 dados[k] = esquerda[i]
#                 i += 1
#                 k += 1
#                 trocas[0] += 1

#             while j < len(direita):
#                 dados[k] = direita[j]
#                 j += 1
#                 k += 1
#                 trocas[0] += 1