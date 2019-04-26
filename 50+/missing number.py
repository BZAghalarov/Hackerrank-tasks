
'''
How do you find the missing number in a given integer array of 1 to 100?

'''

# As we know from formula sumof numbers from 1 to n is equal n*(n+1)/2
# For example if we must find sum of numbers from 1 to 1000
# you can calculate it 1000*(1000+1)/2= 500500
def sumByRange(n):
    sum_int = 0
    for i in range(1001):
        sum_int += i
    return sum_int

n = 1000
print(sumByRange(n))
# Output 500500

# With this formula we can find missing number
# Really_sum - current_sum

def sumByArray(nums):
    sum_int = 0
    for i in nums:
        sum_int += i
    return sum_int

nums = [n for n in range(1001) if n!= 7]
print(sumByArray(nums))
# Output 500493