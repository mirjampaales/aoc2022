f = open("strategy.txt")
score = 0
for row in f:
    if row[2] == 'X': #rock from me / needs to lose
        #score = score + 1
        #no points for losing
        if row[0] == 'A': #rock from them
            #score = score + 3
            score = score + 3 #choosing scissors gives me 3 points
        elif row[0] == 'B': #paper from them
            #pass
            score = score + 1 #choosing rock gives me 1 point
        else: #scissors from them
            #score = score + 6
            score = score + 2 #choosing paper gives me 2 points
    elif row[2] == 'Y': #paper from me / needs to draw
        #score = score + 2
        score = score + 3 #if it draws I get 3 points
        if row[0] == 'A': #rock from them
            #score = score + 6
            score = score + 1 #choosing rock gives me 1 point
        elif row[0] == 'B': #paper from them
            #score = score + 3
            score = score + 2 #choosing paper gives me 2 points
        else: #scissors from them
            #pass
            score = score + 3 #choosing scissors gives me 3 points

    else: #scissors from me / needs to win
        #score = score + 3
        score = score + 6 #six points for winning
        if row[0] == 'A': #rock from them
            #pass
            score = score + 2 #choosing paper gives me 2 points
        elif row[0] == 'B': #paper from them
            #score = score + 6
            score = score + 3 #choosing scissors me 3 points
        else: #scissors from them
            #score = score + 3
            score = score + 1 #choosing rock gives me 1 point
f.close()
print(score)

