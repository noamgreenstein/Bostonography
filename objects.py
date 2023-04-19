import pygame
from presets import *
import data_scraper

pygame.font.init()
pix = [f"images/{i}-9.png" for i in range(1, 10)]
pops = ["Allston", "North End", "empty", "Jamaica Plain",
        "Back Bay", "Fenway", "Roxbury", "South End", "South Boston"]
schools = [f"images/{i}-1.png" for i in range(1, 10)]
countries = [f"images/{i}-2.png" for i in range(1, 10)]
landmarks = [f"images/{i}-3.png" for i in range(1, 10)]


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, type):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.x, self.y = x, y
        self.text = text
        self.type = type
        self.rect = self.image.get_rect()
        self.change_puzzle(type)

    def update(self):
        self.rect.x = self.x * TILESIZE + 100
        self.rect.y = self.y * TILESIZE + 100

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + TILESIZE < GAME_SIZE * TILESIZE

    def left(self):
        return self.rect.x - TILESIZE >= 0

    def up(self):
        return self.rect.y - TILESIZE >= 0

    def down(self):
        return self.rect.y + TILESIZE < GAME_SIZE * TILESIZE

    def change_puzzle(self, idx):
        if self.text != "empty":
            if idx == 0:
                img = pygame.image.load(pix[int(self.text) - 1]).convert()
            if idx == 1:
                num = data_scraper.get_pop_data(pops[int(self.text) - 1])
                font = pygame.font.SysFont("MS Serif", 30)
                pop_num = font.render(str(num), True, WHITE)
                self.image.fill((int(self.text) * 1000 // 255, int(self.text) * 300 // 255 + 20,
                                 int(self.text) * 4500 // 255))
                self.image.blit(pop_num, (self.x + 30, self.y + 60))
                return
            elif idx == 2:
                img = pygame.image.load(schools[int(self.text) - 1]).convert()
            elif idx == 3:
                img = pygame.image.load(countries[int(self.text) - 1]).convert()
            elif idx == 4:
                img = pygame.image.load(landmarks[int(self.text) - 1]).convert()

            img = pygame.transform.scale(img, (TILESIZE, TILESIZE))
            self.image.blit(img, self.rect)
        else:
            self.image.fill(LIGHTGREY)








class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("MS Serif", 55)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))


class Button:
    def __init__(self, x, y, width, height, text, colour, text_colour):
        self.colour, self.text_colour = colour, text_colour
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Verdana", 30)
        text = font.render(self.text, True, self.text_colour)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
