# higher order functions
# pass a fun as a parameter to the another fun if u want u can change it 
# a = int(input("enter a: "))
# b = int(input("enter b: "))

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def operate(a,b,operation):
#     return operation(a,b)

# print(operate(a,b,add))
# print(operate(a,b,sub))
# print(operate(a,b,mul))
# print(operate(a,b,div))

# what if i pass a list or arr

list =  set(map(int, input("enter list item:").split()))
def square(item):
    return item * item
def cube(item):
    return item * item * item

def dec(list,operation):
    for i in list:
        print(operation(i))

dec(list,square)
dec(list,cube)