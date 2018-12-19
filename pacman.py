import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255)
pacman_circle_color= pygame.Color(255,204,0,255)
GHOST_COLOR = pygame.Color(255,255,255,0)
SUPER_COLOR = pygame.Color(0,127,127,0)
score_color = pygame.Color(200,100,0,0)
time_color = pygame.Color(100,200,50,0)
win_color = pygame.Color(0,255,0,0)
life_color =pygame.Color(0,200,100,50)
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)
STILL=(0,0)
score=0
clock=pygame.time.Clock()
pacman1=pygame.image.load('pacman_2.png')
pacman2=pygame.image.load('pacman_21.png')
pacman3=pygame.image.load('pacman_22.png')
pacman4=pygame.image.load('pacman_23.png')
heart=pygame.image.load('package_favourite.png')
ghost=pygame.image.load('ghost_.png')

def draw_life(life):
	pos_life=(8.25,0.25)
	for i in range(0,life):
		screen.blit(heart,pixels_from_points(pos_life))
		pos_life=(pos_life[0]+0.5,pos_life[1])





def message(text,lt,colour,pos):
	screen.blit(background, (0,0))
	text_surf=lt.render(text,True,colour)
	text_rect=text_surf.get_rect()
	text_rect.center=pos
	screen.blit(text_surf,text_rect)
	pygame.display.update()
def score_message(score):
	font=pygame.font.SysFont(None,25)
	text=font.render("SCORE:"+str(score),True,score_color)
	screen.blit(text,pixels_from_points((0.5,0.25)))
def time_message(time_taken):
	font=pygame.font.SysFont(None,25)
	text=font.render("TIME:"+str(time_taken),True,time_color)
	screen.blit(text,pixels_from_points((3,0.25)))
def time_message_END(time_taken):
	font=pygame.font.SysFont(None,25)
	text=font.render("TIME:"+str(time_taken)+'sec',True,time_color)
	screen.blit(text,pixels_from_points((4,8)))
def life_message(life):
	font=pygame.font.SysFont(None,25)
	text=font.render("LIVES:"+str(life),True,life_color)
	screen.blit(text,pixels_from_points((6,0.25)))
	draw_life(life)


def score_END(score):
	font=pygame.font.SysFont(None,25)
	text=font.render("SCORE:"+str(score),True,score_color)
	screen.blit(text,pixels_from_points((4,7)))
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen, pos): 
	pixels = pixels_2(pos)
	pygame.draw.circle(screen,pacman_circle_color, pixels,15)

#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_2(pos)
	pygame.draw.circle(screen, COIN_COLOR, pixels,5)
def draw_ghost(screen,pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, GHOST_COLOR, [pixels, (WIDTH, HEIGHT)])
def draw_super(screen,pos):
	pixels = pixels_2(pos)
	pygame.draw.circle(screen, SUPER_COLOR, pixels, 7)
	

#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)
def pixels_2(pos):
	return (pos[0]*WIDTH+WIDTH//2,pos[1]*HEIGHT+HEIGHT//2)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((320,320), 0, 32)
background = pygame.surface.Surface((320,320)).convert()

temp=0
#Initializing variables
layout_1 = loadtxt('level1.txt', dtype=str)
layout2 = loadtxt('level2.txt', dtype=str)
if temp==1 or temp==0:
	layout1=layout_1
elif temp==10:
	layout1=layout2
rows, cols = layout1.shape
pacman_position = (1,1)
background.fill((0,0,0))
move_direction=STILL
ghost_position=(5,1)
ghost_position_2=(4,18)
lt=pygame.font.Font('freesansbold.ttf',30)
message('welcome to pacman',lt,PACMAN_COLOR,pixels_from_points((5,5)))
time.sleep(2)


while True:
	layout_1 = loadtxt('level1.txt', dtype=str)
	layout2 = loadtxt('level2.txt', dtype=str)
	pacman_position = (1,1)
	ghost_position=(5,1)
	ghost_position_2=(10,10)
	move_direction=STILL
	score=0
	no_=1
	life=3
	time_taken=0
	if temp==1 or temp==0:
		message('press enter to start',lt,PACMAN_COLOR,pixels_from_points((5,5)))
		pygame.init()
		screen = pygame.display.set_mode((320,320), 0, 32)
		background = pygame.surface.Surface((320,320)).convert()
		layout1=layout_1
	elif temp==10:
		message('press enter to start',lt,PACMAN_COLOR,pixels_from_points((10,10)))
		pygame.init()
		screen = pygame.display.set_mode((640,640), 0, 32)
		background = pygame.surface.Surface((640,640)).convert()
		layout1=layout2
	rows, cols = layout1.shape

	key_et=pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == QUIT or key_et[K_ESCAPE]:
			exit()

# Main game loop 
	while  key_et[K_RETURN] and life!=0 and no_!=0:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		screen.blit(background, (0,0))
		no_=0
	
	#Draw board from the 2d layout1 array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
		for col in range(cols):
			for row in range(rows):
				value = layout1[row][col]
				pos = (row, col)
				if value == 'w':
					draw_wall(screen, pos)
				elif value == '.':
					draw_coin(screen, pos)
					no_=no_+1
				elif value =='c':
					draw_super(screen,pos)
					no_=no_+1
		pos=pacman_position
		r=ghost_position
		z=ghost_position_2
	#Draw the player
		#draw_pacman(screen, pacman_position)
		if move_direction==TOP:
			screen.blit(pacman4,pixels_from_points(pacman_position))
		elif move_direction==DOWN:
			screen.blit(pacman2,pixels_from_points(pacman_position))
		elif move_direction==LEFT:
			screen.blit(pacman3,pixels_from_points(pacman_position))
		elif move_direction==RIGHT:
			screen.blit(pacman1,pixels_from_points(pacman_position))
		else:
			draw_pacman(screen, pacman_position)
		score_message(score)
		time_message(time_taken)
		life_message(life)
	
		x=random.choice([TOP,DOWN,LEFT,RIGHT])
		y=random.choice([TOP,DOWN,LEFT,RIGHT])
		
		if layout1[r[0]][r[1]-1] =='w' and x==TOP:
				x = STILL
		if layout1[r[0]][r[1]+1] =='w' and x==DOWN:
				x = STILL
		if layout1[r[0]-1][r[1]] =='w' and x==LEFT:
				x = STILL
		if layout1[r[0]+1][r[1]] =='w' and x==RIGHT:
				x = STILL
		if temp==10:
			if layout1[z[0]][z[1]-1] =='w' and y==TOP:
				y = STILL
			if layout1[z[0]][z[1]+1] =='w' and y==DOWN:
				y = STILL
			if layout1[z[0]-1][z[1]] =='w' and y==LEFT:
				y = STILL
			if layout1[z[0]+1][z[1]] =='w' and y==RIGHT:
				y = STILL

		#draw_ghost(screen,ghost_position)
		screen.blit(ghost,pixels_from_points(ghost_position))
		if temp==10:
			screen.blit(ghost,pixels_from_points(ghost_position_2))
		ghost_position=add_to_pos(ghost_position,x)
		ghost_position_2=add_to_pos(ghost_position_2,y)


	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
		keys=pygame.key.get_pressed()
		if keys[K_w]:
		
		
			move_direction = TOP

		elif keys[K_s]:
		
			move_direction = DOWN
		elif keys[K_a]:
			move_direction = LEFT
		elif keys[K_d]:
			move_direction = RIGHT
		if layout1[pos[0]][pos[1]-1] =='w' and move_direction==TOP:
			move_direction = STILL
		elif layout1[pos[0]][pos[1]+1] =='w' and move_direction==DOWN:
			move_direction = STILL
		elif layout1[pos[0]-1][pos[1]] =='w' and move_direction==LEFT:
			move_direction = STILL
		elif layout1[pos[0]+1][pos[1]] =='w' and move_direction==RIGHT:
			move_direction = STILL


	#Update player position based on movement.
		pacman_position = add_to_pos(pacman_position, move_direction)
		if layout1[pacman_position[0]][pacman_position[1]]=='.':
			layout1[pacman_position[0]][pacman_position[1]]=''
			score=score+1
		if layout1[pacman_position[0]][pacman_position[1]]=='c':
			layout1[pacman_position[0]][pacman_position[1]]=''
			score=score+10
			draw_super(screen,pacman_position)
		if pacman_position==ghost_position or pacman_position==ghost_position_2:
			life=life-1
			ghost_position=(3,8)
			pacman_position=(1,1)
			ghost_position_2=(15,1)


		#TODO: Check if player ate any coin, or collided with the wall by using the layout1 array.
		# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout1 array

	#Update the display
		pygame.display.update()
		clock.tick(60)
		x=clock.get_time()
		x=x/1000
		time_taken=time_taken+x
		time_taken=round(time_taken,2)


	#Wait for a while, computers are very fast.
		time.sleep(0.15)
	if life ==0 and temp!=10:
		temp=1
		message('GAME OVER !!',lt,PACMAN_COLOR,pixels_from_points((5,4)))
		time_message_END(time_taken)
		score_END(score)
		pygame.display.update()
		time.sleep(2)
		message('Press enter to retry',lt,PACMAN_COLOR,pixels_from_points((5,5)))
		time.sleep(2)
	if life ==0 and temp==10:
		message('GAME OVER !!',lt,PACMAN_COLOR,pixels_from_points((10,10)))
		time_message_END(time_taken)
		score_END(score)
		pygame.display.update()
		time.sleep(2)
		message('Press enter to retry',lt,PACMAN_COLOR,pixels_from_points((10,10)))
		time.sleep(2)
		temp=10
		no_=1


	if no_==0 and temp!=10:
		temp=10
		message('LEVEL 1 CLEARED',lt,win_color,pixels_from_points((5,4)))
		time_message_END(time_taken)
		score_END(score)
		pygame.display.update()
		time.sleep(2)
		screen = pygame.display.set_mode((640,640), 0, 32)
		background = pygame.surface.Surface((640,640)).convert()
		message('Press enter to start round 2',lt,PACMAN_COLOR,pixels_from_points((10,10)))
		time.sleep(2)
		no_=1
	if no_==0 and temp==10:
		message('YOU WON!!',lt,win_color,pixels_from_points((10,10)))
		time_message_END(time_taken)
		score_END(score)
		pygame.display.update()
		time.sleep(2)
		message('THANKS FOR PLAYING',lt,pacman_circle_color,pixels_from_points((10,10)))
		time.sleep(2)
		exit()