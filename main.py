
user_input = int(input("Введіть число: "))

if is_power_of_four(user_input):
    print(f"{user_input} є ступенем 4.")
else:
    print(f"{user_input} не є ступенем 4.")

from untils.py import check_even_add
num = 72
result = check_even_odd(num)
print(f"{num} - {result})

num = int(input("Введіть число: "))
result = check_even_odd(num)
print(f"{num} - {result}.")
