def two_sum(listi, k):
    two_sum_nums = []
    for i in range(len(listi)):
        number = listi[i]
        for j in range(i+1, len(listi)):
            if number + listi[j] == k or number - listi[j] == k:
                two_sum_nums.append([number, listi[j]])
    
    return two_sum_nums




print(two_sum([4,7,1,-3,2], 4))