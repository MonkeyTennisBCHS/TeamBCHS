import sys
def SignUp():
    Name=str(input('Full Name:'))
    DOB=str(input('Enter your Date of Birth(type like this- ddmmyyyy):'))
    Artist=str(input('Do you accept our terms of service?:'))
    if Artist == 'no' or Artist == 'No':
        print('Sorry')
        sys.exit(3)
    elif Artist == 'Yes' or Artist == 'yes':
        Genre=str(input('What would you like to achieve with monkey tennis?:'))
        Password=str(input('Type a password:'))
        writefile=open('OCR.csv','a')
        writefile.write(Name+','+DOB+','+Artist+','+Genre+','+Password+','+'\n')
        writefile.close()
        LOGIN=input('Ok you are now a member\nPlease type LOGIN to log into the account:')
    if LOGIN=='LOGIN':
        print('Name:',Name)
        pass2=str(input('Enter Password:'))
        if pass2==Password:
            print('Access Granted')
        else:
            print('Access Denied')
            sys.exit()
def Login():
    with open('OCR.csv','r') as Member:
        User=Member.read()
        MemberName=str(input('Full Name:'))
        if MemberName in User:
                LOGIN=input('Please type LOGIN to log into the account:')
                if LOGIN=='LOGIN':
                    print('Name:',MemberName)
                    pass2=str(input('Enter Password:'))
                    if pass2==Password:
                        print('Access Granted')
                    else:
                        print('Access Denied')
                        sys.exit()
                else:
                    sys.exit()
        else:
            print('You are not a member, we will sign you up')
            SignUp()


print('Welcome to MonkeytennisBchs')
User=str(input('Are you already a user?'))
if User == 'yes':
    Login()
    

else:
    SignUp()




    

