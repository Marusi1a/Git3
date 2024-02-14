from utils.py import is_power_of_four
user_input = int(input("Введіть число: "))

if is_power_of_four(user_input):
    print(f"{user_input} є ступенем 4.")
else:
    print(f"{user_input} не є ступенем 4.")
