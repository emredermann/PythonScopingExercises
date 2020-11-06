def foo():
    global x
    x = 10
    print("in foo : ",x)
    def bar():
        nonlocal x
        x = 2
        print("in bar : ", x)
    bar()
    print("in foo after bar", x)

x = 7
foo()
print("End statement ",x)