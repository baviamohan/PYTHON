NumList = []
Positive_count = 0
Negative_count = 0
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " %i))
    NumList.append(value)
print("\nList Entered By the User: ",NumList)
for j in range(Number):
    if(NumList[j] >= 0):
        Positive_count = Positive_count + 1
    else:
        Negative_count = Negative_count + 1
print("\nTotal Number of Positive Numbers in this List =  ", Positive_count)
print("Total Number of Negative Numbers in this List = ", Negative_count)

