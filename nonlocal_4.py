x = 7
def level1():
    x = 1
    def level2():
        y = 2
        def level3():
            global x                # change it to the nonlocal to observe the difference
            x = 3
            print("level 3 x = {} y = {}".format(x,y))
        level3()
        print("level 2 x = {} y = {}".format(x, y))
    level2()
    print("level 1 x = {}".format(x))

level1()
print("x is ", x)