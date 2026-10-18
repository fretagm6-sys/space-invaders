import pygame

WIDTH=900
HEIGHT=500

FPS=60
WHITE=(255,255,255)

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")


WHITE=(255,255,255)
Yellow_spaceship=pygame.image.load(os.path.join("images","spaceship_yellow.png"))
Red_spaceship=pygame.image.load(os.path.join("images","spaceship_red.png"))

spaces=pygame.image.load(os,path.join("images","space.png"))
def draw():
    WIN.blit(WHITE)
    pygame.display.update

def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        draw_window()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

    pygame.quite()

if __name__ == "__main__":
    main()

