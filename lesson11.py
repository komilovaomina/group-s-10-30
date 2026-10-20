"""
08.10.2026
Mavzu:
    -String methodlar
    -Join,split,

"""

# products = ["guruch", "go'sht", "piyoz"]

# # "Men bugun bozordan:guruch,go'sht,piyoz olishim kerak."
# t1 = ",".join(products)

# text = f"Men bugun bozordan: {t1} olishim kerak"
# print(text)

# message= "1 2 3 4 5 6 7 8 9"
# print(message.split())
#split- matndagi sozlarni ajratib alohida-alohida yozib beradigan funksiya

#Agar sozlarni ortasida vergul bolsa,split ichida(,)beriladi.Misol:
message = "1,2,3,4,5,6,7,8,"
print(message.split(","))

#startwith-bu sozni boshlanishini tekshirib beradigan funksiya.Printga chiqarsak,true yoki false chiqarib beradi

# name1= "name_Jamshid"
# name2= "name_Navro'z"
# age1= "age_25"

# print(name1.startswith("name"))
# print(name2.startswith("name"))
# print(age1.startswith("name"))

#endswith()- bu matnni oxirgi sozini tekshirib beradigan funksiya.True yoki false  boladi

# print("Hello world".endswith("age")) #True,#False

# message = "Assalomu alaykum,Telegram Botga xush kelibsiz."
# message2 = message.lower()
# count_a = message2.count("a")
# count_a = message.lower().count("a")
# message_length = len(message)#->bu sozda nechta belgi borligini aniqlab beradi
# text = f"A harfi messageda: {count_a}/{message_length}."
# print(text)
