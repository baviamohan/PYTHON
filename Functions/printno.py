a=int(input("Enter the start of range:"))
b=int(input("Enter the end of range:"))
def num(range):
  for i in range(a,b+1):
    if(i%5!=0):
      print(i)
num(range)
