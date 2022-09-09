n=int(input("enter the number of rows"))
for i in range(0,n):
   for j in range(1,i+1):
       d=j*0.1
       print('%0.1f'%d,end="")
   print(" ")
