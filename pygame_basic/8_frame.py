import pygame

# 1. 기본 초기화(반드시 해야하는 것들)
##########################################################################################
# 1-1. 게임시작
pygame.init()

# 1-2. 화면 크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 1-3. 게임 타이틀 설정
pygame.display.set_caption("인생이란 충돌의 연속")

# 1-4. FPS 변수 설정
clock = pygame.time.Clock()
##########################################################################################



# 2. 사용자 게임 초기화 (배경, 게임이미지, 좌표, 폰트 등)
##########################################################################################
# 2-1. 배경 이미지 불러오기
background = pygame.image.load("E:/004OTHER/python_apply/background.png")

# 2-2. 캐릭터 설정
# 캐릭터 불러오기
character = pygame.image.load("E:/004OTHER/python_apply/character.png")
# 캐릭터 사이즈 설정
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭서 세로 크기
# 캐릭터 위치 설정
character_x_pos = screen_width / 2 - character_width/2 #화면 가로의 절반
character_y_pos = screen_height - character_height  
# 화면 세로 크기 가장 아래 - 캐릭터 크기 : 
# 640 기준일때 캐릭터 (0,0)점이 640 위치에 가게되면 나머지 캐릭터는 화면 밖으로 벗어나서 안보임

# 캐릭터 이동 속도
character_speed = 0.3
# 캐릭터가 이동할 좌표변수 생성
to_x = 0
to_y = 0

# 적캐릭터
enemy_character = pygame.image.load("E:/004OTHER/python_apply/enemy_character.png")
enemy_character_size = enemy_character.get_rect().size 
enemy_character_width = enemy_character_size[0] 
enemy_character_height = enemy_character_size[1] 
enemy_character_x_pos = screen_width / 2 - enemy_character_width/2
enemy_character_y_pos = screen_height / 2 - enemy_character_height/2 

# 2-3. 폰트 정의 
game_font = pygame.font.Font(None,40) #폰트 객체 생성 (폰트,크기)

# 2-4. 시간 설정
#총 시간
total_time = 10
#시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴
##########################################################################################



# 3. 이벤트 루프
###########################################################################################

# 3-1. 게임 실행
running = True
while running:
    # 3-2. 프레임 설정
    dt = clock.tick(60)
    print("fps :" + str(clock.get_fps()))
    # 3-3. 이벤트 처리
    for event in pygame.event.get():
        # 종료 이벤트
        if event.type == pygame.QUIT: 
            running = False
        # 키 입력 이벤트
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
    # 3-4. 캐릭터 이동 좌표 저장
    character_x_pos += to_x * dt # *dt값을 곱해주면서 fps속도에 대한 보정
    character_y_pos += to_y * dt

    # 3-5. 충돌처리
    #충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos #캐릭터의 실제 좌표값을 현재 위치로 변경 
    character_rect.top = character_y_pos
    enemy_character_rect = enemy_character.get_rect()
    enemy_character_rect.left = enemy_character_x_pos
    enemy_character_rect.top = enemy_character_y_pos
    #screen.blit > 화면에 표시만 해주는 기능이라고 생각하고
    # ^ 이 위에 부분은 실제 이미지 위치 값을 지정해주는 개념

    if character_rect.colliderect(enemy_character_rect): # 사각형 표면에 충동했는지 확인하는 함수
        print("충돌했어요")
        running = False

    # 3-6. 스크린에 표시
    screen.blit(background,(0,0)) # 배경설정
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy_character,(enemy_character_x_pos,enemy_character_y_pos))


    # 3-7. 타이머 집어넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과시간을 1000으로 나누어서 초 단위 표시 ( 기본 : ms)
    #time.get_ticks() > 현재 시간을 가져옴 즉 현재시간 - 시작시간
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    #render > 글자 그리기 (출력할 글자 ,안티앨리언스 true, 색깔)
    screen.blit(timer, (10,10))
    #타임오버 글자
    time_over = game_font.render("TIME OVER",True,(255,255,255))
    #만약 시간이 0이하이면 게임종료
    if total_time - elapsed_time <= 0 :
        screen.blit(time_over, (screen_width/2,screen_height/2))
        running = False

    # 3-8. 게임화면 반복 업데이트 (필수)
    pygame.display.update()
    
    # 3-9. 가로세로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
#############################################################################################


#잠시 딜레이
pygame.time.delay(2000) # 2초 정도 대기 (ms)

#pygame 종료
pygame.quit()