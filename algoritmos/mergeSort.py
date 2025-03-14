from algoritmos.strategy import OrdenacaoStrategy

class MergeSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        comparacoes = [0]
        trocas = [0]
        self._merge_sort(dados, comparacoes, trocas)
        return dados, comparacoes[0], trocas[0]

    def _merge_sort(self, dados, comparacoes, trocas):
        if len(dados) > 1:
            meio = len(dados) // 2
            esquerda = dados[:meio]
            direita = dados[meio:]

            self._merge_sort(esquerda, comparacoes, trocas)
            self._merge_sort(direita, comparacoes, trocas)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                comparacoes[0] += 1
                if esquerda[i] < direita[j]:
                    dados[k] = esquerda[i]
                    i += 1
                else:
                    dados[k] = direita[j]
                    j += 1
                k += 1
                trocas[0] += 1

            while i < len(esquerda):
                dados[k] = esquerda[i]
                i += 1
                k += 1
                trocas[0] += 1

            while j < len(direita):
                dados[k] = direita[j]
                j += 1
                k += 1
                trocas[0] += 1