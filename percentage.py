n=int(input("Enter number of subjects: ))
m=int(input("Enter maximum marks: ))
t=0
m=m*n
for i in range (n):
            a=int(input("Enter marks of ",n+1," subject))
            t=a+t
per=(t/m)*100
pritn("Percentage gain is: ",per)                       
            
