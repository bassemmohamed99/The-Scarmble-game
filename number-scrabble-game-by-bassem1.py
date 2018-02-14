print(" Scrabble game")
print("Hello and Welcome")
print("Instructions:")
print("Each Player must choose 3 numbers which their sum is equal 15 EX:(9,4,2)")
name1 = str(input("player 1 enter your name:"))
name2 = str(input("player 2 enter your name:"))
print("let's get started")
list = [1,2,3,4,5,6,7,8,9]
print(list)
x = int(input(name1+" choose your first number from list:"))
list.remove(x)
print(list)
y = int(input(name2+" choose your first number from list:"))
list.remove(y)
print(list)
z = int(input(name1+" choose your second number from list:"))
list.remove(z)
print(list)
k = int(input(name2+" choose your second number from list:"))
list.remove(k)
print(list)
l = int(input(name1+" choose your third number from list:"))
list.remove(l)
print(list)
if (x+z+l)==15:
    print(name1+" is winner")
elif (x+z+l)!=15:
    m = int(input(name2+" choose your third number from list:"))
    list.remove(m)
    print(list)
    if (y+k+m)==15:
        print(name2+" is winner")
    elif (y+k+m)!=15:
        c = int(input(name1+" choose another number from list:"))
        list.remove(c)
        print(list)
        if (x+z+c)==15 or (x+l+c)==15 or (l+z+c)==15:
            print(name1+" is winner")
    else:
        (x+z+c)!=15 and (x+l+c)!=15 and (l+z+c)!=15
        p = int(input(name2+" choose another number from list:"))
        list.remove(p)
        print(list)
        if (y+k+p)==15 or (y+m+p)==15 or (m+k+p)==15:
            print(name2+" is winner")
else:
    if (y+k+p)!=15 and (y+m+P)!=15 and (m+k+P)!=15:
        q = int(input(name1+" choose the last number from list:"))
        list.remove(q)
        print(list)
    elif (x+z+q)==15 or (x+l+q)==15 or (l+z+q)==15 or (x+c+q)==15 or (z+c+q)==15 or (l+c+q)==15:
        print(name1+" is winner")
    else:
        print("draw")
                    
        
        

           
