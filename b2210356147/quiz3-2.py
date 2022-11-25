import sys
strstep=""
outputlist=[]
numberstr=sys.argv[1]
numberstr2=""
step=numberstr.split(" ")
for x in step:
    strstep+=x
numberliststr=strstep.split(",")
numberlistint=[int(number) for number in numberliststr]
numberlistint2=numberlistint.copy()
for i in range(len(numberlistint)):
    number=numberlistint2[i]
    if number%2==0:
        numberlistint.remove(number)
    if number<0:
        numberlistint.remove(number)
numberlistint3=numberlistint.copy()
for i in range(len(numberlistint)):
    number=numberlistint3[i]
    if (i+1)%3==0:
        numberlistint.remove(number)
numberlistint4=numberlistint.copy()
for i in range(len(numberlistint)):
    number=numberlistint4[i]
    if (i+1)%7==0:
        numberlistint.remove(number)
numberliststr=[str(number) for number in numberlistint]
for element in numberliststr:
    numberstr2+=("{} ".format(element))
print("Output : {}".format(numberstr2))