from sys import argv

script, filename = argv


def merge_sort(values_list):  # assumes no duplicates
    l = len(values_list)

    if l <= 1:
        return values_list

    first_half = merge_sort(values_list[:l/2])
    second_half = merge_sort(values_list[l/2:])

    return merge_lists(first_half, second_half)


def merge_lists(list1, list2):
    merged_list = []
    global count_inversions

    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
            count_inversions += len(list1)

    if list1:
        merged_list.extend(list1)
    elif list2:
        merged_list.extend(list2)

    return merged_list


count_inversions = 0

# list1 = [1, 2]
# list2 = [5, 6, 8]

# print merge_lists(list1, list2)

# list3 = [1, 2, 3, 4, 5, 6]

txt = open(filename)

# run through file to get out all the numbers in the list
num_list = []
for line in txt:
    line = line.rstrip('\n')
    num_list.append(int(line))

txt.close()


print merge_sort(num_list)
print count_inversions