def add_two_numbers() -> int:
    my_string = input()
    my_string_list = my_string.split(",")
    my_int_list = []
    for s in my_string_list:
        my_int_list.append(int(s))
    return (my_int_list[0] + my_int_list[1])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
