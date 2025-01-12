def isAnagram(s1:str, s2:str)->bool:
       
          s1Dictionary={}
          s2Dictionary={}
          for char in s1:
              s1Dictionary[char]= s1Dictionary.get(char,0)+1
          for char in s2:
              s2Dictionary[char]= s2Dictionary.get(char, 0)+1

          return s1Dictionary==s2Dictionary

print(isAnagram("anagram","rat"))