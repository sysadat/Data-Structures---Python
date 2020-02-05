#1.
def findMaxN(alist, size):
    maxN = 0
    for i in range (0,size):
        if alist[maxN] < alist[i]:
            maxN = i
    return maxN

def flipStack(alist, i):
    startPoint = 0
    while startPoint < i:
        alist[i], alist[startPoint] = alist[startPoint], alist[i]
        i = i - 1
        startPoint = startPoint + 1

def pancakeSort(alist):
    #1a. T(n) = 2(n - 1) - 1
    size = len(alist)
    while size >= 2:
        maxN = findMaxN(alist, size)
        if maxN != (size - 1):
            flipStack(alist, maxN)
            flipStack(alist, size - 1)
        size = size - 1

#Test Input
##alist = [5,1,3,2,6]
##pancakeSort(alist)
##print(alist)

#2.
def bubbleSort(anotherList):
    for num in range(len(anotherList)-1,0,-1):
        for i in range(num):
            if anotherList[i]>anotherList[i+1]:
                anotherList[i],anotherList[i+1] = anotherList[i+1], anotherList[i]

##Test input
##anotherList = [54,26,93,17,77,31,44,55,20]
##bubbleSort(anotherList)
##print(anotherList)

#3.
def findLeft(alist2, mid):
    newList = []
    counter = 0
    while counter < mid:
        newList.append(alist2[counter])
        counter += 1    
    return newList

def findRight(alist2, mid,length):
    newList2 = []
    counter = mid
    while counter < length:
        newList2.append(alist2[counter])
        counter += 1    
    return newList2

def mergeSort(alist2):
#    print("Splitting ",alist2)
    alist2Size = len(alist2)
    if len(alist2)>1:
        mid = len(alist2)//2
        lefthalf = findLeft(alist2, mid)
        righthalf = findRight(alist2, mid, alist2Size)

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist2[k]=lefthalf[i]
                i=i+1
            else:
                alist2[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist2[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist2[k]=righthalf[j]
            j=j+1
            k=k+1
#    print("Merging ",alist2)

#Test Input
##alist2 = [54,26,93,17,77,31,44,55,20]
##mergeSort(alist2)
##print(alist2)
