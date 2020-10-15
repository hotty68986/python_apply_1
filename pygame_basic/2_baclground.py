import pygame

pygame.init() # 게임시작
 
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정


pygame.display.set_caption("Nado Game") # 게임 이름 설정


background = pygame.image.load("E:/004OTHER/python_apply/background.png")


#이벤트 루프
running = True #게임이 진행중인가=
 
while running: 
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 =
        if event.type == pygame.QUIT: # 창이 닫히느 ㄴ이벤트가 발생하였는가
            running = False # 게임 종료

    screen.blit(background,(0,0)) # 배경설정 
    pygame.display.update() # 게임화면 반복 업데이트

#pygame 종료
pygame.quit()