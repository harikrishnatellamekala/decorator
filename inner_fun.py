# inner function
def outer():
    print("in outer fun")

    def inner():
        print("in inner fun")
    inner()

outer() # calling a inner to outer 
# if i want to return inner as outer
def outer():
    print("in outer fun")

    def inner():
        print("in inner fun")
    return inner()

outer()