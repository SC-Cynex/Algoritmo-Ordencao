from algoritmos.strategy import OrdenacaoStrategy
import threading

class InsertionSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0
        threads = []
        lock = threading.Lock()
        
        def insertion_task(i):
            nonlocal comparacoes, trocas
            chave = dados[i]
            j = i - 1
            local_comps = 0
            local_trocas = 0
            
            while j >= 0 and chave < dados[j]:
                local_comps += 1
                dados[j + 1] = dados[j]
                local_trocas += 1
                j -= 1
            dados[j + 1] = chave
            
            with lock:
                comparacoes += local_comps
                trocas += local_trocas
        
        for i in range(1, len(dados)):
            t = threading.Thread(target=insertion_task, args=(i,))
            t.start()
            threads.append(t)
            
            if len(threads) >= 4:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
            
        return dados, comparacoes, trocas

# from algoritmos.strategy import OrdenacaoStrategy

# class InsertionSort(OrdenacaoStrategy):
#     def ordenar(self, dados):
#         comparacoes = 0
#         trocas = 0
#         for i in range(1, len(dados)):
#             chave = dados[i]
#             j = i - 1
#             while j >= 0 and chave < dados[j]:
#                 comparacoes += 1
#                 dados[j + 1] = dados[j]
#                 trocas += 1
#                 j -= 1
#             dados[j + 1] = chave
#         return dados, comparacoes, trocas