
def list_examples():
    # Lists can have sub-lists
    list_in_list = [['Vikram', 19], ['Peter', 20]]
    # You can add multiple types in a list
    multiple_types = ["2B", "2B"]

    # Put different lists together
    zipped_list = zip(list_in_list, multiple_types)

    # Printing a zipped list
    print(list(zipped_list))

    # Empty list
    my_empty_list = []

    # Can be filled later using two methods
    # 1. Append: Add a value to the list.
    #    If list is !empty, add value at end
    my_empty_list.append(1)
    my_empty_list.append(1920)

    #2. Grow (+): use + to add multiple things in []
    #     to a list at once. + can only be used 
    #     when you equate it to another list
    growing_list = my_empty_list + [4, 5, 6]

    
    # Range: put numbers in lists (zero to number - 1)
    # Below returns a range object with 0 - 9
    my_range = range(10)

    # Range of two values, 2 - 9
    my_range_two = range(2, 10)

    # Range skip numbers, 1, 11, 21, .. , 91 (each number is 10 greater than previous)
    my_range_three = range(1, 100, 10)

    # convert it into a list
    my_range_list = list(my_range)

def append_sum(lst):
    result = lst[-1] + lst[-2]
    lst.append(result)
    result2 = lst[-1] + lst[-2]
    lst.append(result2)
    result3 = lst[-1] + lst[-2]
    lst.append(result3)
    return lst

def larger_list(lst1, lst2):
    if (len(lst1) > len(lst2)):
        return lst1[-1]
    elif (len(lst2) > len(lst1)):
        return lst2[-1]
    else:
        return lst1[-1]

def more_than_n(lst, item, n):
    return (n < lst.count(item))

def append_size(lst):
    lst.append(len(lst))
    return lst

def combine_sort(lst1, lst2):
    zipped_list = lst1 + lst2
    zipped_list.sort()
    return zipped_list

def every_three_nums(start):
    return list(range(start, 101, 3))

def remove_middle(lst, start, end):
    lst1 = lst[0:start]
    lst2 = lst[end + 1:]
    return lst1 + lst2

def more_frequent_item(lst, item1, item2):
    if (lst.count(item1) > lst.count(item2)):
        return item1
    elif (lst.count(item2) > lst.count(item1)):
        return item2
    else:
        return item1

def double_index(lst, index):
    if (index >= len(lst)):
        return lst
    lst2 = lst
    lst2[index] = lst[index] * 2
    return 

def middle_element(lst):
    if (len(lst) % 2 != 0):
        return lst[int(len(lst) / 2)]
    else:
        return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2

# Tuples:
#         Are like lists, but they
#         cannot be appended/changed
#         after they are initialized

# Use () to specify a tuple. Remember
# it cannot be changed afterwards
my_tuple = ("Vikram", 19, "Student")

# One element tuple needs to have a 
# trailing comma or python will think of
# it as an expression.
one_element_tuple = (4, )