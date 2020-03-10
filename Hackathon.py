from tkinter import *
import random
from PIL import Image, ImageTk
import time, sys, os

my_window = Tk()
my_window.geometry("500x500")
myCanvas = Canvas(my_window, width = 400, height = 400, background = 'black')
myCanvas.grid(row=0, column =0)
PlayerSprite = PhotoImage(file="Player.gif")
WallSprite = PhotoImage(file="wall.gif")
FloorSprite = PhotoImage(file="floor.gif")
WinSprite = PhotoImage(file="Victor.gif")
MonsterSprite = PhotoImage(file="Monster.gif")
WORLDWIDTH = 20
WORLDHEIGHT = 20
tile = 400//WORLDHEIGHT * .5
loEnemies = []
PlayerX = WORLDHEIGHT//2
PlayerY = WORLDHEIGHT//2


class Player:
	def __init__(self, name, xStart, yStart, world):
		self.name = name
		self.x = xStart
		self.y = yStart
		self.realx = WORLDHEIGHT//2
		self.realy = WORLDHEIGHT//2
		PlayerX = self.realx
		PlayerY = self.realy
		self.tileSize = 400//WORLDHEIGHT
		self.id = self.showDave(self.x, self.y)
		self.world = world
		self.setBindings()
		#Game stats
		self.Maxhp = 10
		self.hp = self.Maxhp
		self.atk = 5
		self.arm = 0
		
	def isLegal(self, x, y):
		if(self.world.arr[x][y] == '#'):
			return False
		else:
			return True		
			
	def isWin(self, x, y):
		if(self.world.arr[x][y] == '$'):
			return True
		else:
			return False
	
	def moveLeft(self,evt):
		if(self.isLegal((self.realx - 1), self.realy) == True):
			self.x = self.x - self.tileSize
			myCanvas.delete(self.id)
			self.id = self.showDave(self.x, self.y)
			self.realx -= 1
			self.world.arr[self.realx][self.realy] = '@'
			self.world.arr[self.realx + 1][self.realy] = '%'
			if(self.isWin(self.realx, self.realy)):
				text = Label(my_window, text="YOU WIN")
				text.place(x=100, y=401)
				self.clearBindings()
	def moveRight(self,evt):
		if(self.isLegal((self.realx + 1), self.realy) == True):
			self.x = self.x + self.tileSize
			myCanvas.delete(self.id)
			self.id = self.showDave(self.x, self.y)
			self.realx += 1
			self.world.arr[self.realx][self.realy] = '@'
			self.world.arr[self.realx - 1][self.realy] = '%'
			if(self.isWin(self.realx, self.realy)):
				text = Label(my_window, text="YOU WIN")
				text.place(x=100, y=401)
				self.clearBindings()
	def moveUp(self,evt):
		if(self.isLegal((self.realx), self.realy - 1) == True):
			self.y = self.y - self.tileSize
			myCanvas.delete(self.id)
			self.id = self.showDave(self.x, self.y)
			self.realy -= 1
			self.world.arr[self.realx][self.realy] = '@'
			self.world.arr[self.realx][self.realy + 1] = '%'
			if(self.isWin(self.realx, self.realy)):
				text = Label(my_window, text="YOU WIN")
				text.place(x=100, y=401)
				self.clearBindings()
	def moveDown(self,evt):
		if(self.isLegal((self.realx), self.realy +1 ) == True):
			self.y = self.y + self.tileSize
			myCanvas.delete(self.id)
			self.id = self.showDave(self.x, self.y)
			self.realy += 1
			self.world.arr[self.realx][self.realy] = '@'
			self.world.arr[self.realx][self.realy-1] = '%'
			if(self.isWin(self.realx, self.realy)):
				text = Label(my_window, text="YOU WIN")
				text.place(x=100, y=401)
				self.clearBindings()
	
	def hurt(self, atk):
		if((self.hp-(atk-self.arm))>0):
			self.hp = self.hp - (atk - self.arm)
		else:
			self.hp	= 0
			self.death()
			
	def showDave(self, x, y):
		return myCanvas.create_image(self.x, self.y, image=PlayerSprite)
		
	def setBindings(self):
		myCanvas.bind_all('<KeyPress-Left>', self.moveLeft)
		myCanvas.bind_all('<KeyPress-Right>', self.moveRight)
		myCanvas.bind_all('<KeyPress-Up>', self.moveUp)
		myCanvas.bind_all('<KeyPress-Down>', self.moveDown)
	
	def clearBindings(self):
		myCanvas.bind_all('<KeyPress-Left>', self.doNothing)
		myCanvas.bind_all('<KeyPress-Right>', self.doNothing)
		myCanvas.bind_all('<KeyPress-Up>', self.doNothing)
		myCanvas.bind_all('<KeyPress-Down>', self.doNothing)

	def doNothing(self, evt):
		return 0
			
	def death(self):
		text = Label(my_window, text="YOU DIED!")
		text.place(x=100, y=401)
		self.clearBindings()
		myCanvas.delete(self.id)
		return 0;

class Enemy:
	
	def __init__(self, xStart, yStart, y, x):
		self.x = x
		self.y = y
		self.pixX = xStart
		self.pixY = yStart
		self.id = self.showMug(self.x, self.y)
		self.hp = 4
		self.atk = 2
		self.arm = 0
		
	def updateEnemy(self):
		myList = astar(self.x, self.y, PlayerX, PlayerY)
		if (myList[1].positionX > self.x):
			return 0
		
		
	def moveLeft(self,evt):
		if(self.isLegal((self.x - 1), self.y) == True):
			self.pixX = self.pixX - 2*tile
			myCanvas.delete(self.id)
			self.id = self.showMug(self.pixX, self.pixY)
			self.x -= 1
			world.arr[self.x][self.y] = '&'
			world.arr[self.x + 1][self.y] = '%'
			
	def moveRight(self,evt):
		if(self.isLegal((self.x + 1), self.y) == True):
			self.pixX = self.pixX + 2*tile
			myCanvas.delete(self.id)
			self.id = self.showMug(self.pixX, self.pixY)
			self.x += 1
			world.arr[self.x][self.y] = '&'
			world.arr[self.x -1][self.y] = '%'
			
	def moveUp(self,evt):
		if(self.isLegal((self.x ), self.y-1) == True):
			self.pixY = self.pixY - 2*tile
			myCanvas.delete(self.id)
			self.id = self.showMug(self.pixX, self.pixY)
			self.y -= 1
			world.arr[self.x][self.y] = '&'
			world.arr[self.x + 1][self.y] = '%'
	def moveDown(self,evt):
		if(self.isLegal((self.x ), self.y+1) == True):
			self.pixY = self.pixY + 2*tile
			myCanvas.delete(self.id)
			self.id = self.showMug(self.pixX, self.pixY)
			self.y += 1
			world.arr[self.x][self.y] = '&'
			world.arr[self.x - 1][self.y] = '%'
		
	def chase(self, userPlayer):
		return 0
		
	def defend(self, x1, y1, x2, y2):
		return 0
	
	def showMug(self, x, y):
		return myCanvas.create_image(self.pixX, self.pixY, image=MonsterSprite)
	

class createWorld:
	def __init__(self, r, c):
		self.rows, self.cols = (r,c)
		self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]
		for x in range(0, self.cols):
			for y in range(0, self.rows):
				self.arr[x][y] = '#' #walls
		
	def createLevel(self):
	#Randomize '%' spaces (floor)
		for x in range(1, self.cols-1):
			for y in range(1, self.rows-1):
				myRandomVal = random.randint(0, 100) + 1
				if(myRandomVal >= 55):
					self.arr[x][y] = '%'
				elif(myRandomVal >= 45 and myRandomVal < 55):
					self.arr[x][y] = '&'
		#Build out '%' spaces (floor)
		for x in range(0, self.cols):
			for y in range(0, self.rows):
				if(self.arr[x][y] == '%' or self.arr[x][y] == '&'):
					if((x>1) and (x<self.cols-1) and (y>1) and (y<self.rows-1)):
						'''
						if(self.arr[x-1][y-1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
								'''
						if(self.arr[x][y-1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
						if(self.arr[x+1][y-1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
						if(self.arr[x-1][y]=='#'):
							myRandomVal = random.randint(0, 00) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						if(self.arr[x+1][y]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
						if(self.arr[x-1][y+1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
						if(self.arr[x][y+1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
						if(self.arr[x+1][y+1]=='#'):
							myRandomVal = random.randint(0, 100) + 1
							if(myRandomVal >=20):
								self.arr[x-1][y-1] = '*'
						'''
		self.arr[(self.cols//2)-1][ 1] = '%'
		self.arr[(self.cols//2)-1][ 2] = '%'
		self.arr[(self.cols//2)][ 1] = '%'
		self.arr[(self.cols//2)][2] = '%'
		self.arr[(self.cols//2) +1][1] = '%'
		self.arr[(self.cols//2) +1][2] = '%'
		self.arr[self.cols//2][0] = '$' #goal
		self.arr[self.cols//2][self.rows//2] = '%'
		
		
	def graphicLevel(self):
		for x in range(0,self.rows):
			for y in range(0,self.cols):
				if(self.arr[x][y]==('#')):
					myCanvas.create_image((x*400//self.cols) + (1 * tile), (y*400//self.rows) + (tile), image=WallSprite)
				elif(self.arr[x][y]==('%')):
					myCanvas.create_image((x*400//self.cols) + (1 * tile), (y*400//self.rows) + (tile), image=FloorSprite)
				elif(self.arr[x][y]==('&')):
					myCanvas.create_image((x*400//self.cols) + (1 * tile), (y*400//self.rows) + (tile), image=FloorSprite)
				elif(self.arr[x][y]==('$')):
					myCanvas.create_image((x*400//self.cols) + (1 * tile), (y*400//self.rows) + (tile), image=WinSprite)
				elif(self.arr[x][y] == '*'):
					myCanvas.create_image((x*400//self.cols) + (1 * tile), (y*400//self.rows) + (tile), image=FloorSprite)
	def levelReset(self):
		self.__init__(self.rows, self.cols)
		self.createLevel()
		self.graphicLevel()
'''
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, positionX, positionY):
        self.parent = parent
        self.positionX = positionX
        self.positionY = positionY
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, startX, startY, endX, endY):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, startX, startY)
    start_node.g = 0
    end_node = Node(None, playerX, playerY)
    end_node.g =  0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [0,-1,  0,1, -1,0, 1,0]: # Adjacent squares
            count=0
            other=1
            # Get node position
            node_positionX = (current_node.positionX + new_position[count])
            node_positionY = (current_node.positionY + new_position[other])

            # Make sure within range
            if (node_positionX <= (0) or node_positionX >= self.rows):
                if(node_positionY <= (0) or node_positionX >= self.rows):
                    continue

            # Make sure walkable terrain
            if self.arr[node_positionX][node_positionY] != '#':
                continue

            # Create new node
            new_node = Node(current_node, node_positionX. node_positionY)

            # Append
            children.append(new_node)
            count+=2
            other+=2

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            enemyX = -1
            enemyY =-1
            for x in range(0, WORLDWIDTH):
				for y in range(0, WORLDHEIGHT):
					if WORLD.arr[x][y] == '@':
						playerX = x
						playerY = y
					if WORLD.arr[x][y] == '&':
						enemyX = x
						enemyY = y
			child.f = abs(playerX - enemyX)) + abs(playerY - enemyY)
						

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.f > open_node.f:
                    continue

            # Add the child to the open list
            open_list.append(child)
            return open_list
'''

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def spawnEnemies(world):
	for i in range(0, WORLDHEIGHT):
		for j in range(0, WORLDWIDTH):
			if(world.arr[i][j] == '&'):
				loEnemies.append(Enemy(j * 2 * tile + (tile) ,i * 2 * tile + (tile), i, j))

def interfaceInit():
	world = createWorld(WORLDHEIGHT,WORLDWIDTH)
	world.createLevel()
	world.graphicLevel()
	#spawnEnemies(world)
	Button(my_window, text="QUIT", width=6, command=my_window.destroy).place(x=0, y=401)
	Button(my_window, text="Play Again", width = 10, command=restart).place(x=291, y=401)
	return world

def gameUpdate(player):
	return 0


def main():
	print("love you Dave")
	'''
	root = Tk()
	root.geometry("400x300")
	app = Window(root)
	world = createWorld()
	world.createLevel()
	wMap = world.arr
	while True:
		root.update_idletasks()
		root.update()
	'''
	world = interfaceInit()
	tile = 400//WORLDHEIGHT
	player = Player("Dave", WORLDHEIGHT//2 * tile + (.5 * tile), WORLDHEIGHT//2 * tile  + (.5 * tile), world)
	#world.arr[WORLDHEIGHT//2 * tile + (.5 * tile)][ WORLDHEIGHT//2 * tile  + (.5 * tile)] = '@'
	#player.showDave()
	'''
	img = PhotoImage(file="TheHero(Top) (2).gif")
	myCanvas.create_image(20, 20, image=img)
	'''
	while True:
		gameUpdate(player)
		my_window.update_idletasks()
		my_window.update()
	return 0

main()
