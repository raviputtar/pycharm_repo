def myfunct(a,b,c):

    if c=="sum":
        return(a+b)
    elif c=="mul":
        if a < 0 or b < 0:
            raise ValueError("a or b should be greater than 0")
        else:
            return(a*b)
    else:
        return(a-b)
