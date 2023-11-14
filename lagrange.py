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


def txt_lagrange(x, y, variable, xformat=".2f", yformat="7.5f", one_row=False):
    """
    Returns the text representation of the Lagrange polynomial.
        x: x coordinates
        y: y coordinates
    """
    num = len(x)
    txt = ""

    rows = []
    for i in range(num):
        w1 = ""
        w2 = 1.
        for j in range(num):
            if i != j:
                w1 = w1 + f"({variable}-{x[j]:{xformat}})"
                w2 = w2 *(x[i]-x[j])
        c = y[i]/w2
        rows.append(f"{c:{yformat}} {w1}")
        
    line_break = "\n"
    if one_row:
        line_break = ""
    
    for i, r in enumerate(rows):
        if i > 0:
            if r[0] == "-":
                txt = txt + " - " + line_break + r[1:]
            else:
                txt = txt + " + " + line_break + r 
        else:
            txt = r
   
    return txt   
