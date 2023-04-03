def sum_list(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list)) 
