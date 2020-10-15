import os
import pygame

# try :
########## start ###########
pygame.init()

# 화면 크기설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀
pygame.display.set_caption("인생은 마치 튀어다니는 하나의 공")

# FPS
clock = pygame.time.Clock()
############################


########## setting ##########
# 파일 경로 간소화 절차
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "pang_sources") # image 폴더위치
#path.join

# 이미지 불러오기
background = pygame.image.load(os.path.join(image_path,"background.png"))

stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height- character_height - stage_height

############################



######## execute ###########
running = True
while running :
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))



    pygame.display.update()

pygame.quit()

# except Exception as err :
#     print("에러명 : ",err)