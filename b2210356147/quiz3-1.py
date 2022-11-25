import sys
numlist=[]
outputlist=[]
x=sys.argv[1]
a=int(x)
y=sys.argv[2]
b=int(y)
exponent=a**b
numlist.append(exponent)
numlist=list(str(exponent))
for i in range(0,len(numlist)):
    number=numlist[i]
    outputlist.append(number)
    outputlist.append(" + ")
outputlist.pop(-1)
outputstr=""
for element in outputlist:
    outputstr += element
numint=[int(numstr) for numstr in numlist]
Sum = sum(numint)
print("Output : {}^{} = {} = {} = {}".format(a,b,exponent,outputstr,Sum))