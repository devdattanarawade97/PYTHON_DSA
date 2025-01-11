def kthLargestElement(list1:int, k:int)->int:
           
          list1.sort()
          return list1[-k]


print(kthLargestElement([1,2,3], 2))