def find_second_smallest(my_list):
    return 0


def find_second_smallest_v2(my_list):
    if len(my_list) <= 1:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
 
    for item in my_list:
        if item < smallest:
            second_smallest=smallest
            smallest=item
        elif item < second_smallest:
            second_smallest = item
    return second_smallest

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))
