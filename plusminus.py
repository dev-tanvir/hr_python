
def plusMinus(arr):
    #
    # Write your code here.
    #
    z,p,n = 0,0,0
    for num in arr:
        if num < 0:
            n += 1
        elif num == 0:
            z += 1
        else:
            p += 1
    
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))
