'''
Given an integer n, find the nth Fibonacci number

Sample input: 10
Output: 55

'''

def fibonacci(n):
  if n<=1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)