"""
Sana:06-10-2026
Mavzu:
     -String methodlari bilan ishlash
     -Methodlar:
      -count,strip,rstrip,lstrip
      -replace,find,index
      -join,split
      -starwith,endswith

"""


# text = input("Matn kiriting:")

# counter1 = text.count("a")
# counter2 = text.count("A")
# print(f"Matnda 'a' harfi {counter1 + counter2} marta ishlatilgan")

# text = input("Matn kiriting: ").lower()
# counter1 = text.count("a")
# print(f"Matnda 'a' harfi {counter1} marta ishlatilgan")

# text = "  Hello world    "
# text = text.strip()
# print(text)
# Matndagi boshliqlarni olib tashlaydi.Chap tarafdagi boshliqni olib tashlash uchun:

# text = "    Hello world" 
# text = text.lstrip()
# print(text)

#O'ng tarafdagi boshliqni olib tashlash uchun:

# text = "Hello world     "
# text = text.rstrip()
# print(text)

# name = input("Ism kiriting:").title()

# text = "Assalomu alaykum,user!"
# text = text.replace("user",name)
# print (text)


# index ->xarfni tartib raqami

# text = "Muslima aqlli" 


# print( text[0])
# print( text[4])
# print( text[0:7] )
# print( text[8:13] ) ->bular kesib olish yani slicing
# []->index

# print( text[:7])
# print(text[8:])

text = "Kiber xavfsizlik"
print(text [0:16:2] )
print(text[0:16:3])

print(text[::2])
print(text [::-1])


