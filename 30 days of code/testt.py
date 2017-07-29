import itertools
n=int(input())
numbers = [ 1, 3, 9, 27, 81]
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers,i) if sum(seq)==n]
print (result)