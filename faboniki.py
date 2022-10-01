n=int(input("How many terms? "))
if n==1:
  print("0")
elif n==2:
  print("0,1")
elif n<2:
  n1, n2 = 0, 1
  count = 0
  print("Fibonacci sequence:")
  while count<n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
else:
  print("INVALID INPUT")
