#coding=utf-8
from random import randint

# 迭代
data = [1, 5, -3, -2, 6, 0, 9]
res = []
for x in data:
  if x >= 0:
    res.append(x)

print data

# 随机生成一个-10到10之间的10位list
data = [randint(-10, 10) for _ in xrange(10)]
print data

# filter函数, 返回条件为true的对象，组成一个新的list
data = filter(lambda x: x >= 0, data)
print data

# 列表解析
data = [x for x in data if x >= 0]
print data


d = {x: randint(60, 100) for x in xrange(1, 21)}

c = {k: v for k, v in d.iteritems() if v > 90}

print c