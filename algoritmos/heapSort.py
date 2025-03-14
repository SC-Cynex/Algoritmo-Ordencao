from algoritmos.strategy import OrdenacaoStrategy

class HeapSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        comparacoes = [0]
        trocas = [0]
        n = len(dados)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(dados, n, i, comparacoes, trocas)

        for i in range(n - 1, 0, -1):
            dados[i], dados[0] = dados[0], dados[i]
            trocas[0] += 1
            self._heapify(dados, i, 0, comparacoes, trocas)

        return dados, comparacoes[0], trocas[0]

    def _heapify(self, dados, n, i, comparacoes, trocas):
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and dados[esquerda] > dados[maior]:
            maior = esquerda
        comparacoes[0] += 1

        if direita < n and dados[direita] > dados[maior]:
            maior = direita
        comparacoes[0] += 1

        if maior != i:
            dados[i], dados[maior] = dados[maior], dados[i]
            trocas[0] += 1
            self._heapify(dados, n, maior, comparacoes, trocas)