#Bubble Sort
def BubbleSort(lst):
   
    lst = [54,45,6,78,3,9,3]
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    
    print("The Sorted List ==>",lst)    
BubbleSort([54,45,6,78,3,9,0])
