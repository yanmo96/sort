# Merge Sort
list1 = [12,18,15,21,19,30,4,17, 30,17,2]

def merge(left, right):
    result = []
    l_i, r_i = 0, 0
    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            result.append(left[l_i])
            l_i+=1
        else:
            result.append(right[r_i])
            r_i+=1
    result.extend(left[l_i:])
    result.extend(right[r_i:])
    return result

def merge_sort(listN):
    if len(listN) <= 1:
        return listN
    middle = len(listN)//2
    left = listN[:middle]
    right = listN[middle:]
    print("left: ", left)
    print("right:", right)
    print()
    
    left = merge_sort(left)
    right = merge_sort(right)
    end = merge(left,right)
    return end

ans = merge_sort(list1)
print(ans)
