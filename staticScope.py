def foo():
    x = 5
    def bar():
        global x
        x = 7
        print("in bar x is " + str(x))
    print("in foo x is " + str(x))
    bar()
    print("in foo x is "+str(x))

x = 3
print("in main x is "+ str(x))
foo()
print("in main x is "+ str(x))
