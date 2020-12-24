#函数式编程
#map
from collections.abc import Iterable
def f(x):
    return x*x

r = map(f,[1,2,3,4])
list(r)

#reduce
def add(x,y):
    return x + y
from	functools	import	reduce
reduce(add,[1,2,3,4,5,6])

#filter
def isOdd(x):
    return x%2 == 1


list(filter(isOdd,[1,2,3,4]))

#删除空字符串
def isEmpty(str):
    return str and str.strip()

list(filter(isEmpty,["","a"," ","d"]))

##求1000以内的素数





#sort
sorted([],key=abs,reverse=True)

#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax +i
        return ax
    return sum

f1 = lazy_sum(*[1,2,3,4])

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1 = count
f1()

def now():
    print('2020-08-30')

fn = now
fn()


fn.__name__



