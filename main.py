from utils.py import is_power_of_four
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


from utils.py import find_gcd
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

gcd = find_gcd(num1, num2)

print(f"НСД({num1}, {num2}) = {gcd}")

    
from utils.py import unique_n

a, b = map(int, input().split())
result = [str(num) for num in range(a, b + 1) if unique_n(num)]

print(*result)
