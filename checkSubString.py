
class stringContainsSubstring:

  def check(self):


    completeString=input('pls enter complete string : ')
    substring=input('pls enter complete substring : ')

    if(substring in completeString):

      return True

    else:
      return False

    


to=stringContainsSubstring()

print(to.check())


