import pygame

pygame.init() # 게임시작
 
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정


pygame.display.set_caption("Nado Game") # 화면 타이틀 설정

#FPS
clock = pygame.time.Clock()


background = pygame.image.load("E:/004OTHER/python_apply/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("E:/004OTHER/python_apply/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭서 세로 크기

character_x_pos = screen_width / 2 - character_width/2#화면 가로의 절반
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래 - 캐릭터 크기 
                                                    # 640 기준일때 캐릭터 (0,0)점이 640 위치에 가게되면
                                                    # 나머지 캐릭터는 화면 밖으로 벗어나서 안보임

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임이 진행중인가?

#이동 속도
character_speed = 0.3


# 적캐릭터
#캐릭터(스프라이트) 불러오기
enemy_character = pygame.image.load("E:/004OTHER/python_apply/enemy_character.png")
enemy_character_size = enemy_character.get_rect().size #이미지의 크기를 구해옴
enemy_character_width = enemy_character_size[0] # 캐릭터 가로 크기
enemy_character_height = enemy_character_size[1] # 캐릭서 세로 크기

enemy_character_x_pos = screen_width / 2 - enemy_character_width/2#화면 가로의 절반
enemy_character_y_pos = screen_height / 2 - enemy_character_height/2  # 화면 세로 크기 가장 아래 - 캐릭터 크기 
                                                    # 640 기준일때 캐릭터 (0,0)점이 640 위치에 가게되면
                                                    # 나머지 캐릭터는 화면 밖으로 벗어나서 안보임


while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정
    # 캐릭터가 1초동안 100만큼 이동을 해야함
    # 10 fps : 1초 동안 10번 동장 > 한번에 10만큼 이동
    # 20 fps : 1초 동안 20번 동작 > 한번에 5만큼 이동
    # 지금 코드에서는 프레임이 낮아지면 속도가 낮아짐
    print("fps :" + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히느 ㄴ이벤트가 발생하였는가
            running = False # 게임 종료
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # *dt값을 곱해주면서 fps속도에 대한 보정
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width



    #충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    #캐릭터의 실제 좌표값을 현재 위치로 변경 
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_character_rect = enemy_character.get_rect()
    enemy_character_rect.left = enemy_character_x_pos
    enemy_character_rect.top = enemy_character_y_pos
    #screen.blit > 화면에 표시만 해주는 기능이라고 생각하고
    # ^ 이 위에 부분은 실제 이미지 위치 값을 지정해주는 개념



    #충돌체크
    if character_rect.colliderect(enemy_character_rect): # 사각형 표면에 충동했는지 확인하는 함수
        print("충돌했어요")
        running = False

    screen.blit(background,(0,0)) # 배경설정
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy_character,(enemy_character_x_pos,enemy_character_y_pos))
    pygame.display.update() # 게임화면 반복 업데이트

    #세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

#pygame 종료
pygame.quit()