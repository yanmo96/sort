# Bubble sort
list1 = [12,18,15,21,19,30,4,17, 30,17]

def sort(listN):
    for i in range(len(listN)-1):
        for j in range(i,len(listN)-1):
            print("i",i, "j",j)
            if listN[j] > listN[j+1]:
                listN[j],listN[j+1]= listN[j+1],listN[j]
    return listN

ans = sort(list1)
print("ans", ans)