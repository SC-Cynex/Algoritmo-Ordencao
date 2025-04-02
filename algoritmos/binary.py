class BinarySearchWithCache:
    def __init__(self):
        self.cache = {}
        
    def binary_search(self, arr, target, low=None, high=None):
        if target in self.cache:
            return self.cache[target]

        if low is None and high is None:
            low = 0
            high = len(arr) - 1
            
        if high < low:
            self.cache[target] = -1
            return -1
            
        mid = (low + high) // 2
        
        if arr[mid] == target:
            self.cache[target] = mid
            return mid

        elif arr[mid] > target:
            return self.binary_search(arr, target, low, mid - 1)

        else:
            return self.binary_search(arr, target, mid + 1, high)
            
    def clear_cache(self):
        """Limpa o cache de resultados"""
        self.cache = {}