class CheckEquality:

    comparision_string="abcd"


    @staticmethod
    def checkequality():
        
    
        

        input_string=input('enter input string : ')
      

        if input_string==CheckEquality.comparision_string:
            return True
        
        else:

            return False
        


Check=CheckEquality()

print(Check.checkequality())