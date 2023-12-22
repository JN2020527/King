my_list = [1, 2, 3, 4, 5]

# 创建迭代器对象
my_iterator = iter(my_list)

# # 逐个访问元素
# print(next(my_iterator))  # 输出: 1
# print(next(my_iterator))  # 输出: 2
# print(next(my_iterator))  # 输出: 3

# 使用 for 循环遍历
for item in my_iterator:
    print(item)
