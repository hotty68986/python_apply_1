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
character_speed  = 10
character_to_x = 0

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10
weapons = [] # 무기는 한번에 여러 발 발사 가능

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path,"ball1.png")),
    pygame.image.load(os.path.join(image_path,"ball2.png")),
    pygame.image.load(os.path.join(image_path,"ball3.png")),
    pygame.image.load(os.path.join(image_path,"ball4.png"))
]
# 공 크기에 따른 최초스피드
ball_speed_y = [-18, -15, -12, -9] # index 0,1,2,3 값
# 공 
balls = []

# 최초 발생하는 큰 공 추가 딕셔너리
balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50, # 공의 y좌표
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x" : 3, # x축 이동방향
    "to_y" : -6, # y축 이동방향
    "init_spd_y" : ball_speed_y[0] # y 최초 속도
})

############################



######## execute ###########
running = True
while running :
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    character_x_pos += character_to_x
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width -character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    # 천장에 닿은 무기 없애기 > 천장에 닿은 무기를 리스트에서 없애는 개념
    weapons = [ [ w[0],w[1] ] for w in weapons if w[1] > 0 ]
    print(weapons)
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()

pygame.quit()

# except Exception as err :
#     print("에러명 : ",err)