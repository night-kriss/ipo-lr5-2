#Создайте программу, которая принимает две строки и проверяет,
#являются ли они анаграммами (содержат одни и те же символы в разном порядке).
str1=str(input("Введите первую строку: "))
str2=str(input("Введиите вторую строку:"))
sorted_string1 = sorted(str1.lower())
sorted_string2 = sorted(str2.lower())
if sorted_string1 == sorted_string2:
    print("Да, это анаграммы.")
else:
    print("Нет, это не анаграммы.")
