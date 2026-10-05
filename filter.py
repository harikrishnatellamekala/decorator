# filter fun
# traditional way using for loop
# list = [1,5,4,3,6]
# even = []
# def is_even(n):
#     for i in n:
#         if i % 2 == 0:
#             even.apped(i)

# print(even)

# use filter with normal fun

# nums = [4,1,3,7,5,2]

# def is_even(n):
#     if n % 2 == 0:
#         return True

# even = list(filter(is_even,nums))
# print(even)



# filter using the lambda

# nums = [5,2,3,6,2]

# val = lambda n : n % 2 == 0

# even = list(filter(val,nums))
# print(even)

# two lines
nums = [5,2,3,6,2]
print(list(filter(lambda n : n % 2 == 0,nums)))
