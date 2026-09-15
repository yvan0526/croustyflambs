import pygame

class Message:

    def __init__(self, screen):
        self.font = pygame.font.Font("assets/EarlyGameBoy.ttf", 8)
        self.screen = screen
        self.text = ""
        self.button_text = ""
        self.active = False
        self.button_rect = pygame.Rect(0, 0, 80, 30)

    def show(self, text, button_text):
        """Active l'affichage d'un nouveau message"""
        self.text = text
        self.button_text = button_text
        self.active = True
        text_width = self.font.size(button_text)[0]
        self.button_rect.width = max(80, text_width + 30)

    def hide(self):
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.button_rect.collidepoint(event.pos):
                self.hide()
                return True
        return False

    def wrap_text(self, text, max_width):
        wrapped_lines = []
        for paragraph in text.split("\n"):
            if paragraph == "":
                wrapped_lines.append("")
                continue

            words = paragraph.split(" ")
            current_line = ""
            for word in words:
                test_line = (current_line + " " + word).strip()
                if self.font.size(test_line)[0] <= max_width:
                    current_line = test_line
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
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 210))
        self.screen.blit(overlay, (0, 0))

        # Texte, avec retour à la ligne automatique
        margin = 20
        max_width = self.screen.get_width() - 2 * margin
        lines = self.wrap_text(self.text, max_width)

        line_height = self.font.get_height()
        total_text_height = len(lines) * line_height
        start_y = self.screen.get_height() // 2 - total_text_height // 2

        for i, line in enumerate(lines):
            line_image = self.font.render(line, True, "white")
            line_rect = line_image.get_rect(
                center=(self.screen.get_width() // 2, start_y + i * line_height)
            )
            self.screen.blit(line_image, line_rect)

        # Bouton OK, positionné sous le texte (contraint à rester dans l'écran)
        button_y = start_y + total_text_height + 40
        max_y = self.screen.get_height() - self.button_rect.height // 2 - 10
        button_y = min(button_y, max_y)

        self.button_rect.center = (self.screen.get_width() // 2, button_y)
        pygame.draw.rect(self.screen, "black", self.button_rect, border_radius=4)
        pygame.draw.rect(self.screen, "white", self.button_rect, width=2, border_radius=4)
        button_image = self.font.render(self.button_text, True, "white")
        button_rect = button_image.get_rect(center=self.button_rect.center)
        self.screen.blit(button_image, button_rect)