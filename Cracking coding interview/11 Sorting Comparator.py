
'''

https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

In this challenge Quicksort algo is used

Recursive Quicksort
https://www.geeksforgeeks.org/quick-sort/

Iterative Quicksort
https://www.geeksforgeeks.org/iterative-quick-sort/

http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html

'''


'''


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        if   arr[j] <= pivot:
         
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 

def quickSort(arr,low,high):
    if low < high:
 
        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
 

'''

'''
 

def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
       
        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
 

def quickSort(arr,low,high):
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
# Driver Code
if __name__ == '__main__' :
     
    arr = [4, 2, 6, 9, 2]
    n = len(arr)
     
    quickSort(arr, 0, n - 1)
     
    for i in range(n):
        print(arr[i], end = " ")
 
'''


'''
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val

'''

'''

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name < b.name:
                return -1
            else:
                return 1
        elif a.score > b.score:
            return -1

'''