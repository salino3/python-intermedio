
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


# def sum_two_values_and_add_value(first_value, second_value):
#     return sum_one(first_value + second_value)

def sum_two_values_and_add_value(first_value, second_value, fn):
    return fn(first_value + second_value)



print(sum_two_values_and_add_value(5, 2, sum_one))

print(sum_two_values_and_add_value(5, 2, sum_five))

print('------------------')

## Closures ##

def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten()

print(add_closure(5))

print('****************************')

##

def sum_ten_with_original_value(original_value):
    def add(value ):
        return value + 10 * original_value
    return add


add_closure = sum_ten_with_original_value(5)

print(add_closure(9))

print((sum_ten_with_original_value(5))(60))


result = sum_ten_with_original_value(5)(60)
print(result)

print('------------------')


def multiplier(factor):
    def print_this(factor):
        print("The factor value is " + str(factor))

    print_this(factor)

    def multiply(value):
        return value * factor
    return multiply

multiply_by_2 = multiplier(2)
multiply_by_5 = multiplier(5)

print(multiply_by_2(4)) 
print('Hello')
print(multiply_by_5(4))  

# Output: The factor value is 2
#         The factor value is 5
#         8
#         Hello
#         20


### Built-in Higher Order Functions ###

print('-----------------------')

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))


print(list(map(lambda number:number * 2, numbers)))

print('------------------')

# Filter

def filter_greater_than_ten(number):
    if(number > 10):
        return True
    return False
   

print(list(filter(filter_greater_than_ten, numbers)))

print(list(filter(lambda number: number > 10, numbers)))

print('-------------------')

# Reduce


def fn_sum_two_values(first, second):
        print(first)
        print(second)
        print('*')
        return first + second

# iterates with the accumulated value plus the next value
print(reduce(fn_sum_two_values, numbers))


