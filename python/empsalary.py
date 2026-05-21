name=input("enter Employee name : ")
empid=int(input("enter employee id : "))
bs=int(input("enter salary : "))
if bs >= 100000 :
    hra = bs * 0.3
    da = bs * 0.2
    pf = bs * 0.1
elif bs <= 50000 :
     hra = bs * 0.2
     da = bs * 0.1
     pf = bs * 0.05
else : 
     hra = bs * 0.1
     da = bs * 0.05
     pf = bs * 0.025
gs = hra + da + bs
ns = gs - pf
print("name=",name);
print("employee number=",empid);
print("gross salary = {} and net salary= {}".format(gs,ns));