x=input("Enter number1 :")
y=input('Enter number2 :')
#if we forgot to execption like int when we enter the number
try:                #to handle the exception in the program
    #z=x/int(y)
    z=int(x)/int(y) #instead of stoping the program here we handle it
#below line is to handle any genric exception
#except Exception as e:
#To handle spicific exception like in this case we use zerodivisionError
except ZeroDivisionError as e:
    print("Divison by ZERO EXCEPTION")
    z= None
#To find out which exception error is this
#'''except Exception as e:
#    print('exception type:',type(e).__name__)
#    z=None '''
#after finding out the error type
except TypeError as e:
    print("Type error exception")
    z=None
print("Division is:", z)
