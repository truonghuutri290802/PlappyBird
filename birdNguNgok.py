import pygame,sys
def draw_floor():
    screen.blit(floor,(floor_x_pos ,600))
    screen.blit(floor,(floor_x_pos+432 ,600))
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
#them trong luc
gravity = 0.25
bird_moverment= 0
#chen background
bg = pygame.image.load("background-night.png").convert() #convert giup hinh anh load nhanh hon
bg = pygame.transform.scale2x(bg)
#chen san 
floor = pygame.image.load("floor.png")
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tao chim 
bird = pygame.image.load("yellowbird-midflap.png")
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center= (100,384)) # tao hinh vuong xung quanh con chim
while(True):
    for event in pygame.event.get():
        #thao tac tren ban phim 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_moverment = 0
                bird_moverment-= 11
    screen.blit(bg,(0,0))#dat phong
    bird_moverment+=gravity #giup con chim bay 
    bird_rect.centery += bird_moverment
    screen.blit(bird,bird_rect)
    floor_x_pos  -= 1 
    draw_floor()
    if floor_x_pos <=-432:
        draw_floor=0
    pygame.display.update()
    clock.tick(120)
    
