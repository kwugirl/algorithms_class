from sys import argv

script, filename = argv

txt = open(filename)

# run through file to get out all the numbers in the list
num_list = []
for line in txt:
    line = line.rstrip('\n')
    num_list.append(int(line))

txt.close()

count_comparisons = 0


def quicksort(num_list):
    if len(num_list) <= 1:
        return num_list

    # index_pivot = 0  # choosing first element as pivot
    # index_pivot = -1  # choosing last element as pivot
    index_pivot = choose_pivot(num_list)
    pivot = num_list[index_pivot]

    partition(num_list, index_pivot)

    global count_comparisons
    count_comparisons += len(num_list)-1

    new_pivot_index = num_list.index(pivot)

    num_list[0:new_pivot_index] = quicksort(num_list[0:new_pivot_index])  # sort left half

    if new_pivot_index < len(num_list)-1:  # check that new pivot isn't at end
        num_list[new_pivot_index+1:] = quicksort(num_list[new_pivot_index+1:])  # sort right half

    return num_list


def partition(num_list, index_pivot):
    pivot = num_list[index_pivot]

    # move pivot to beginning of array, swap with first element
    temp = num_list[0]
    num_list[0] = pivot
    num_list[index_pivot] = temp

    i = 1

    for j in range(1, len(num_list)):
        if num_list[j] < pivot:  # if find a number that should go to the left of pivot
            temp = num_list[j]
            num_list[j] = num_list[i]
            num_list[i] = temp
            i += 1

    # swap last of numbers on the left side of pivot with pivot stored at beginning of list
    temp = num_list[i-1]
    num_list[i-1] = num_list[0]
    num_list[0] = temp

    return num_list


def choose_pivot(num_list):
    first = num_list[0]
    mid = num_list[(len(num_list)-1)/2]  # get to kth element even if 2k
    last = num_list[-1]

    values = [first, mid, last]
    values.sort()

    return num_list.index(values[1])


quicksort(num_list)
print num_list
print count_comparisons
