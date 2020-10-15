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
pygame.display.set_caption("C'set la vie")

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
ball_speed_y = [-18, -15, -12, -10] # index 0,1,2,3 값
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

# 사라질 무기, 공
weapon_to_remove = -1
ball_to_remove = -1

# 폰트
game_font = pygame.font.Font(None,40)
total_time = 30
game_result = "fuck..."
start_ticks = pygame.time.get_ticks()

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
    
    # 공 위치 정의 
    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 방향 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_val["to_x"] = ball_val["to_x"] * -1
        

        # 튕기는 효과
        if ball_pos_y >= screen_height-stage_height - ball_height :
            ball_val["to_y"] = ball_val["init_spd_y"]
        else :
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 충돌처리
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        #공 rect
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공 - 캐릭 충돌
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공 - 무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_index
                
                # 가장 작은 크기의 공이 아니라면 다음단계의 공으로 나눠주기
                if ball_img_idx < 3 :
                    # 현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                     # 왼쪽 공
                    balls.append({
                            "pos_x" : ball_pos_x + (ball_width/2) - small_ball_width/2, # 공의 x좌표
                            "pos_y" : ball_pos_y + (ball_height/2) - small_ball_height/2, # 공의 x좌표
                            "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                            "to_x" : -3, # x축 이동방향
                            "to_y" : -6, # y축 이동방향
                            "init_spd_y" : ball_speed_y[ball_img_idx + 1] # y 최초 속도
                        })
                    # 오른쪽 공
                    balls.append({
                            "pos_x" : ball_pos_x + (ball_width/2) - small_ball_width/2, # 공의 x좌표
                            "pos_y" : ball_pos_y + (ball_height/2) - small_ball_height/2, # 공의 x좌표
                            "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                            "to_x" : 3, # x축 이동방향
                            "to_y" : -6, # y축 이동방향
                            "init_spd_y" : ball_speed_y[ball_img_idx + 1] # y 최초 속도
                        })

                    break
        
    #충돌된 공 이랑 무기 없앰
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우 게임 종료 (성공)
    if len(balls) == 0 :
        game_result = "yes..."
        running = False


    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))
    
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    if total_time -elapsed_time <= 0:
        game_result = "time..."
        running = False

    pygame.display.update()


msg = game_font.render(game_result, True, (0,0,0))
msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()

# except Exception as err :
#     print("에러명 : ",err)