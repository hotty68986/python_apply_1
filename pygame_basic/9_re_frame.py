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



# 2. 사용자 게임 초기화 (배경, 게임이미지, 좌표, 속도, 폰트 등)
##########################################################################################

##########################################################################################



# 3. 이벤트 루프
###########################################################################################

# 3-1. 게임 실행
running = True
while running:
    # 3-2. 프레임 설정
    dt = clock.tick(30)

    # 3-3. 이벤트 처리

    # 3-4. 캐릭터 이동 좌표 저장

    # 3-5. 가로세로 경계값 처리

    # 3-6. 충돌처리

    # 3-7. 스크린에 표시

    # 3-8. 게임화면 반복 업데이트 (필수)
    pygame.display.update()
    

#############################################################################################


#잠시 딜레이
pygame.time.delay(2000) # 2초 정도 대기 (ms)

#pygame 종료
pygame.quit()