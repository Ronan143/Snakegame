import pygame
import sys
from pygame.math import Vector2
import time
import random

# Snake parameters
block_size = 20
snake_speed = 15

# Time limit
time_limit = 999999
start_time = time.time()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False


        head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(head_up, (40, 40)).convert_alpha()
        head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_down = pygame.transform.scale(head_down, (40, 40)).convert_alpha()
        head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(head_right, (40, 40)).convert_alpha()
        head_left = pygame.image.load('head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(head_left, (40, 40)).convert_alpha()

        tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(tail_up, (40, 40)).convert_alpha()
        tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(tail_down, (40, 40)).convert_alpha()
        tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(tail_right, (40, 40)).convert_alpha()
        tail_left = pygame.image.load('tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(tail_left, (40, 40)).convert_alpha()

        body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(body_vertical, (40, 40)).convert_alpha()
        body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(body_horizontal, (40, 40)).convert_alpha()

        body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(body_tr, (40, 40)).convert_alpha()
        body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(body_tl, (40, 40)).convert_alpha()
        body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(body_br, (40, 40)).convert_alpha()
        body_bl = pygame.image.load('body_bl.png').convert_alpha()   
        self.body_bl = pygame.transform.scale(body_bl, (40, 40)).convert_alpha()
        self.pipe_sound = pygame.mixer.Sound('metal pipe.mp3')

    def drawsnake(self):
        self.update_head_graphics()
        self.update_tail_graphics()


        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)


            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] -block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    def play_pipe_sound(self):
        self.pipe_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)   
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple_trans,fruit_rect)
        #pygame.draw.rect(screen,(126,166,144),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

screen_color= (5,110,5)
grass_color = (0,100,0)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.drawsnake()
            self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_pipe_sound()

        for block in self.snake.body[1:]:
            if block == self .fruit.pos:
                self.fruit.randomize() and print('the fruit attacked the snake')

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                 for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surf = game_font.render(score_text,True,(5,5,5))
        score_x = int(cell_size * cell_number -60)
        score_y =int(cell_size * cell_number - 30)
        score_rect = score_surf.get_rect(center = (score_x,score_y))
        apple_rect = apple_trans.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 20,apple_rect.height)

        pygame.draw.rect(screen,(179,0,0),bg_rect)
        screen.blit(score_surf,score_rect)
        screen.blit(apple_trans,apple_rect)
        pygame.draw.rect(screen,(0,0,0),bg_rect,2)

    #if score_text =+ 1

game_active = False
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = int(40)
cell_number = int(20)
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
apple = pygame.image.load("Actual.gif").convert_alpha()
apple_trans = pygame.transform.scale(apple, (40, 40)).convert_alpha()
game_font = pygame.font.Font('postan.ttf', 22)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1,0)       
    
    screen.fill((screen_color))
    main_game.draw_elements()

    pygame.display.update()
    #clock.tick(120)

        # Add 10 seconds to time limit each time the score goes up by 1
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        length_of_snake += 1
        start_time = time.time()
    
        snake_speed += 10

    clock.tick(snake_speed)