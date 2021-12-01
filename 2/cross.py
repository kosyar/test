class cross(object):
    def __init__(self):
        self.field = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.gamestatus ="start";\
        self.player = True
    def newGame(self):
        self.field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.gamestatus = "game"
        self.showField()



    def cheakgame(self):
        if self.gamestatus == "game":
            for i in range(3):
                if (self.field[i][0] == self.field[i][1] == self.field[i][2] and (self.field[i][0] != " ") and (self.field[i][0] != " ") and (self.field[i][0] != " ")):
                    print()
                    print("win gor  " + self.field[i][0])
                    self.gamestatus = "start"
                    break
                if (self.field[0][i] == self.field[1][i] == self.field[2][i] and (self.field[0][i] != " ") and (self.field[1][i] != " ") and (self.field[0][i] != " ")):
                    print()
                    print("win ver " + self.field[0][i])
                    self.gamestatus = "start"
                    break
                if (self.field[0][0] == self.field[1][1] == self.field[2][2] and (self.field[0][0] != " ") and (self.field[1][1] != " ") and (self.field[2][2] != " ")):
                    print()
                    print("win dig  " + self.field[i][0])
                    self.gamestatus = "start"
                    break
                if (self.field[2][0] == self.field[1][1] == self.field[0][2] and (self.field[2][0] != " ") and (self.field[1][1] != " ") and (self.field[2][0] != " ") ):
                    print()
                    print("win dig  " + self.field[i][0])
                    self.gamestatus = "start"
                    break
    def showField(self):
        self.cheakgame()
        if self.gamestatus == "game":
            print("player turn " + self.who())
            print("  1  2  3")
            field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            for idx, var in enumerate(self.field):
                print(idx + 1, end='')
                for b in var:
                    print("|" + str(b) + "|", end='')
                print()
        else:
            print("""game not start
for new game enter n""")
    def who(self):
        if(self.player == True):
            return "+"
        if(self.player == False):
            return "0"

    def setItem(self,line):
        if(self.field[int(line[1])-1][int(line[0])-1] == "+" or self.field[int(line[1])-1][int(line[0])-1] == "0"):
            self.showField()
            print("bad move")
            return
        self.field[int(line[1])-1][int(line[0])-1] = str(self.who())

        if (self.player == True):
            self.player = False
            self.showField()
            return
        if (self.player == False):
            self.player = True
            self.showField()
            return
