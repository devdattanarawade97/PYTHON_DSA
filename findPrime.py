

class FindPrimeNumber:



    def findPrime():


        givenNumber=int(input('pls enter number : '))

        
        for number in range(2,givenNumber):

            if givenNumber%number==0:

                print(f'number is not prime {givenNumber}')

                break

        else:

            print(f'given number is prime {givenNumber}')


    
    findPrime()