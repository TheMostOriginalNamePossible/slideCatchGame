import pygame, simpleGE, collisionTest

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("campus.jpg")
        self.charlie = Charlie(self)

        self.sprites = [self.charlie]


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
