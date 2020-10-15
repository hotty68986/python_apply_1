import pygame

pygame.init() # 게임시작
 
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정


pygame.display.set_caption("Nado Game") # 게임 이름 설정


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

#이벤트 루프
running = True #게임이 진행중인가=
 
while running: 
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 =
        if event.type == pygame.QUIT: # 창이 닫히느 ㄴ이벤트가 발생하였는가
            running = False # 게임 종료

    screen.blit(background,(0,0)) # 배경설정
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면 반복 업데이트

#pygame 종료
pygame.quit()