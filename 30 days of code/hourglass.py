
import sys
arr = []
max = -100
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

for i in range(4):
    for j in range(4):
        sum = arr[i+1][j+1]
        for x in range(3):
            sum += arr[i][j+x] + arr[i+2][j+x]
        if sum > max:
            max = sum
print(max)

