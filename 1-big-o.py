# Ω = Best case       (Omega)
# θ = Average case    (Theta)
# O = Worst case      (Omikron - Big O)

# [ 1, 2, 3, 4, 5, 6, 7 ]
#   Ω        θ        O

# O(n): Linear. Ran n times
def print_items1(n):
  for i in range(n):
    print(i)
    # n prints


# O(n): Linear. Ran 2n times. O(2n) = O(n)    {still linear}
def print_items2(n):
  for i in range(n):
    print(i)

  for j in range(n):
    print(j)
    # n + n prints


# O(n²): Potential. Ran n² times
def print_items3(n):
  for i in range(n):
    for j in range(n):
      print(i, j)
      # n * n prints


# O(n²): Potential. Ran n³ times. O(n³) = O(n²)    {still potential}
def print_items(n):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        print(i, j, k)
        # n * n * n prints


# O(n²): Potential. Ran n² + n times. O(n² + n) = O(n²)    {still potential}
def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i, j)
      # n * n prints

    for k in range(n):
      print(k)
      # n prints


# O(1): Constant. Ran 1 time. Most efficient Big O
def add_items(n):
  print(n + n + n + n + n)
  # 1 print


# Search for 1 using halfs:

# [ 1, 2, 3, 4, 5, 6, 7, 8 ]      {left half: step 1}
# [ 1, 2, 3, 4 ]                  {left half: step 2}
# [ 1, 2 ]                        {left half: step 3}
# [ 1 ]                           {1 found}

# It took 3 steps to find an item in a list of 8 items.
# 2³ = 8    =>    log₂(8) = 3
# O(log₂(n)) = O(log(n)). Very efficient Big O.


# O(a + b). a ≠ b ≠ 2n
def print_items2(a, b):
  for i in range(a):
    print(a)
    # a prints

  for j in range(b):
    print(b)
    # b prints


# O(a * b). a ≠ b ≠ 2n
def print_items2(a, b):
  for i in range(a):
    for j in range(b):
      print(a, b)
      # a * b prints


# Adding or popping last item in a list: O(1): only 1 operation takes place
# Adding or popping any otheri tem in a list: O(n): n operations must take place to re-order the indexes.


# n = 100
# O(1) = 1
# O(log(n)) ≈ 7
# O(n) = 100
# O(n²) = 10.000


# n = 1.000
# O(1) = 1
# O(log(n)) ≈ 10
# O(n) = 1.000
# O(n²) = 1.000.000


# O(1) - Constant                   {excellent}
# O(log(N)) - Divide and Conquer    {excellent}
# O(n) - Proporitonal               {very good}
# O(n²) = Loop within a loop        {horrible}