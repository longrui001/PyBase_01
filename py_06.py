# switch..case
n = 0
if n == 0:
    print("you typed zero .\n")
elif n == 1:
    print("you typed 1 .\n")
elif n == 2:
    print("you typed 2 .\n")


#Ìø×ª±í



def getN(n):
    return
{
    0:"you typed zero .\n",
    1:"you typed 1 .\n",
    2:"you typed 1 .\n"
}.get(n,"only single-digit numbers are allowed \n")

getN(1)