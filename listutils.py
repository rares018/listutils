#listutils

def combine(*args): #mathematical reunion (A U B)
    combined = []
    for i in args:
        for e in i:
            if e in combined:
                pass
            else:
                combined.append(e)
    
    return combined


def pick(arg1,arg2): #picks only the args that are also in arg2.similar to 'intersection' in math.
    new = []
    for i in arg1:
        if i in arg2:
            new.append(i)
        else:
            pass
    return new


def excepting(arg1,arg2):  #is like in x86 ANDN and in math A\B
    new = []
    for i in arg1:
        if i in arg2:
            pass
        else:
            new.append(i)
    return new

def symmetry(arg1,arg2):
    new = []
    
    for i in combine(excepting(arg1,arg2),excepting(arg2,arg1)):  #(A\B)U(B\A)
        new.append(i)
    return new

def is_subset(arg1,arg2):  #returns True if all the values in arg1 are also in arg2 else,returns False
    all_in = True
    for i in arg1:
        if i in arg2:
            pass
        else:
            all_in = False
    
    return all_in

def divs(arg1):   #this one takes intigers,not lists
    new = []
    num = 1
    while num <= arg1:
        if arg1%num == 0:
            new.append(num)
        else:
            pass
        num += 1
    
    return new

def is_prime(arg1): #needs an int and returns a boolean
    if arg1 != 1 and divs(arg1) == [1,arg1]:  #NOTE:even if 1 and 0 are mathematically not prime numbers,nor are they composite,if you try this function with 1 or 0,it will return False
        return True
    else:
        return False
    
def is_element(arg1,arg2): #arg1:var arg2:list and returns a boolean
    is_it = False
    for i in arg2:
        if arg1 == i:
            is_it = True
        else:
            pass
        
    return is_it  #is_it means 'is it an element of the list?'

def bcd(arg1,arg2): #bcd stands for 'biggest common divider' also arg1 and arg2 are vars
    return max(pick(divs(arg1),divs(arg2)))


def sqr(arg1): #sqr means 'square root'
    x = 0
    x = arg1 ** 0.5
    
    return x


def issqr(arg1,arg2): #returnes True if the square root of arg1 is arg2 else,returns False
    sqroot = sqr(arg1)  #also,if you need the square root of a non perfect square number,do issqr(foo,int(bar))
    if sqroot == arg2:
        return True
    else:
        return False
    
        
        
    
