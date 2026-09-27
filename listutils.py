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
        
         
        
        
    
