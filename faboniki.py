n=int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
# if there is only one term, return n1
print("Fibonacci sequence:")
while count<n:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count += 1
