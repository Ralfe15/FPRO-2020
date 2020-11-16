def mastermind(g1, g2, g3, c1, c2, c3):
    g_colors = g1+g2+g3
    c_colors = c1+c2+c3
    c_colors_control = c_colors
    res = 0
    ind = 0
    for i in g_colors:
        if c_colors[ind] == i:
            res +=3
            ind+=1          
        elif i in c_colors_control:
            res += 1
            c_colors_control = c_colors_control.replace(i,"")
            ind+=1
        else:
            ind+=1
    return(res)