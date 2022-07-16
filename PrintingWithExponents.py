import random
clist=[]
explst=[]
s=""
for i in range(10):
    clist.append(random.randrange(-10,10,1))
    explst.append(str(i))
def print_equation2():
    global s
    for i in range(len(clist)):
        term="+(%s)"%clist[i]+"x"+explst[i]
        s+=term
    print(s)
print_equation2()                 
