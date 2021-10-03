s=input("enter the string here: ")

i,j,f=0,-1,0

while(i<len(s)//2):
  if(s[i]!=s[j]):
    f=1
    break
  i+=1
  j-=1
if(f==0):
  print(s ," is palindrome..")
else:
  print(s, "is not palindrome")
