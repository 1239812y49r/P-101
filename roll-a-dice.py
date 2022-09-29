import random

r = "si"

while r == "si":

    al = random.randint(1,6)

    if al == 1:
        print("_________")
        print("[       ]")
        print("[   0   ]")
        print("[       ]") 
        print("---------")

    if al == 2:
        print("_________")
        print("[ 0     ]")
        print("[       ]")
        print("[      0]") 
        print("---------")
    
    if al == 3    :
        print("_________")
        print("[ 0     ]")
        print("[   0   ]")
        print("[     0 ]") 
        print("---------")

    if al == 4:
        print("_________")
        print("[0     0]")
        print("[       ]")
        print("[0     0]") 
        print("---------")

    if al == 5:
        print("_________")
        print("[0     0]")
        print("[   0   ]")
        print("[0     0]") 
        print("---------")

    if al == 6:
        print("_________")
        print("[0     0]")
        print("[0     0]")
        print("[0     0]") 
        print("---------")

r = input ("¿Quieres tirar el dado?  ")