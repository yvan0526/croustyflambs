from typing import LiteralString

import pygame
from pygame import Surface
from pygame import Rect
from pygame.ftfont import Font

class Message:

    def __init__(self, screen: Surface, font: Font):
        self.font: Font = font
        self.screen: Surface = screen
        self.text: str = ""
        self.button_text: str = ""
        self.active: bool = False
        self.button_rect: Rect = pygame.Rect(0, 50, 80, 30)

    def show(self, text: str, button_text: str):
        """Active l'affichage d'un nouveau message"""
        self.text = text
        self.button_text = button_text
        self.active = True
        text_width: int = self.font.size(button_text)[0]
        self.button_rect.width = max(80, text_width + 30)

    def hide(self):
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.button_rect.collidepoint(event.pos):
                self.hide()
                return True
        return False

    def wrap_text(self, text: str, max_width: int):
        wrapped_lines: list = []
        for paragraph in text.split("\n"):
            if paragraph == "":
                wrapped_lines.append("")
                continue

            words: list = paragraph.split(" ")
            current_line: str = ""
            for word in words:
                test_line: str = (current_line + " " + word).strip()
                if self.font.size(test_line)[0] <= max_width:
                    current_line: str = test_line
                else:
                    if current_line:
                        wrapped_lines.append(current_line)
                    current_line = word
            wrapped_lines.append(current_line)
        return wrapped_lines

    def draw(self):
        if not self.active:
            return

        # Fond semi-transparent sur tout l'écran
        overlay: Surface = Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        self.screen.blit(overlay, (0, 0))

        # Texte, avec retour à la ligne automatique
        margin: int = 20
        max_width = self.screen.get_width() - 2 * margin
        lines = self.wrap_text(self.text, max_width)

        line_height = self.font.get_height() +5
        total_text_height = len(lines) * line_height
        start_y = self.screen.get_height() // 2 - total_text_height // 2

        for i, line in enumerate(lines):
            line_image = self.font.render(line, True, "white")
            line_rect: Rect = line_image.get_rect(
                center=(self.screen.get_width() // 2, start_y + i * line_height)
            )
            self.screen.blit(line_image, line_rect)

        # Bouton OK, positionné sous le texte (contraint à rester dans l'écran)
        button_y: int = start_y + total_text_height + 40
        max_y: int = self.screen.get_height() - self.button_rect.height // 2 - 10
        button_y = min(button_y, max_y)
        self.button_rect.center = (self.screen.get_width() // 2, button_y)
        pygame.draw.rect(self.screen, "black", self.button_rect, border_radius=4)
        pygame.draw.rect(self.screen, "white", self.button_rect, width=2, border_radius=4)
        button_image = self.font.render(self.button_text, True, "white")
        button_rect: Rect = button_image.get_rect(center=self.button_rect.center)
        self.screen.blit(button_image, button_rect)