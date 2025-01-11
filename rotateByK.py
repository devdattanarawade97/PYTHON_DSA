

def rotateByK(list1:list[int], k:int)->list[int]:
       
       list1.reverse()
       list2=list(reversed(list1[:k]))+list( reversed(list1[k:]))
       return list2


print(rotateByK([1,2,3,4],2))




     