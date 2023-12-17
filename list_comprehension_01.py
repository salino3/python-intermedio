
# my_original_list = [35, 24, 62, 52, 30, 17, 30]
my_original_list = [0,1, 2, 3, 4, 5, 6, 7]

# first 'i' variable of iteration of every list value; second 'i' is the value  that includes in the new list
my_list = [i for i in range(7)]
my_other_list = my_original_list
my_range = range(8)

print(my_list)

print(my_other_list)

print(my_range)
print(list(my_range))


print('----------------')


my_list = [i + 1 if i <= 0 else i for i in range(8)]


print(my_list)

my_list = [i * 2 if i >= 0 else 0 for i in range(8)]

print(my_list)

my_list = [i * i for i in range(8)]

print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]

print(my_list)

