"""
Sana: 10.10.2026
Mavzu:
   -Mantiqiy ma'lumot turlari
   -True false qiymatlar
   -and, or , not
   -bool()funksiyasi
   -Mantiqiy masalalar
"""

#bool faqat 2ta qiymatni oz ichiga oladi:True yoki false

x = True
y = False

print(f"{x=}) : {type(x) = }")
print(f"{y=} ; {type(y)=}")

"""
>(katta),
<(kichik),
>= -(katta yoki kichik)
<= - (kichik yoki teng)
== - (tngmi)
!= - (teng emasmi)

"""

a = 10
b = 7
c = a == b
print(f"{c =}")


# agar or ishlatilganda 1tasi true bolsa natija true boladi.Ammo agar 2lasi ham false bolsa unda false boladi
# And ishlatilganda faqatgina 2lasi true bolsagina true boladi

print("and ga bog'liq holatlar:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"True and False = {False and False}")

print('\n===========\n')

print("or ga bog'liq holatlar:")
print(f"True or True = {True or True}")
print(f"True or True = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")


y = 5 > 3 and 4 < 9
print(f"{y =}")

res =( (2 == 2.0) or (5 > 100))
print(f"{res =}")

z = "salom" == "Salom" or 5.45 / 5 == 1.09
print(f"{z =}")

r1 = 41 
res = r1 % 5 ==1
print(f"{res =}")

s1 = 8 * 3 
s2 = 12 * 2
res = s1 + s2 == 2 * s1 and s1 // s2 ==1
print(f"{res=}")

#Masala #1
a = int (input("a ="))
b = a > 0
print(b)

#Masala #2
a = int(input("a ="))
result = (a % 2 == 1)
print(f"{result =}")
        



