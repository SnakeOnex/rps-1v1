#import matej
import roman

def to_string(s):
    output = ""
    if s == 'r':
        output = "kámen";
    elif s == 'p':
        output = "papír"
    elif s == 's':
        output = "nůžky"

    return output
        

p2 = roman.Player()

print(p2.play())

p1_score = 0
p2_score = 0

for i in range(100):
    # move1 = p1.play()
    move1 = 'r'
    move2 = p2.play()

    win = 0 

    while win == 0:
        if move1 == 'r' and move2 == 's':
            win = 1
        elif move1 == 'p' and move2 == 'r':
            win = 1
        elif move1 == 's' and move2 == 'p':
            win = 1
        elif move1 == move2:
            #move1 = p1.play()
            move2 = p2.play()
        else:
            win = 2

    print("Matěj hraje " + to_string(move1))
    print("Roman hraje " + to_string(move2))

    if (win == 1):
        print(str(i) + ": Matěj vyhrává!")
        p1_score += 1
    else:
        print(str(i) + ": Roman vyhrává!")
        p2_score += 1

print("Scóre: " + str(p1_score) + ":" + str(p2_score))

if p1_score == p2_score:
    print("Remíza!")
elif p1_score > p2_score:
    print("Matěj vyhrává se scóre " + str(p1_score) + " bodů!")
else:
    print("Roman vyhrává se scóre " + str(p2_score) + " bodů!")




