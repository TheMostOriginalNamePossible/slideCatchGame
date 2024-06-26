import pygame, simpleGE, random


class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("coin.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        #move to top of screen
        self.y = 10

        #x is random number between 0 and screen width
        self.x = random.randint(0, self.screenWidth)

        #y is random number between min and max speed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("campus.jpg")

        self.sndcoin = simpleGE.Sound("pickupCoin.wav")
        self.numCoins = 10
        self.charlie = Charlie(self)
        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        self.sprites = [self.charlie, self.coins]

    def process(self):
        for coin in self.coins:
            if coin.collidesWith(self.charlie):
                coin.reset()
                self.sndcoin.play()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
