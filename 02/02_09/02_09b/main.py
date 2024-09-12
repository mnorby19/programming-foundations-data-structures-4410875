def find_second_smallest(my_list):
    if len(my_list) <= 1:
        return None
    sorted_list = sorted(my_list, reverse = False)
    return sorted_list[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([]))
print(find_second_smallest([2]))