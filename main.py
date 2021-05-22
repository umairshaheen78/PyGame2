# Import the system library and PyGame Library
import sys, pygame

# Initialize PyGame
pygame.init()

# Setting up the Screen Size
size = width, height= 650, 350

# Creating a display screen with size
screen = pygame.display.set_mode(size)

# Loading an image
ball = pygame.image.load("intro_ball.gif")    

# Measure the ball size in the rectangle
ballrect = ball.get_rect()

# Setting the Ball Speed
speed = [1, 1]

# Setting color (black; 0,0,0)
black = 0, 0, 0

# Makes the Game Repeating
while True:
	# When the user clicks the exit btton, game terminates
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			sys.exit()

	# Changing ball directions after bouncing
	ballrect = ballrect.move(speed)

    # If ball goes left
	if (ballrect.left < 0  or ballrect.right > width):
		speed[0] = -speed[0]
	
    # If ball goes right
	if (ballrect.top < 0  or ballrect.bottom > height):
		speed[1] = -speed[1]
	
	screen.fill(black)

	#Updating the screen and the balll position
	screen.blit(ball, ballrect)
	pygame.display.flip()