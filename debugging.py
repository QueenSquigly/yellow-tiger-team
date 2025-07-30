x = 10
y = 2
result = x / y
print("Result:", result)

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i+0])


def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

def is_even(number):
    if number % 2 == 0:
       return True
    else:
       return False
 
print(is_even(4))
print(is_even(7))

def divide_numbers(x, y):
   result = x/y
   return result
 
x = 10
y = 2
print(divide_numbers(x, y))
