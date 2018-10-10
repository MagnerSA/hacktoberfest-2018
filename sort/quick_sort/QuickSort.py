'''
    A implementation of Quick Sort using  partition strategy Lomuto
'''

def sort(array):
    QuickSort(array, 0, len(array) -1)

def QuickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        QuickSort(array, start, (pivot - 1))
        QuickSort(array, (pivot + 1), end)

def partition(array, start, end):
    pivot = start

    for i in range(start, end):
        if array[i] <= array[end]:
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1

    array[end], array[pivot] = array[pivot], array[end]
    return pivot



