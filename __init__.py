import json
COLUMNS = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z".split(".")

class Crossword():
    def __init__(self,p=None,d=None):
        if d == None:
            with open(p, "r") as f:
                data = json.load(f)
                words = data[0]
                positions = data[1]
                clues = data[2]
                w = data[3]
                h = data[4]
        else:
            data = d
            words = data[0]
            positions = data[1]
            clues = data[2]
            w = data[3]
            h = data[4]
            
        self.grid = []
        self.clues = clues
        #create blank grid
        for x in range(0,w):
            self.grid.append([])
            for y in range(0,h):
                self.grid[x].append(" ")
                if y == 0:
                    self.grid[x][y] = COLUMNS[x-1]
                if x == 0:
                    self.grid[x][y] = str(y)
                if x == 0 and y == 0:
                    self.grid[x][y] = " "
        
        #create solutions grid
        self.solve_grid = list()
        for x in range(0,w):
            self.solve_grid.append([])
            for y in range(0,h):
                self.solve_grid[x].append(" ")
                if y == 0:
                    self.solve_grid[x][y] = COLUMNS[x-1]
                if x == 0:
                    self.solve_grid[x][y] = str(y)
                if x == 0 and y == 0:
                    self.solve_grid[x][y] = " "
        
        #populate solutions grid
        for word in words:
            squares = positions[word]
            if squares[0][0] == squares[1][0]:
                horizontal = True
            else:
                horizontal = False
                
            count = -1
            for x in squares:
                count += 1
                self.solve_grid[x[0]][x[1]] = word[count].upper()
                if horizontal:
                    if self.grid[x[0]][x[1]] == " ":
                        self.grid[x[0]][x[1]] = "–"
                    else:
                        self.grid[x[0]][x[1]] = "+"
                else:
                    if self.grid[x[0]][x[1]] == " ":
                        self.grid[x[0]][x[1]] = "|"
                    else:
                        self.grid[x[0]][x[1]] = "+"
        
        print("\n")
        for clue in self.clues: print(clue)
        print("\n")    
        self.loop()
    
    def pr(self):
        for k in self.solve_grid:
            s = ""
            for n in k:
                s += " "+n+" "
        for y in self.grid:
            s = ""
            for n in y:
                s += " "+n+" "
            print(s)
            
    def loop(self):
        self.pr()
        while self.solve_grid != self.grid:
            self.selected = input("Choose a square or type $CLUES for clues: ").strip()
            if self.selected == "$CLUES" or self.selected == "$clues":
                print("\n")
                for clue in self.clues: print(clue)
                print("\n")
                
            else:
                s_column = COLUMNS.index(self.selected[0].upper())
                s_row = int(self.selected[1:])
                
                self.fill = input("Choose a letter: ").strip().upper()
                if self.fill == self.solve_grid[s_column+1][s_row]:
                    self.grid[s_column+1][s_row] = self.fill
                    self.pr()
                else:
                    print("That's incorrect.")

#c = Crossword(p="cw_file.json") 
c = Crossword(d=[["water", "plank", "walking", "ail", "llc", "pavise", "tachyon"], {"water": [[1, 1], [1, 2], [1, 3], [1, 4], [1,5]], "plank": [[1, 7], [1,8], [1, 9], [1,10], [1,11]], "walking":[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]], "ail":[[1,2],[2,2],[3,2]], "llc":[[3,1],[3,2],[3,3]], "pavise":[[1,7],[2,7],[3,7],[4,7],[5,7],[6,7]], "tachyon":[[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]]}, ["From top to bottom and left to right", "1 over: wet", "1 down: transportation", "2 over: piracy's end", "2 down: seek a cure", "3 over: cheaper business", "3 down: faster than light", "4 down: protection, but long"], 12, 12])

