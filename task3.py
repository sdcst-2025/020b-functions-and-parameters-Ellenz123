#!python3
"""
Create a function called perimeter()
The input is a list or tuple.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter(numbers):
  numbers=list(numbers)
  total=0
  
  for i in numbers:
    total += i
    pass
  print(f"The sum of all numbers in {numbers} is {total}")
  return total

if __name__ == "__main__":
  assert perimeter( [5,2,3,4] ) == 14
  assert perimeter( [5,2,4] ) == 11
  assert perimeter( [5,2.2,3] ) == 10.2
  assert perimeter( [5,2,3,4,1,3,2] ) == 20
  assert perimeter( [4,4,4,4] ) == 16

