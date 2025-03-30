from algoritmos.strategy import OrdenacaoStrategy
import multiprocessing as mp

class QuickSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        with mp.Manager() as manager:
            comparacoes = manager.Value('i', 0)
            trocas = manager.Value('i', 0)
            
            dados_local = list(dados)
            
            max_depth = 3
            
            self._quick_sort_parallel(dados_local, 0, len(dados_local) - 1, comparacoes, trocas, max_depth)
            
            return dados_local, comparacoes.value, trocas.value

    def _quick_sort_parallel(self, dados, baixo, alto, comparacoes, trocas, max_depth):
        if baixo < alto:
            pi = self._particionar(dados, baixo, alto, comparacoes, trocas)

            if max_depth > 0:
                esquerda = mp.Process(target=self._quick_sort_parallel, args=(dados, baixo, pi - 1, comparacoes, trocas, max_depth - 1))
                direita = mp.Process(target=self._quick_sort_parallel, args=(dados, pi + 1, alto, comparacoes, trocas, max_depth - 1))
                
                esquerda.start()
                direita.start()
                
                esquerda.join()
                direita.join()
            else:
                self._quick_sort_sequencial(dados, baixo, pi - 1, comparacoes, trocas)
                self._quick_sort_sequencial(dados, pi + 1, alto, comparacoes, trocas)

    def _quick_sort_sequencial(self, dados, baixo, alto, comparacoes, trocas):
        if baixo < alto:
            pi = self._particionar(dados, baixo, alto, comparacoes, trocas)
            self._quick_sort_sequencial(dados, baixo, pi - 1, comparacoes, trocas)
            self._quick_sort_sequencial(dados, pi + 1, alto, comparacoes, trocas)

    def _particionar(self, dados, baixo, alto, comparacoes, trocas):
        pivo = dados[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            comparacoes.value += 1
            if dados[j] < pivo:
                i += 1
                dados[i], dados[j] = dados[j], dados[i]
                trocas.value += 1
        dados[i + 1], dados[alto] = dados[alto], dados[i + 1]
        trocas.value += 1
        return i + 1


# from algoritmos.strategy import OrdenacaoStrategy

# class QuickSort(OrdenacaoStrategy):
#     def ordenar(self, dados):
#         comparacoes = [0]
#         trocas = [0]
#         self._quick_sort(dados, 0, len(dados) - 1, comparacoes, trocas)
#         return dados, comparacoes[0], trocas[0]

#     def _quick_sort(self, dados, baixo, alto, comparacoes, trocas):
#         if baixo < alto:
#             pi = self._particionar(dados, baixo, alto, comparacoes, trocas)
#             self._quick_sort(dados, baixo, pi - 1, comparacoes, trocas)
#             self._quick_sort(dados, pi + 1, alto, comparacoes, trocas)

#     def _particionar(self, dados, baixo, alto, comparacoes, trocas):
#         pivo = dados[alto]
#         i = baixo - 1
#         for j in range(baixo, alto):
#             comparacoes[0] += 1
#             if dados[j] < pivo:
#                 i += 1
#                 dados[i], dados[j] = dados[j], dados[i]
#                 trocas[0] += 1
#         dados[i + 1], dados[alto] = dados[alto], dados[i + 1]
#         trocas[0] += 1
#         return i + 1