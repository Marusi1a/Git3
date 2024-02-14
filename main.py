
user_input = int(input("Введіть число: "))

if is_power_of_four(user_input):
    print(f"{user_input} є ступенем 4.")
else:
    print(f"{user_input} не є ступенем 4.")
    
from utils.py import unique_n

a, b = map(int, input().split())
result = [str(num) for num in range(a, b + 1) if unique_n(num)]

print(*result)
