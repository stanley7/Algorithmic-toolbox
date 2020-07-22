'''
Given two integers ?? and ??, find their greatest common divisor

Sample input: 10,100
Output: 10
'''
def gcd(a,b):
  result = 1
  for i in range(2, min(a,b)+1):
    if a%i==0 and b%i==0:
      if i>result:
        result = i

  return result

print(gcd(10, 100))

