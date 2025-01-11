def findMissingNum(nums:list[int]  )->int:
        
        nums.sort()

        for i in range(nums[-1]):
            

            if i not in nums and i!=0:
                  return i

print(findMissingNum([1,2,4]))