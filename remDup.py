def remDup(arr):
    ar = []
    dup_arr = []
    unique = []
    for i in range(len(arr)):
        if arr[i] in ar:
            dup_arr.append(arr[i])
            pass
        else:
            ar.append(arr[i])

    for i in range(len(ar)):
        if ar[i] in dup_arr:
            pass
        else:
            unique.append(ar[i])

    return unique



a = [4,3,2,4,1,3,2,9] 

print(remDup(a))