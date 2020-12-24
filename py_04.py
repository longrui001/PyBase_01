
import re
line = "aaaboooooooobabbbaaby123"
regex_str1 = ".*?(b.+?b).*"
print(re.match(regex_str1,line).group(1))


regex_str2 = ".*(b.{2,}b).*"
print(re.match(regex_str2,line).group(1))

def foo():
    print("starting...")
    while True:
        yield 4
        res = 5
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(next(g))
print(next(g))





















