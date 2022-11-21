if __name__ == '__main__':
    matches = []
    f = open("matches.txt", "r")
    for line in f:
        splitlist = line.split(" ")
        if len(splitlist) != 4:
            print("error in match data :", line, end="")
            continue
        try:
            splitlist[2] = int(splitlist[2])
            splitlist[3] = int(splitlist[3])
        except ValueError:
            print("invalid score", line, end="")
        continue
    matches.append(splitlist)
    f.close()
    print("R E S U L T S")
    highestScore = 0
    highestScoreTeam = ""
    for match in matches:
        homeTeam = match[0]
        awayTeam = match[1]
        homeScore = match[2]
        awayScore = match[3]
        if homeScore <= highestScore:
            highestScoreTeam = homeTeam
            highestScore = homeScore
        if awayScore > highestScore:
            highestScoreTeam = awayTeam
            highestScore = awayScore
        print(homeTeam, " ", homeScore, " : ", awayScore, " ", awayTeam)
print("Highest scoring team was", highestScore, highestScoreTeam)
