# Python练习

#### 实例001：数字组合

**题目：**有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

**分析：**互不相同且无重复数据的三位数，意味着每个数字在此三位数中只能出现一次

**解法一：**使用三个for循环对列表进行遍历，并使用if语句判定每个遍历的值不相等，只能出现一次

```python
numbers = [x for x in range(1,5)]

total = 0
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and i != k and j != k:
                total += 1

print(total)
```

**解法二：**使用itertools库中的permutations来实现

```python
from itertools import permutations

numbers = [x for x in range(1,5)]
total = 0
for number in permutations(numbers, 3):
    print(number)
    total += 1

print(total)
```



#### 实例003：完全平方数

**题目：**一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

**分析：**假设这个整数为x，则x+100是一个完全平方数，x+100+168又是一个完全平方数，即(x+100)开平方再平方=x+100，(x+268)开平方再平方=x+268

**解法一：**直接使用while从0开始暴力循环破解

```python
import math

number = 0
while True:
    number += 1
    if math.isqrt(number + 100)**2 == number + 100 and math.isqrt(number + 268)**2 == number + 268:
        print(number)
        break
```





#### 实例005：三数排序

**题目：**输入三个整数a,b,c，请把这三个数由小到大输出

**解法一：**使用if语句对abc三个整数进行排序处理，始终将最小的值交换给a，确保a是最小值，然后再比较b和c，将最小值交换给b，从而实现排序

```python
a, b, c = map(int, input("请输入三个整数：").split())

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a, b, c)
```

**解法二：**使用sorted函数对abc三个整数进行排序

```python
a, b, c = map(int, input("请输入三个整数：").split())

print(sorted(list(a,b,c))
```

