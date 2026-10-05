# map
t = tuple(map(int, input("enter elements: ").split()))
# for i in t:
#     if i % 2 == 0:
#         print(i,end=" ")

# def square(n):
#     return n * n
# res = tuple(map(square, t ))
# print(res)


tu = lambda n : n * n

print(set(map(tu,t)))

