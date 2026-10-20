"""
   int (integer) - butun sonlar(-2,-1,0,1,2,3)
   float (floating point) - (5.2,6.0,1.5,-8.3)

   Amallar (operation):
    +,-,*,/,//,%,**
    / - oddiy bolish : 10 / 5=2
    // - butun bolish : 14 // 4 = 3
    % - qoldiqli bolish:14%4= 2
    **-darajaga oshirish: 5**2=25

"""

# #Masala #1

# l = int (input("l="))
# m = l // 100
# print ("metr:",m)

# Masala #2
# m = int(input("m="))
# t = m // 1000
# print("Tonna:",t)

# Masala #3

# a = int (input("a="))
# h = a // 1024
# print ("kb:",h)

# #Masala #4
# a = int (input("a="))
# b = int (input("b="))

# c= a // b
# print("c=",c)

#Masala #5
# a = int (input("a="))
# b = int (input("b="))

# c= a % b
# print("c=",c)

# #Masala #6

# son= int (input("son="))

# c = son // 10
# b = son % 10 
# print("O'nliklar xonasi:",c)
# print("Birliklar xonasi:",b)

#Masala #7

son = int (input("son="))

b = son  // 10 + son % 100

print ("raqamlar yig'indisi=:",b)

#Masala #8

son = int (input("a="))

a = son // 10
b = son % 10 

c = a * 10 + b

print("Hosil bo'lgan son:",c)

#Masala #9

son = int (input("son="))

b = son // 100

print("Yuzlar xonasidagi raqam:",b)

#Masala #10

son = int (input("son="))



#Masala #11

son = int (input("a="))

a = son // 100
b =  (son // 10) % 10
c = son % 10

formula =  a + b + c
print("3xonali sonlar yig'indisi:",formula)

#Masala #12

son = int (input("3 xonali son="))

a = son // 100
b = (son // 10) % 10
c = son % 10
formula = a * 100 + b * 10 + c
print("Hosil bo'lgan son:")

#Masala #13

son = int (input("3 xonali son="))

a = son // 100
b = son % 100
c = b * 10 + a
print("Hosil bo'lgan son:",c)

#Masala #16

son = int (input("3 xonali son="))

a = son // 100
b = (son // 10) % 10
c = son % 10
formula = a * 100 + c * 10 + b
print("Hosil bo'lgan son:")



