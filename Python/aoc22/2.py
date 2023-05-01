def part1(data):
    dict = {"X":  1, "Y":  2,    "Z":  3,}
    points = 0
    for i in data:
        opponent = i[0]; you = i[-1] 
        points += dict[you]
        if(DEBUG):
            print(i[0] + "&" + i[-1])
            
        if(opponent == "A"): 
            if(you == "X"):
                points += 3
            if(you == "Y"):
                points += 6
            if(you == "Z"):
                points += 0             
        elif(opponent == "B"):
            if(you == "X"):
                points += 0
            if(you == "Y"):
                points += 3
            if(you == "Z"):
                points += 6
        elif(opponent == "C"):
            if(you == "X"):
                points += 6
            if(you == "Y"):
                points += 0
            if(you == "Z"):
                points += 3     
    return points

def part2(data):
    points = 0
    dict = {"A":1,"B":2,"C":3,
            "X":0,"Y":3,"Z":6}
    for i in data:
        opponent = i[0]
        score = i[-1]
        points += dict[score]
        if(score == "Y"):
            points += dict[opponent]
        if(score == "X"):
            if(opponent == "A"):
                points += dict["C"]
            else:
                points += dict[opponent]-1
        if(score == "Z"):
            if opponent == "C":
                points += dict["A"]
            else:
                points += dict[opponent] +1
    return points

#This is my solution for advent of code 2022
DEBUG =False
#Dictionary of values for Rock(X) Paper(Y) and Scissor(Z) 

#opening the input file and formatting it into a list
with open("data/2.txt") as file:
      data = [i for i in file.read().split("\n")]

#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤PART1¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
points = part1(data)

print("part 1: ", points)
#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤PART2¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
points = part2(data)

print("part 2: ", points)