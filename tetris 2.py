import renderer as renderer
import time
import keyboard
from random import randint

blockA = [[0,0,0,0],
          [1,1,1,1],
          [0,0,0,0],
          [0,0,0,0]]

blockB = [[1,1],
          [1,1]]

blockC = [[0,1,0],
          [1,1,1],
          [0,0,0]]

blockD = [[0,1,0],
          [0,1,1],
          [0,0,1]]

blockE = [[0,1,0],
          [1,1,0],
          [1,0,0]]

blockF = [[0,1,1],
          [0,1,0],
          [0,1,0]]

blockG = [[1,1,0],
          [0,1,0],
          [0,1,0]]

tex = " -ABCDEFGHIJ"

def constructGrid(longueur,renderer.hauteur):
    
    grille = [[0 for _ in range(longueur)] for _ in range(renderer.hauteur)]
    for y in range(renderer.hauteur):
        for x in range(longueur):
            if x == 0 or x == longueur-1 or y == renderer.hauteur-1:
                grille[y][x] = 1
        return grille
    
def dessiner(grille,b,bTex):
    
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if grille[y][x] != 0:
                placerPixel(x,y,tex[grille[y][x]])
                
    for y in range(len(b)):
        for x in range(len(b[0])):
            if b[y][x] == 1:
                placerPixel(bx+x,by+y,tex[bTex])


def blockInit():
    
    randBlock = [blockA,blockB,blockC,blockD,blockE,blockF,blockG][randint(0,6)]
    randTex = randint(2,len(tex)-1)
    x = (len(grid[0])- len(randBlock))//2
    y = 0
    return randBlock,randTex,x,y

def collision(b, bx,by):
    
    for y in range(len(b)):
        for x in range(len(b[0])):
            if b[y][x] != 0 and grid[y+by][x+bx] != 0 :
                return True
        return False

def rotation(b,bx,by):

    size = len(b)
    
    rotated = [[0 for _ in range(size)] for _ in range(size)]
    
    for x in range(size):
        for y in range(size):
            rotated[x][y] = b[size-y-1][x]
    
    
    if collision(rotated,bx,by):
        return b
    else:
        return rotated

def poserBlock(b,bx,by,bTex):
    
    for y in range(len(b)):
        for x in range(len(b[0])):
            if b[y][x] == 1:
                grid[y+by][x+bx] = bTex

def detectLignes():
    
    check = True
    for y in range(len(grid)-1):
        check = True
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                check = False
            if check:
                del grid[y]
                grid.insert(0,[1]+[0]*(len(grid[0])-2)+[1])

grid = constructGrid(15,20)

bType,bTex,bx,by = blockInit()

temps_initial = time.time()
speed = 0.5

hold = False

while True :
    delete()
    
    if keyboard.is_pressed("up"):
        if not hold:
            bType = rotation(bType,bx,by)
        hold = True
        
    elif keyboard.is_pressed("left"):
        if not hold and not collision(bType,bx-1,by):
            bx -= 1
        hold = True
        
    elif keyboard.is_pressed("right"):
        if not hold and not collision(bType,bx+1,by):
            bx += 1
        hold = True
        
    else :
        hold = False
        
    if keyboard.is_pressed("down"):
        speed = 0.05
    else:
        speed = 0.5
    
    if time.time()-temps_initial>=speed:
        
        if collision(bType,bx,by+1):
            if by == 0:
                print("perdu !")
                input()
                exit()
            else:
                poserBlock(bType,bx,by,bTex)
                detectLignes()
                bType,bTex,bx,by = blockInit()
        else:
            by += 1
            temps_initial = time.time()
        
    dessiner(grid,bType,bTex)
    
    renderer.afficher()