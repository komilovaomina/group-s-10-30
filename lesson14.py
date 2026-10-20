"""
Sana:15.10.2026
Mavzu:
    -List(ro'yhatlar bilan ishlash)
    -List(index)
    -List slicing
    


"""
#Masala #11
# a =int (input("a="))
# b =int (input("b="))
# result=a % 2 == 1 and b % 2 == 1 or a % 2 ==0 and b % 2 == 0
# # print(f"{result=}")

# #Masala #14
# a =int (input("a="))
# b =int (input("b="))
# c =int (input("c="))
# res1 = a > 0 and b < 0 and c < 0
# res2 = b > 0 and a < 0 and c < 0
# res3 = c > 0 and a < 0 and b < 0
# result = res1 or res2 or res3
# print(f"{result=}")

# x = [1 , 2, 3, 4, 5]
# print(f"{"x ="}")
# print(type(x))

# sonlar = [1, 2, 3, 4, 5]
# harflar =['a' , 'b', 'c']
# mevalar = ['olma', 'anor', 'nok']
# cars = ['cobalt' , 'gentra', 'malibu']

# print(f"{sonlar =}")
# print(f"{harflar =}")
# print(f"{mevalar=}")
# print(f"{cars =}")


# #Listni ichida elementlar boladi va bu elementlarni tartib raqami yani indeksi boladi.Oxirgi elementni -1 orqali topsak boladi
#royhatni teskari qilish uchun ::-1 qilib yozamiz
# x = []  #bosh royhat
# print(f"{x =}")

# yillar = [ 1991, 1992, 1993, 1994, 1995, 1996, 2000] #tartib raqam-index

# a = yillar [3] 
# print(f"{a =}")

# b = yillar [0]
# print(f"{b =}")

# c = yillar [4]
# print(f"{c =}")

yillar = [ 1991, 1992, 1993, 1994, 1995, 1996, 2000]

x = yillar[1:6]
print(f"{x =}")
# 94dan 20
x = yillar[4:]
print(f"{x =}")

yillar_teskari =yillar [::-1]
print(f"{yillar_teskari =}")












































