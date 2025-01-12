def findAllDuplicates(nums: list[int]) -> list[int]:
         
            list1={}
            for eachNum in nums :
                  list1[eachNum]=list1.get(eachNum,0)+1
            print(list1)
            list2=[]
            for eachNum, value in list1.items():
                  print(eachNum)
                  if value>1:
                       list2.append(eachNum)

            return list2

print(findAllDuplicates([1,2,2,3]))
                      