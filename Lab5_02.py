# Problem 2
"""
def factorial(num):
    value =1
    print ' the factorial of',num,'is' 
    for n in range (1,num+1,1):
        value = value*n
    return value

print factorial(5)
print factorial(4)
print factorial(6)

"""

#Problem 3
"""
def fibonacci(num):
    print'the fibonacci sequence for',num,'is: '
    value = 0
    new_num = 1
    old_num = 0
    fibo_list=[]
    for n in range (0,num,1):
        value = old_num + new_num
        old_num= new_num
        new_num= value
        fibo_list.append(value)
        print value,
    print
    return fibo_list

#fibonacci(7)
print fibonacci(6)
"""

#Problem 4
"""
def prime(num):
    divisor_count = 0
  
    for n in range(1,num+1,1):
        if num%n ==0:
            divisor_count= divisor_count + 1
            
    if divisor_count == 2:
        return True
    
    else:
        return False
"""




