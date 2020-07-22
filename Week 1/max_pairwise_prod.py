# Maximum Pairwise Product

'''
Find the maximum product of two distinct numbers
in a sequence of non-negative integers.

Input: A sequence of non-negative
integers.

Output: The maximum value that
can be obtained by multiplying
two different elements from the sequence

Sample Input: [1,2,3]
Ouput: 6
'''

def max_pairswise_prod(val):
  max_val = 0
  for i in range(len(val)-1):
    max_val = max(max_val, val[i] * val[i+1])
  return max_val

if __name__ == '__main__':
  val = [x for x in map(int, input().split())]
  print(max_pairswise_prod(val))
