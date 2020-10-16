# quick sort
list1 = [12,18,15,21,19,30,4,17, 30,17]
N = 0
def sort(listN,startP,endP,N):
    print()
    
    print("listN", listN)
    # print("startP", startP)
    # print("endP", endP)
    print("sorting")

    privote = listN[endP]
    print("privote:", privote)

    smallL = []
    bigL = []
    for item in listN[startP:endP]:
        if item <= privote:
            smallL.append(item)
        if item > privote:
            bigL.append(item)
    
    
    partList = smallL
    partList.append(privote)
    # partList = partList + bigL
    partList.extend(bigL)
    print("partList", partList)

    endList = listN
    endList[startP:endP+1] = partList
    print("end list", endList)

    if len(smallL) > 1:
        N+=1
        print("smallL",smallL)
        print("N",N)
        sort(endList,startP,startP + len(smallL) - 2,N)
    if len(bigL) > 1:
        N+=1
        print("bigL",bigL)
        print("N",N)
        sort(endList,endP - len(bigL),endP,N)

    return endList

ans = sort(list1,0,len(list1)-1,0)
print("=============", ans, "=============")