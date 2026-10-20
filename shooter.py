import os
import pygame

from pygame.surface import Surface
from pygame.image import load
from pygame.key import get_pressed as keyboard

pygame.init()

class Background:

    def __init__(self,game):
        self.game = game
        self.images = self.collect_images()

    def collect_images(self):

        images = []

        for img in ["sky_cloud.png", "mountain.png","pine1.png","pine2.png"]:
            img_file = load(f"images/background/{img}").convert_alpha()

            value = img_file.get_width() / self.game.WIDTH
            new_width = img_file.get_width() / value
            new_height = img_file.get_height() / value

            img_file = pygame.transform.scale(img_file, (new_width, new_height))

            images.append(img_file)
        return images
        

    def draw(self, display:Surface):
        display.blit(self.images[0], (0, 0) )
        display.blit(self.images[1], (0, self.images[0].get_height()-200))
        display.blit(self.images[2], (0, self.images[0].get_height()-150))
        display.blit(self.images[3], (0, self.images[0].get_height()-100))

    def update(self):
        pass
        

class Player:
    def __init__(self, x, y):

        self.speed = 10
        self.states = ["Idle", "Run", "Jump", "Death"]
        self.image_set = self.collect_images()

        self.state = 0
        self.image_index = 0
        self.direction= 0

        self.image = self.image_set[ self.states[self.state] ][self.image_index]
        self.rect = self.image.get_rect(topleft=(x, y))


    def collect_images(self):
        data = {}
        for key in self.states:
            data[key] = []
            img_files = os.listdir(f"images/player/{key}")
            for img in img_files:
                frame = load(f"images/player/{key}/{img}")
                w = frame.get_width()
                h = frame.get_height()
                frame = pygame.transform.scale(frame, (w * 2, h * 2))
                data[key].append(frame)
        return data 

    def animate(self,anim_speed=4):

        total = len(self.image_set[ self.states[ self.state]])

        if self.image_index < total * anim_speed - 1:
            self.image_index += 1
        else:
            self.image_index = 0

        image = self.image_set [self.states[self.state] ][self.image_index // anim_speed]
        self.image = pygame.transform.flip(image, self.direction,False)

    def move(self):

        if keyboard()[pygame.K_d]:
            self.rect.x += self.speed
            self.state = 1
            self.direction = 0

        elif keyboard()[pygame.K_a]:
             self.rect.x -= self.speed
             self.state = 1
             self.direction = 1 

        else:
            self.state = 0

        

    def draw(self, display: Surface):

        display.blit(self.image, self.rect)

    def update(self):
        self.animate()
        self.move()
        


class Game:

    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 600
        self.FPS = 30 

        self.display = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )
        self.clock = pygame.time.Clock()


    def run(self):

        player=Player(100, 400)
        background = Background(self)

        running = True
        while running:
            pygame.display.update()
            self.display.fill("white")
            self.clock.tick(self.FPS)

            background.draw(self.display)
            background.update()

            player.draw(self.display)
            player.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()

