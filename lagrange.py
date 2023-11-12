def lagrange(x, y, xp):
    """
    Computes value of the Lagrange polynomial at position xp.
        x: x coordinates
        y: y coordinates
        xp: sampling point in x
    """
    num = len(x)
    r = 0

    for i in range(num):
        w1 = 1.
        w2 = 1.
        for j in range(num):
            if i != j:
                w1 = w1 * (xp-x[j])
                w2 = w2 *(x[i]-x[j])
        r += y[i]*w1/w2
    return r   


def print_lagrange(x, y):
    """
    Computes value of the Lagrange polynomial at position xp.
        x: x coordinates
        y: y coordinates
        xp: sampling point in x
    """
    num = len(x)
    r = ""

    for i in range(num):
        w1 = ""
        w2 = 1.
        for j in range(num):
            if i != j:
                w1 = w1 + f"(x-{x[j]:.3f})"
                w2 = w2 *(x[i]-x[j])
        r = r + f"{y[i]:.3f}*{w1}/{w2:.3f}+\n"
    return r   


def coeff(x, y):
    """
    Determines a b c coefficients for 
    quadratic Lagrange polynomial: 
    f(x) = ax^2 + bx + c
    """
    A = y[0]/((x[0]-x[1])*(x[0]-x[2]))
    B = y[1]/((x[1]-x[0])*(x[1]-x[2]))
    C = y[2]/((x[2]-x[0])*(x[2]-x[1]))  
    a = A + B + C
    b = -(A*(x[1]+x[2]) + B*(x[0]+x[2]) + C*(x[0]+x[1]))
    c = (A*x[1]*x[2]) + (B*x[0]*x[2]) + (C*(x[0]*x[1]))
    return a,b,c

