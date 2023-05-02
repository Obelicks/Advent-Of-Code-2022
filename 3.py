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



def main():
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
    
    print(prioritysum)

main()



    