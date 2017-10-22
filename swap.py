x=23
y=45
# python can not swap values of variable. in order to do so, we create another storage for the variable (z).
if x<y:
    z=y
    y=x
    x=z
    print x,y

