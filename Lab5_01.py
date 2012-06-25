#Problem A

"""
def do(thing):
    return str(thing) + str(1)
print do(5)
"""
#Ans: the function takes in an aguement 'thing'
    # it converts thing into a string and then adds 1(which is a string)
    # to the end of the arguement and returns it, thus do(5) returns 51


#Problem B
"""
def do(one, two=5):
    return one+two
print do(5)
"""
#Ans : this fucntion takes one or two arguements
# depending on how many arguements are passed to the function
# if the only one arguement is passed to the function the value is added to 5(default)
# thus 10 is returned.


# Problem C
"""
def do(a,b):
    a=5
    b=5
    return a*b
inp = 8
do(inp,5)
print inp
"""
# the value printed is the value of imp which is 8
#this is because whatever the operation that goes on in the function
#does not change the value of the variable inp

# Problem D
"""
def try_to_change_list_contents(the_list):
    the_list.append('four')
outer_list = ['one', 'two', 'three']

try_to_change_list_contents(outer_list)
print outer_list
"""
# this is a function to append the string 'four' to a list
# the variable outer_list is a list containing the following string elements 'One'....
# the output is ['one','two',''tree','four']

# Problem E
"""
def do(a, f):
    return a*f(a)
def inp(a):
    return a*2

print do(6,inp)
"""
#the output is 72


