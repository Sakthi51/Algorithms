#First element is already sorted, so start from index 1
#It is slightly faster than bubble sort and selection sort in some time
#It is like playing cards

def insertion_sort(list_1):
    for i in range(1, len(list_1)):
        value_to_sort = list_1[i]

        while list_1[i-1]>=list_1[i] and i>0:
            list_1[i-1], list_1[i] = list_1[i], list_1[i-1]
            i = i - 1

    return list_1

list_1 = list(map(int, input().strip().split()))
insertion_sort(list_1)
print(list_1)
