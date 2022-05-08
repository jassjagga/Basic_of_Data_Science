tom_exp_list= [2100,3400,3500]
joe_exp_list= [200,500,700]

#if we need total without fucntion
total=0
for item in tom_exp_list:
    total=total+item
print("Tom's total expenses:",total)

total=0
for item in joe_exp_list:
    total=total+item
print("Joe's total expenses:",total)

#with function the same code

#function to calculate the total
def calculate_total(exp):
    total =0
    for item in exp:
        total=total+item
    return total

tom_exp_list= [2100,3400,3500]
joe_exp_list= [200,500,700]

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)

print("Tom's total=",toms_total)
print("Joe's Total=",joes_total)

#other Example of fucntion to sum two numbers
def sum(a,b=0):     #b=0 is the default arguments means if second arguments not passed program still run
    """
    This function takes two arguments which are itnerger numbers and
    it will return sum of them as an output
    :param a:
    :param b:
    :return:
    """
    total= a+b
    return total
#here we are passing the argument by position there are two types named and position arguments
#in name arugments we pass the arguments by Name of the arugments and order does'nt matter
n=sum(5,6)
print("total is :",n)

#Global and local variable in python
#variable work in its scope means variable define in side function can't work outside the function
#varible define ouside the funcition will work anywhere in the program


# Document Strings to document see on the top