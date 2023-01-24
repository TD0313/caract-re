année = int(input("Mettez une année :"))
if ((année % 4 == 0)  and (année % 100 != 0) or (année % 400 == 0)):
    print (année,"Bissextile")
else :
    print (année,"pas bissextile")

