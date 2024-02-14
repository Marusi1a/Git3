
def is_power_of_four(number):
    if number <= 0:
        return False
    if (number & (number - 1)) != 0:
        return False
    return (number - 1) % 3 == 0

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def unique_n(num):
    num_str = str(num)
    unique = []
    for i in num_str:
        if i not in unique:
            unique.append(i)
    return len(unique) == 4

def check_even_odd(number):
    if number % 2 == 0:
        return "Парне число"
    else:
        return "Непарне число"
