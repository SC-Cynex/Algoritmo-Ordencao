from algoritmos.strategy import OrdenacaoStrategy

class SelectionSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0
        for i in range(len(dados)):
            min_idx = i
            for j in range(i+1, len(dados)):
                comparacoes += 1
                if dados[j] < dados[min_idx]:
                    min_idx = j
            dados[i], dados[min_idx] = dados[min_idx], dados[i]
            trocas += 1
        return dados, comparacoes, trocas