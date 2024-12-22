import random
n = int(input('Gib einen Wert für n ein\n'))
körbe = [0] * n
ball = n
experiment = 100

for _ in range(experiment):
    for __ in range(ball):
        körbe[random.randrange(len(körbe))]+=1


for i in range(len(körbe)):
    körbe[i]/= experiment

print(körbe, max(körbe))



min = 1
n = int(input("Was ist das Ende des Zahlenbereichs?\n"))
while(True):
    halb = ((min + n) // 2)
    b = input(f"Ist deine Zahl kleiner als {halb}?(y/n)\n")
    if b == "y":
        n = halb-1
    elif b == "w":
        exit()
    else:
        min = halb + 1

def sprod(l:list,k:list):
    if len(l) != len(k):
        print ("Listen nicht gleich lang!")
        exit()
    a =0
    for i in range(len(l)):
        a+=l[i] * k[i]
    return a

