import pygame
import random
import time

# 1. 기본 초기화(반드시 해야하는 것들)
##########################################################################################
# 1-1. 게임시작
pygame.init()

# 1-2. 화면 크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 1-3. 게임 타이틀 설정
pygame.display.set_caption("인생은 충돌의 연속")

# 1-4. FPS 변수 설정
clock = pygame.time.Clock()
##########################################################################################



# 2. 사용자 게임 초기화 (배경, 게임이미지, 좌표, 속도, 폰트 등)
##########################################################################################

# 이미지 불러오기
background = pygame.image.load("/Users/jeongseunghwan/Documents/python_apply_1/python_apply1/background.png")
character = pygame.image.load("/Users/jeongseunghwan/Documents/python_apply_1/python_apply1/character.png")
enemy = pygame.image.load("/Users/jeongseunghwan/Documents/python_apply_1/python_apply1/enemy_character.png")

# 캐릭터 설정
character_size = character.get_rect().size
character_width = character_size[0]
character_heigth = character_size[1]

character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_heigth

character_speed = 1

to_x = 0

# 적 설정
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_heigth = enemy_size[1]

enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

game_font = pygame.font.Font(None,80) #폰트 객체 생성 (폰트,크기)
score = 0

##########################################################################################



# 3. 이벤트 루프
###########################################################################################

# 3-1. 게임 실행
running = True
while running:
    # 3-2. 프레임 설정
    dt = clock.tick(60)
    
    # 3-3. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            to_x = 0

    # 3-4. 캐릭터 이동 좌표 저장
    character_x_pos += to_x * dt
    
    # enemy 좌표이동
    enemy_x_rand = random.randint(0, screen_width - enemy_width)
    enemy_y_pos += random.randint(10,25)

    if enemy_y_pos >= screen_height - enemy_heigth:
        enemy_x_pos = enemy_x_rand
        enemy_y_pos = 0
        score += 1
    
    # 3-5. 가로세로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    # 3-6. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    # 타이틀 객체 생성
    title = game_font.render("DDONG",True,(150,75,0))
    title_width = title.get_rect().size[0]
    title_height = title.get_rect().size[1]
    title_x_pos = screen_width /2 - title_width/2
    title_y_pos = screen_height /2 - title_height/2
    
    #score 객체
    score_board = game_font.render(str(score),True,(255,0,0))

    # 3-7. 스크린에 표시
    screen.blit(background,(0,0))
    screen.blit(title,(title_x_pos,title_y_pos))
    screen.blit(score_board,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    # 3-8. 게임화면 반복 업데이트 (필수)
    pygame.display.update()
    

#############################################################################################


#잠시 딜레이
pygame.time.delay(2000) # 2초 정도 대기 (ms)

#pygame 종료
pygame.quit()