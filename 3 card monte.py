# shuffle / how to play / high score: beating levels in a row

import pygame
import random
import sys
from pygame.locals import *
import textwrap

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("3 Card Monte")

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (800, 600))

font = pygame.font.Font('BruceForeverRegular-X3jd2.ttf', 20)


class Button:
    def __init__(self, text, position):
        self.text = text
        self.image = pygame.Surface((200, 50))
        self.rect = self.image.get_rect(center=position)
        self.color = (169, 169, 169)

    def draw(self, surface):
        self.image.fill(self.color)
        text_surface = font.render(self.text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, (self.rect.width // 2 - text_rect.width // 2, self.rect.height // 2 - text_rect.height // 2))
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)


class Card:
    def __init__(self, front_image_path, back_image_path, position):
        self.front_image = pygame.image.load(front_image_path)
        self.front_image = pygame.transform.scale(self.front_image, (150, 250))
        self.back_image = pygame.image.load(back_image_path)
        self.back_image = pygame.transform.scale(self.back_image, (150, 250))
        self.image = self.back_image
        self.rect = self.image.get_rect(center=position)
        self.flipped = False

    def flip(self):
        if self.flipped:
            self.image = self.back_image
        else:
            self.image = self.front_image
        self.flipped = not self.flipped

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def click(self, position):
        return self.rect.collidepoint(position)
    # def shuffle(self):

card1 = Card('card1.png','backcard.png', (200, 300))
card2 = Card('card2.png','backcard.png', (400, 300))
card3 = Card('card3.png','backcard.png', (600, 300))
cards = [card1, card2, card3]

button_positions = [
    (800 // 2, 600 // 2 - 50 - 20),
    (800 // 2, 600 // 2),
    (800 // 2, 600 // 2 + 50 + 20)
]
buttons = [
    Button('How to Play', button_positions[0]),
    Button('Start Game', button_positions[1]),
    Button('Options', button_positions[2])
]

GameOn = True
current_screen = 'welcome'

def howtoplay(screen):
    instructions = [
        "Welcome to 3 Card Monte!",
        "1. The objective of the game is to find the correct",
        " card.",
        "2. Click on a card to flip it.",
        "3. Watch the cards shuffle and try to keep track.",
        "4. Click on the card you think is the correct one.",
        "5. Have fun and try to beat your high score!"
    ]
    text_color = (255, 255, 255)  # White color for text
    y_offset = 50
    for instruction in instructions:
        lines = textwrap.wrap(instruction, width=70)  # Wrap text to fit within 70 characters
        for line in lines:
            text_surface = font.render(line, True, text_color)
            screen.blit(text_surface, (50, y_offset))
            y_offset += 40  # Increase vertical spacing

    # Draw back button
    back_button = Button('Back', (400, 550))
    back_button.draw(screen)
    return back_button

while GameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == 'welcome':
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        if button.text == 'How to Play':
                            current_screen = 'how_to_play'
                        elif button.text == 'Start Game':
                            print("Start Game clicked")
                            current_screen = 'game'
                        elif button.text == 'Options':
                            print("Options clicked")
            elif current_screen == 'game':
                for card in cards:
                    if card.click(mouse_pos):
                        card.flip()
            elif current_screen == 'how_to_play':
                back_button = howtoplay(screen)
                if back_button.is_clicked(mouse_pos):
                    current_screen = 'welcome'
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                GameOn = False


    screen.blit(bg, (0, 0))

    if current_screen == 'welcome':
        screen.blit(bg, (0, 0))
        for button in buttons:
            button.draw(screen)
    elif current_screen == 'game':
        for card in cards:
            card.draw(screen)
    elif current_screen == 'how_to_play':
        back_button = howtoplay(screen)

    pygame.display.flip()

pygame.quit()