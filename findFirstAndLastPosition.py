def findFirstAndLastPosition(nums:list[int], k:int)->list[int]:
         newList=[]
         for i in range(len(nums)):
             num=nums[i]
             if num==k:
                   newList.append(i+1)
                   break
               
         
         nums.reverse()
         for i in range(len(nums)):
             print(i)
             num=nums[i]
             if num==k:
                   newList.append(len(nums)-(i))
                   break
         
         return newList


print(findFirstAndLastPosition([1,2,3,4,4,5], 4))

         
          
