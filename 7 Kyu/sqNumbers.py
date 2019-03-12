# marzo 12, 2019 

def is_square(n):   
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        return n%n**0.5==0
