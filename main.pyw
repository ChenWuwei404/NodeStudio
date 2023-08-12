import pygame,numpy,numba,sys,math

pygame.init()

screen = pygame.display.set_mode((500,300),pygame.NOFRAME)
screen.blit(pygame.image.load("./start.png"),(0,0))

pygame.display.update()
pygame.time.delay(1000)
pygame.display.quit()
pygame.time.delay(100)
pygame.display.init()


screen = pygame.display.set_mode((1600,900),pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load("./resource/icon.png"))
pygame.display.set_caption("Node Studio")

Font = pygame.font.Font("./resource/HanSans.ttf",20)
Title = pygame.font.Font("./resource/HanSans.ttf",30)


img_gallery = pygame.image.load("./resource/side/gallery.png")
img_music = pygame.image.load("./resource/side/music.png")
img_mixer = pygame.image.load("./resource/side/mixer.png")
img_editor = pygame.image.load("./resource/side/editor.png")

menu1 = "music"

#  music
#  editor
#  mixer
#  gallery



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window_width,windows_height = pygame.display.get_window_size()

    screen.fill((10,10,10))

    head = pygame.Surface((window_width,80))
    head.fill((50,50,50))
    head.blit(Title.render("Node Studio",1,(255,255,255)),(25,25))

    side = pygame.Surface((60,windows_height))
    side.fill((40,40,40))
    side.blit(img_music,(0,0))
    side.blit(img_mixer,(0,120))
    side.blit(img_editor,(0,60))
    side.blit(img_gallery,(0,180))

    lib = pygame.Surface((300,windows_height))
    lib.fill((30,30,30))


    frame = pygame.Surface((window_width-360,windows_height-40))



    track = pygame.Surface((window_width-460,3200))
    track.fill((0,0,0))
    for i in range(int(3200/80)+1):
        if not(i == 0):
            pygame.draw.line(track,(20,20,20),(0,i*80),(window_width,i*80),5)

    track_id = pygame.Surface((100,3200))
    track_id.fill((50,50,50))
    for i in range(int(3200/80)+1):
        track_id.blit(Font.render("Track  "+str(i+1),1,(255,255,255)),(5,i*80+5))
        if not(i == 0):
            pygame.draw.line(track_id,(70,70,70),(0,i*80),(window_width,i*80),5)


    frame.blit(track,(100,20))
    frame.blit(track_id,(0,20))

    screen.blit(side,(0,80))
    screen.blit(lib,(60,80))
    screen.blit(frame,(360,80))


    screen.blit(head,(0,0))
    pygame.display.update()