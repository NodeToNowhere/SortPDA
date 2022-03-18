class SortArray:

    def standard_sort(self, array):
        array.sort()
        return array

    def reverse_sort(self, array):
        array.sort(reverse=True)
        return array

    def sortLength(self, array):
        def sortKey(e):
            return len(e)
        array.sort(key=sortKey)
        return array

    