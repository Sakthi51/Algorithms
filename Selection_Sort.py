#pick the minimum value and sort to the left
#Have less numbers of swap than bubble sort

def selection_sort(list1):
    for i in range(len(list1)):
        min = i

        for j in range(i+1, len(list1)):
            if list1[j]<list1[min]:
                min = j

        if min != i:
            list1[min], list1[i] = list1[i], list1[min]

    return list1

list1 = list(map(int, input().strip().split()))
print(selection_sort(list1))
