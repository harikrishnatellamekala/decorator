# reduce
# when ever u use reduce we must import 
from functools import reduce 
nums = [1,4,3,2]
# def fun(a,b):
#     return a+b
# print(reduce(fun , nums))
res = str(reduce(lambda a,b : a +b , nums))
print(type(res) , res)