def main():
    email = input('Enter your email: ')
    
    ########################################
    if email[0].isalpha():
        print("True")
    else:
        print("False")
    
    if 5 < len(email) < 30:
        print("True")
    else:
        print("False")
    
    if email.find('@') == -1 or email.find('. after @') == -1:
        print("False")
    else:
        print("True")

    

    ########################################
    
    result = True

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
