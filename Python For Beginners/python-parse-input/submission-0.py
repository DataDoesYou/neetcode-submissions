from typing import List

def read_integers() -> List[int]:
    my_list = input()
    string_list = my_list.split(",")
    number_list = []
    for s in string_list:
        number_list.append(int(s))
    return number_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
