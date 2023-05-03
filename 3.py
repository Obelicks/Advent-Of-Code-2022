DEBUG = False

def priority(item):
    if(item.islower()):
        priority = ord(item)-96
        if(DEBUG):
            print(item,": ", priority)
        return priority
    else:
        priority = (ord(item)-38)
        if(DEBUG):
            print(item,": ", priority)
        return priority    



def main_part1():
    prioritysum = 0

    with open("data/3.txt") as file:
        data = [i for i in file.read().split("\n")]
    if(DEBUG):
        print(data)
    for i in data:
        split = int(len(i)/2)
        left = i[:split]
        left =  [*set(left)]
        right =i[split:]
        for j in left:
            if (j in right):
                p = priority(j)
                #print(p)
                prioritysum += p
    
    return(prioritysum)

def main_part2():
    prioritysum = 0
    with open("data/3.txt") as file:
        data = [i for i in file.read().split("\n")]
    if(DEBUG):
        print(data)
    while (len(data) > 0):
        one = data.pop(0)
        one =  [*set(one)]
        two =data.pop(0)
        three = data.pop(0)
        if(DEBUG):
            print(one ,"\n",two,"\n",three)
        for i in one:
            if(i in two and i in three):
                p = priority(i)
                if(DEBUG):
                    print(i,": ",p)
                prioritysum += p
    return prioritysum    

print(main_part1())
print(main_part2())



    