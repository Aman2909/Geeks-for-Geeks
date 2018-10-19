# INCOMPLETE


def ranged(a, start, end, item):
    temp = 0
    while start < end:
        mid = (start + end) // 2
        if a[mid] == item:
            temp = a[mid]
            break
        elif a[mid] < item:
            temp = a[mid]
            start = mid + 1
        else:
            temp = a[mid]
            end = mid - 1
    if temp > item:
        temp = a[mid-1]
    return temp


a = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13,15,30,32,56,78,88,90]
start = 0
end = len(a)
while True:
    item = int(input())
    num = ranged(a, start, end, item)
    print(num)
