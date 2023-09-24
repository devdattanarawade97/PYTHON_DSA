#  problem statement- you are given two strings str1, str2. you have to tell whether strings are meta strings or not .
 #  meta strings are strings that are made equal by swapping exactly one pair of distinct char in the string.
# note - equal strings are not considered as meta string


class FindMetaString:

    def getAns(str1 , str2):
        status=False

        if str1==str2:
            return False
        
        dict1={}
        dict2={}
        count=1
        for char in str1:
           # print(char)
            if len(str1)==len(str2):
                  if dict1.get(char)==None :
                       dict1[char]=count
                  
                  else:
                       dict1[char]=dict1.get(char)+1
            
            else:
                 
                 return False
        
            
        for char in str2:
           # print(char)
            if len(str1)==len(str2):
                  if dict2.get(char)==None :
                       dict2[char]=count
                  
                  else:
                       dict2[char]=dict2.get(char)+1
            
            else:
                 
                 return False
        

        for keys in dict1:
             print(dict1.get(keys))
             print(dict2.get(keys))
             if dict1.get(keys)==dict2.get(keys):
                  status=True
             
             else:
                  return False

                  
                 
        return status
                
                
            
            

        # print(dict1)
         #print(dict2)

            
          


        
    

    print( getAns("Hello", "Hello"))
    print( getAns("Coding", "Coidng"))
    



    