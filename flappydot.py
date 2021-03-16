import tkinter as tk

from gamelib import Sprite, GameApp

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5
STARTING_VELOCITY = -30
JUMP_VELOCITY = -20
PILLAR_SPEED = 10


class Dot(Sprite):
    def init_element(self):
        self.vy = STARTING_VELOCITY
        self.is_strated = False

    def update(self):
        if self.is_strated:
            self.y += self.vy
            self.vy += GRAVITY

    def start(self):
        self.is_strated = True

    def jump(self):
        self.vu = JUMP_VELOCITY
        self.vy = self.vu


class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.elements.append(self.dot)
        self.pillar_pair = PillarPair(self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT // 2)
        self.elements.append(self.pillar_pair)

    def init_game(self):
        self.create_sprites()

        self.is_started = False

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        if event.char == ' ':
            if not self.is_started:
                self.dot.start()
                self.dot.jump()



class PillarPair(Sprite):
    def init_element(self):
        self.vx = PILLAR_SPEED

    def update(self):
        self.x -= self.vx
        if self.x < -30:
            self.x = 800



# commit again
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
