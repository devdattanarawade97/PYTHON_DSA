
def check_Palindrome():

    input_val=input('enter number : ')

    reversed_input=input_val[::-1]

    if input_val==reversed_input:
        return True

    else:

        return False

    


print(check_Palindrome())

