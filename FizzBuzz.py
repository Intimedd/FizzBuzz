"""
for num in range(1, 101):
    is_fizz = num%3 == 0
    is_buzz = num%5 == 0
    if is_fizz and is_buzz:
        print("FizzBuzz")
    elif is_fizz:
        print("Fizz")
    elif is_buzz:
        print("Buzz")
    else:
        print(num)
"""
def Get_FizzBuzz(num):
    is_fizz = num%5 == 0
    is_buzz = num%10 == 0
    if is_fizz and is_buzz:
        return "FizzBuzz"
    elif is_fizz:
        return "Fizz"
    elif is_buzz:
        return "Buzz"
    else:
        return num

for num in range(1, 101):
    print(Get_FizzBuzz(num))