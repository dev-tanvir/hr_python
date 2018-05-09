#n = int(input())
arr = list(map(int, input().split()))

arr = set(sorted(arr))

print(arr)

arr.remove(max(arr))

print(arr)

print(max(arr))
