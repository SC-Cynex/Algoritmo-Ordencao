from algoritmos.strategy import OrdenacaoStrategy

class TimSort(OrdenacaoStrategy):
    def ordenar(self, dados):
        comparacoes = [0]
        trocas = [0]

        MIN_MERGE = 32

        def insertion_sort(arr, left, right):
            for i in range(left + 1, right + 1):
                j = i
                while j > left and arr[j] < arr[j - 1]:
                    comparacoes[0] += 1
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    trocas[0] += 1
                    j -= 1

        def merge(arr, left, mid, right):
            len1, len2 = mid - left + 1, right - mid
            left_arr, right_arr = arr[left:mid + 1], arr[mid + 1:right + 1]
            i = j = 0
            k = left

            while i < len1 and j < len2:
                comparacoes[0] += 1
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
                trocas[0] += 1

            while i < len1:
                arr[k] = left_arr[i]
                i += 1
                k += 1
                trocas[0] += 1

            while j < len2:
                arr[k] = right_arr[j]
                j += 1
                k += 1
                trocas[0] += 1

        def tim_sort(arr):
            n = len(arr)
            for i in range(0, n, MIN_MERGE):
                insertion_sort(arr, i, min(i + MIN_MERGE - 1, n - 1))

            size = MIN_MERGE
            while size < n:
                for left in range(0, n, 2 * size):
                    mid = left + size - 1
                    right = min(left + 2 * size - 1, n - 1)
                    if mid < right:
                        merge(arr, left, mid, right)
                size *= 2

        tim_sort(dados)
        return dados, comparacoes[0], trocas[0]
