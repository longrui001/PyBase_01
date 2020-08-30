print("hello world !")
print("hello world !")
age = 3
if age >= 3:
    print("age = "+str(age))

sum =0
for x in range(1,101):
  if (x == 51):break
  sum += x
print (sum)

d = {
    "a":1,
    "b":2,
    "c":3
}
d["d"] = 4
print(d["a"])
print(d)
d.pop('d')
print(d)

set1 = set([1,2,3,4,5])
set2 = set([2,3,4,5,6,7,8])
print(set1|set2)

def power(x,n = 2):
    n = n-1
    while n >0 :
        x = x*x
        n = n-1
    return x

power(5,2)
print(power(5,2))
print(power(5))

#默认参数，默认参数放在后面，类型必须的是不可变型
def add_end(L = []):
    L.append('END')
    return L

l1 = add_end([1,2,3])
l2 = add_end(["x","y","z"])
print(l1)
print(l2)
l3 = add_end()
print(l3)
l4 = add_end()
print(l4)
l5 = add_end()


print(l5)

#可变参数 *
def cacul(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i

    return sum

print(cacul(1,2,3))
print(cacul(1,2,3,4))
print(cacul())
nums = [1,2,3]
print(cacul(*nums))

##关键字参数 **
def person(name,age,**kw):
    print("name : ",name+" age : ",age ," other : ",kw)
extra = {"city":"beijing","job":"engineer"}
person("longrui",30,**extra)

#命名受限制的关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)


#切片，略

#迭代 略

#列表生成式
list(range(1,11))
lx = [x*x for x in range(1,11) if x%2 ==0]
print(lx)
#双层循环
mn = [m+n for m in "ABC" for n in "abc"]
print(mn)

d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k+" = "+v)



##生成器，动态增长内存
#构造方法
# 1，将列表生成式的[],改成()
x2 = (x*x for x in range(1,11) if x%2 ==0)
print(x2)

# 2,包含yield关键字
def fib(max):
    n,a,b, = 0,0,1
    while n<max:
        #print (b)
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

fib(3)

##迭代器

#可直接作用于for循环的有 1. list，str，tuple，dict，set
# 2. generator
#可直接用for循环的称为Iterable，可迭代对象
from collections import Iterable
isinstance((x for x in range(1,10)),Iterable)

###可以被next()调用并返回下一个对象的成为迭代器 Iterator
