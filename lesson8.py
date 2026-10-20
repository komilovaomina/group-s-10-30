#Masala #8

# son = int(input("son = "))

# a = son // 10 #o'nliklar xonasi
# b = son % 10 #birliklar xonasi
# son2 = b * 10 + a
# print("Natija:" , son 2)

# #Masala #9

# son = int(input("son ="))
# res = son // 100

# print("Natija:",res)

# #Masala #10

# number = int(input("number ="))
# res = (number // 10)%10
# print("Natija:",res)

# #Masala #11

# number = int (input("number="))

# a = number // 100
# b =  (number // 10) % 10
# c = number % 10

# res =  a + b + c
# print("3xonali sonlar yig'indisi:",res)

"""
    str(string) - matn 
    str()->matn qilib beruvchi funksiya
    Amallar:
    (+) - konkenatsiya (matnni matnga qo'shish)
    (*) - Matnni ko'paytirish
"""
#int,float,str

t1 = "Hello world" # str
t2 = 'Hello world' # str
t3 = """ Hello world """ # str
t4 = ''' Hello world ''' # str
"""
text1 = "o',g' kabi matnlarga yoki o\' shu yol bn o',g'xarflarini yozsak boladi"
text2 = """""" , '''''' -> kop matn yozsa boladi
text3 = (
     "Assalomu aleykum"
     "Mening ismim Omina"
     "Mening yoshim 18da"
     "Men IT house da oqiyman"
)
 \n -> qatorni pastga tushirib beradi.Misol:
  "Assalomu aleykum./nMening ismim Omina./nMening yoshim 18da./nMen IT house da oqiyman"
 \t -> tabulatsiya qoyib beradi.Misol:
  "/tHello world"

  a = "Hello"
  b =  "world"
  c = a + b

  c = a + " " + b + "!"
"""

first_name = input("Ism kiriting:")
last_name = input("Familiya kiriting:")
bdate = int(input("Tug'ilgan yil kiriting:"))

age = 2026 - bdate

t1 = "Assalomu aleykum," + first_name + " " + last_name + "."
t2 = "\nSizning yoshingiz " + str(age) + "da."

answer_text = t1 + t2
print(answer_text)





