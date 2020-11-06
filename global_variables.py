day  ="monday"
def calendar():
    global day
    print("global day is " ,day)
    day = "Tuesday"
    print("global day is ", day)
def c():
    print("day in c is ", day)
calendar()
c()