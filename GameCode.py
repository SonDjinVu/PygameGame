import pygame
import random
import sys
import copy
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Board:
    def __init__(self, game, copied=False):
        self.board = [['.', '.', '.', '.'],
                      ['.', '.', '.', '.'],
                      ['.', '.', '.', '.'],
                      ['.', '.', '.', '.']]
        self.board[random.randint(0, 3)][random.randint(0, 3)] = 2
        self.game = game
        self.copied = copied

    def get_empty(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == '.':
                    empty.append((i, j))
        return empty

    def create_random(self):
        empty = self.get_empty()
        if empty:
            i, j = random.choice(empty)
            value = random.choice([2] * 9 + [4])
            self.board[i][j] = value

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '.':
                    return False
        return True

    def no_moves(self):
        for move in range(4):
            new_board = Board(game, True)
            new_board.board = copy.deepcopy(self.board)
            move_list = [new_board.up, new_board.down, new_board.left, new_board.right]
            move_list[move]()
            if new_board.board != self.board:
                return False
        return True

    def up(self):
        score = 0
        can_combine = [True, True, True, True]
        move_count = -1
        for j in range(4):
            if '.' not in [self.board[i][j] for i in range(4)] and \
                    self.board[0][j] == self.board[1][j] and \
                    self.board[2][j] == self.board[3][j]:
                self.board[0][j] *= 2
                self.board[1][j] = self.board[2][j] * 2
                self.board[2][j] = '.'
                self.board[3][j] = '.'
                can_combine[j] = False
                score += self.board[0][j] + self.board[1][j]
                if not self.copied:
                    self.game.draw()

        while move_count != 0:
            move_count = 0
            for i in range(1, 4):
                for j in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i - 1][j] == '.':
                            self.board[i][j], self.board[i - 1][j] = self.board[i - 1][j], self.board[i][j]
                            move_count += 1
                        elif self.board[i - 1][j] == self.board[i][j] and can_combine[j]:
                            self.board[i - 1][j] *= 2
                            self.board[i][j] = '.'
                            can_combine[j] = False
                            score += self.board[i - 1][j]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
        return score

    def left(self):
        score = 0
        can_combine = [True, True, True, True]
        move_count = -1

        for i in range(4):
            if '.' not in [self.board[i][j] for j in range(4)] and \
                    self.board[i][0] == self.board[i][1] and \
                    self.board[i][2] == self.board[i][3]:
                self.board[i][0] *= 2
                self.board[i][1] = self.board[i][2] * 2
                self.board[i][2] = '.'
                self.board[i][3] = '.'
                can_combine[i] = False
                score += self.board[i][0] + self.board[i][1]
                if not self.copied:
                    self.game.draw()

        while move_count != 0:
            move_count = 0
            for j in range(1, 4):
                for i in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i][j - 1] == '.':
                            self.board[i][j], self.board[i][j - 1] = self.board[i][j - 1], self.board[i][j]
                            move_count += 1
                        elif self.board[i][j - 1] == self.board[i][j] and can_combine[i]:
                            self.board[i][j - 1] *= 2
                            self.board[i][j] = '.'
                            can_combine[i] = False
                            score += self.board[i][j - 1]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
        return score

    def down(self):
        can_combine = [True, True, True, True]
        score = 0
        move_count = -1
        for j in range(4):
            if '.' not in [self.board[i][j] for i in range(4)] and \
                    self.board[0][j] == self.board[1][j] and \
                    self.board[2][j] == self.board[3][j]:
                self.board[3][j] *= 2
                self.board[2][j] = self.board[1][j] * 2
                self.board[1][j] = '.'
                self.board[0][j] = '.'
                can_combine[j] = False
                score += self.board[3][j] + self.board[2][j]
                if not self.copied:
                    self.game.draw()

        while move_count != 0:
            move_count = 0
            for i in [2, 1, 0]:
                for j in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i + 1][j] == '.':
                            self.board[i][j], self.board[i + 1][j] = self.board[i + 1][j], self.board[i][j]
                            move_count += 1
                        elif self.board[i + 1][j] == self.board[i][j] and can_combine[j]:
                            self.board[i + 1][j] *= 2
                            self.board[i][j] = '.'
                            can_combine[j] = False
                            score += self.board[i + 1][j]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
        return score

    def right(self):
        can_combine = [True, True, True, True]
        score = 0
        move_count = -1
        for i in range(4):
            if '.' not in [self.board[i][j] for j in range(4)] and \
                    self.board[i][0] == self.board[i][1] and \
                    self.board[i][2] == self.board[i][3]:
                self.board[i][3] *= 2
                self.board[i][2] = self.board[i][1] * 2
                self.board[i][1] = '.'
                self.board[i][0] = '.'
                can_combine[i] = False
                score += self.board[i][3] + self.board[i][2]
                if not self.copied:
                    self.game.draw()

        while move_count != 0:
            move_count = 0
            for j in [2, 1, 0]:
                for i in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i][j + 1] == '.':
                            self.board[i][j], self.board[i][j + 1] = self.board[i][j + 1], self.board[i][j]
                            move_count += 1
                        elif self.board[i][j + 1] == self.board[i][j] and can_combine[i]:
                            self.board[i][j + 1] *= 2
                            self.board[i][j] = '.'
                            can_combine[i] = False
                            score += self.board[i][j + 1]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
        return score

    def __str__(self):
        string = ''
        for row in self.board:
            for cell in row:
                string += str(cell)
                if len(str(cell)) == 1:
                    string += '   '
                elif len(str(cell)) == 2:
                    string += '  '
                elif len(str(cell)) == 3:
                    string += ' '

            string += '\n'
        return string.strip()


class Cell(pygame.sprite.Sprite):
    colors = {'.': (180, 180, 180), 2: (230, 230, 230), 4: (255, 255, 140), 8: (255, 200, 100), 16: (200, 30, 10), 32: (200, 30, 40), 64: (230, 30, 30),
              128: (255, 255, 80), 256: (255, 255, 60), 512: (255, 255, 40), 1024: (255, 255, 20), 2048: (255, 255, 0)}

    def __init__(self, pos, width=100, height=100, value=2):
        myFont = pygame.font.Font('freesansbold.ttf', 40)
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.value = value
        self.rect = Rect(0, 0, self.width, self.height)
        self.rect.center = pos
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color(self.colors[self.value]))

        self.label = myFont.render(str(self.value), 1, (0, 0, 0))
        self.labelrect = self.label.get_rect()
        self.imagerect = self.image.get_rect()
        self.labelrect.center = self.imagerect.center
        if self.value != '.':
            self.image.blit(self.label, self.labelrect)

    def update(self, direction):
        pass


class GameMain():
    done = False
    color_bg = Color((76, 76, 76))

    def __init__(self, width=550, height=550, high_score=0):
        pygame.init()
        self.game_over = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.board = Board(self)
        self.score = 0
        try:
            if high_score == 0:
                with open("high_score.txt", "rb") as f:
                    self.high_score = int(f.read().strip())
        except:
            self.high_score = high_score

    def draw_board(self):
        self.cells = pygame.sprite.Group()

        cur_x, cur_y = 100, 100
        for row in self.board.board:
            for square in row:
                new_cell = Cell((cur_x, cur_y), value=square)
                self.cells.add(new_cell)
                cur_x += 110
            cur_y += 110
            cur_x = 100
        self.cells.draw(self.screen)

    def main_loop(self):
        while not self.done:
            self.handle_events()

            if self.score > self.high_score:
                self.high_score = self.score

            self.draw()
            self.clock.tick(30)
            if self.board.no_moves():
                self.game_over = True
                self.end_screen = pygame.Surface((500, 500))
                self.end_screen_rect = self.end_screen.get_rect()
        with open("high_score.txt", 'wb') as f:
            f.write(str(self.high_score))
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(self.color_bg)
        if self.game_over:
            self.game_over_label1 = self.font.render("Game Over", 1, (255, 255, 255))
            self.game_over_label2 = self.font.render("Final Score: %d" % (self.score), 1, (255, 255, 255))
            self.game_over_label3 = self.font.render("Press Space Bar to Play Again", 1, (255, 255, 255))
            self.end_screen.blit(self.game_over_label1, (175, 50))
            self.end_screen.blit(self.game_over_label2, (150, 100))
            self.end_screen.blit(self.game_over_label3, (75, 470))
            self.screen.blit(self.end_screen, (25, 25))
        else:
            self.draw_board()
            self.score_label = self.font.render("Score: %d" % (self.score), 1, (255, 255, 255))
            self.screen.blit(self.score_label, (50, 10))
            self.hiscore_label = self.font.render("High Score: %d" % (self.high_score), 1, (255, 255, 255))
            self.screen.blit(self.hiscore_label, (320, 10))
        pygame.display.update()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN and not self.game_over:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    self.current_board = copy.deepcopy(self.board.board)
                    if event.key == K_UP:
                        self.score += self.board.up()
                    elif event.key == K_DOWN:
                        self.score += self.board.down()
                    elif event.key == K_LEFT:
                        self.score += self.board.left()
                    elif event.key == K_RIGHT:
                        self.score += self.board.right()

                    if self.current_board != self.board.board:
                        self.board.create_random()
            elif event.type == KEYDOWN and self.game_over:
                if event.key == K_SPACE:
                    self.__init__(high_score=self.high_score)


if __name__ == "__main__":
    game = GameMain()
    game.main_loop()