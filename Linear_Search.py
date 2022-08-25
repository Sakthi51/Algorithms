def linearsearch(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return False


list = list(map(int, input().strip().split()))
n = int(input())
result = linearsearch(list, n)

print(list)
if linearsearch(list, n):
    print("Found at", result+1)
else:
    print("Not found")
