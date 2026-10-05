# decorator
# a fun pass an parameter to anotehr fun it is called , 
# a fun can retrurn a another fun
# a function can crearte a another fun
# if i want to access the inner fun in outside the outer methods i need to return thr iner

# why we need decorator 
# if my requirement is i want to change a fun according to my requirements
# with out changing the method , if i changed the method who the people are using this 
# method they got probelm , so i can change this indirectly 

# ex: in india especially marriage we are going to decorate our houses with lights
# we are not going to reconstruct the entiare home but we are just change the external things
# decoration that it the beauty

def outer(ref):

    def wrapper(a,b):
        if b == 0:
            print("enter positive num")
        else:
            ref(a,b)
    return wrapper


@outer # we are decorating or wrapping the main code
def div(a,b):
    print(a/b)

# res = outer(div)
# res(19,162)
# res(1,0)

#res = outer(div)
div(19,162)
div(1,0)