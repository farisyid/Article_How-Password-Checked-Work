# Password checking
while True:
    x=input('Please Input Your Password : ')
    L=''
    U=''
    D=''
    S=''
    for i in x:
        if i.isalpha():
            if i.isupper():
                U+=i
            else :
                L+=i
        elif i.isdigit():
            D+=i
        else:
            S+=i
    l=int(len(L))
    u=int(len(U))
    d=int(len(D))
    s=int(len(S))

    if l>0 and u>0 and d>0 and s>0:
        print(f'Your Password "{x}" is VERY STRONG')
        print('Press Continue')
        break
    elif l>0 and u>0 and d>0 and s==0:
        print('Your Password is STRONG \nYou Need More Strong Password')
    elif l>0 and u>0 and d==0 and s>0:
        print('Your Password is STRONG \nYou Need More Strong Password')
    elif l>0 and u==0 and d>0 and s>0:
        print('Your Password is STRONG \nYou Need More Strong Password')
    elif l==0 and u>0 and d>0 and s>0:
        print('Your Password is STRONG \nYou Need More Strong Password')
    elif l>0 and u>0 and d==0 and s==0:
        print('Your Password is WEAK \nYou Need More Strong Password') 
    elif l==0 and u>0 and d>0 and s==0:
        print('Your Password is WEAK \nYou Need More Strong Password') 
    elif l==0 and u>0 and d==0 and s>0:
        print('Your Password is TOO WEAK \nYou Need More Strong Password')
    elif l==0 and u>0 and d==0 and s==0:
        print('Your Password is TOO WEAK \nYou Need More Strong Password') 
    elif l>0 and u==0 and d==0 and s==0:
        print('Your Password is TOO WEAK \nYou Need More Strong Password')