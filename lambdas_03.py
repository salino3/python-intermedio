

sum_two_values = lambda first_value, second_value: first_value + second_value
  

print(sum_two_values(2,3))


multiply_values = lambda first_value, second_value: first_value * second_value - 3

print(multiply_values(20,3))

print('----------------------')



def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

def sum_three_values_modified(value):
    return sum_two_values(2, 8) + value

def sum_three_values_modified_again(value, first, second):
    return sum_two_values(first, second) + value



print(sum_three_values(5)(2, 4))

print(sum_three_values_modified(5))

print(sum_three_values_modified_again(20, 40, 5))
