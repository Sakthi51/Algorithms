#if the value is smaller, change higher bound and mid value becomes new upper value.
#if the value is bigger, change lower bound and mid value becomes new lower value.

def binarysearch(list, n):
    lower = 0
    upper = len(list)-1
    for i in range(len(list)):
        mid = (lower + upper) // 2
        if list[mid] == n:
            return mid
        else:
            if list[mid] < n:
                lower = mid+1
            else:
                upper = mid-1


list = sorted(list(map(int, input().strip().split())))
n = int(input())
result = binarysearch(list, n)

print(list)
if binarysearch(list, n):
    print("Found at", result+1)
else:
    print("Not found")
    
   
