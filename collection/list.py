l1=[5,22,"Computer","Hindi","B","L"]
l2=[43,67,88,43,35]
print("1.len() /n 2.append() /n 3.extend() /n 4.insert() /n 5.remove() /n 6.pop() /n 7.reverse() /n 8.min() /n 9.max() /n 10.count() /n 11.sort() /n 12.index() /n 13.clear() /n 14.Data Type() /n 15.Concatenation() /n 16.Multiplication() /n")
choice=int(input("Enter your choice:"))
if(choice==1):
  ch=int(input("Enter 1 to view length of list1 and enter 2 to view length of list2 \n choice:"))
  if(ch==1):
    print("Length of the list1")
    print(len(l1))
    print("Print the current list1")
    print(l1)
  elif(ch==2):
    print("Length of the list2")
    print(len(l2))
    print("Print the current 2")
    print(l2)
  else:
    print("Invalid")
elif (choice==2):
  ch=int(input("Enter 1 to append list1 and enter 2 to append list2 \n choice:"))
  if(ch==1):
    print("List1");
    print(l1)
    c=int(input("Enter 1 for number to append and enter 2 for value to append \n choice:"))
    if(c==1):
              n=int(input("Enter the number to append"))
              print("Add the number at the last of the list1")
              l1.append(n)
              print("Print the current list1")
              print(l1)
    elif(c==2):
              n=str(input("Enter the value to append"))
              print("Add the value at the last of the list1")
              l1.append(n)
              print("Print the current list1")
              print(l1)
    else:
              print("Invalid")
  elif(ch==2):
              n=int(input("Enter the number to append"))
              l2.append(n)
              print("Print the current list2")
              print(l2)
  else:
              print("Invalid")
elif (choice==3):
  ch=int(input("Enter 1 for extend list1 and enter 2 for extend list2 \n choice:"))
  if(ch==1):
    n=int(input("Enter the number to extend"))
    m=str(input("Enter the value to extend"))
    print("Adding one or more items in the list1")
    l1.extend([n,m])
    print("Print the current list1")
    print(l1)
  elif(ch==2):
    n=int(input("Enter the number to extend"))
    print("Adding one or more items in the list2")
    l2.extend([n])
    print("Print the current list2")
    print(l2)
  else:
    print("Invalid")
elif (choice==4):
  ch=int(input("Enter 1 for number and enter 2 for character \n choice:"))
  if(ch==1):
    n=int(input("Enter the position"))
    m=int(input("Enter the number to insert"))
    print("Adding a item in a list1 by a specifying the position")
    l1.insert(n,m)
    print("Print the current list1")
    print(l1)
  elif(ch==2):
    n=int(input("Enter the position"))
    k=str(input("Enter the value to insert"))
    print("Adding a item in a list1 by a specifying the position")
    l1.insert(n,k)
    print("Print the current list1")
    print(l1)
  else:
    print("Invalid")
elif (choice==5):
    ch=int(input("Enter 1 for number to and enter 2 for character \n choice:"))
    if(ch==1):
      n=int(input("Enter the number to delete"))
      print("Removing any item in a list1 by a specifying the position")
      l1.remove(n)
      print("Print the current list1")
      print(l1)
    elif(ch==2):
      k=str(input("Enter the value to delete"))
      print("Removing any item in a list1 by a specifying the position")
      l1.remove(k)
      print("Print the current list1")
      print(l1)
    else:
      print("Invalid")
elif (choice==6):
    n=int(input("Enter the position"))
    print("Deleting  any item in a list1 by a specifying the position")
    l1.pop(n)
    print("Print the current list1")
    print(l1)
elif (choice==7):
    ch=int(input("Enter 1 for reverse list1 and enter 2 for reverse list2 \n choice:"))
    if(ch==1):
        print("Reverse the items in a list1")
        l1.reverse()
        print("Print the current list1")
        print(l1)
    elif(ch==2):
        print("Reverse the items in a list2")
        l2.reverse()
        print("Print the current list2")
        print(l2)
elif (choice==8):
        print("Print the minimum item in the list2")
        print(min(l2))
        print("Print the current list2")
        print(l2)
elif (choice==9):
        print("Print the maximum item in the list2")
        print(max(l2))
        print("Print the current list2")
        print(l2)
elif (choice==10):
        print("List 2")
        print(l2)
        n=int(input("Print the occurance item "))
        print(l2.count(n))
elif (choice==11):
        print("Sorting the item in the list2 in a order");
        l2.sort()
        print(l2)
elif (choice==12):
        ch=int(input("Enter 1 for view list1 and enter 2 for view list2 \n choice:"))
        if(ch==1):
            print("List1");
            print(l1)
            c=int(input("Enter 1 for number to find and enter 2 for value to find \n choice:"))
            if(c==1):
              n=int(input("Enter the number to find the index"))
              print(l1.index(n))
            elif(c==2):
              n=str(input("Enter the value to find the index"))
              print(l1.index(n))
            else:
              print("Invalid")
        elif(ch==2):
            print("List2");
            print(l2)
            n=int(input("Enter the number to find the index"))
            print(l2.index(n))
elif (choice==13):
    ch=int(input("Enter 1 to clear list1 and enter 2 to clear list2 \n choice:"))
    if(ch==1):
        print("Clear the list1")
        print(l1.clear())
    elif(ch==2):
        print("Clear the list2")
        print(l2.clear())
elif (choice==14):
  ch=int(input("Enter 1 to find data type of list1 and enter 2 to find data type of  list2 \n choice:"))
  if(ch==1):
      print("Data type of list1")
      print(type(l1))
  elif(ch==2):
      print("Data type of list2")
      print(type(l2))
elif (choice==15):
    print("Concatenation of two list1 & 2")
    print(l1+l2)
elif (choice==16):
    n=int(input("Enter the number to repeated"))
    print("Multiply the list1 by given number")
    print(l1*n)
else:
      print("Invalid")
  
