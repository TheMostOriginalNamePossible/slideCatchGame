import simpleGE, pygame, random
JOSHUA_TIME = 1800


class Sound(simpleGE.Sound):
    def __init__(self, file):
        self.sound = pygame.mixer.Sound(file)

    def volume(self, value):
        if type(value) == float:
            self.sound.set_volume(value)
        else:
            self.sound.set_volume(0.5)


class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("steak.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        # move to top of screen
        self.y = 10

        # x is random number between 0 and screen width
        self.x = random.randint(0, self.screenWidth)

        # y is random number between min and max speed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Joshua(Coin):
    def __init__(self, scene):
        super().__init__(scene)
        self.timing = False
        self.time = pygame.time.get_ticks()
        self.endTime = 0

        self.setImage("Joshua.png")
        self.setSize(75, 75)
        self.minSpeed = 6
        self.maxSpeed = 9
        self.reset()

    def resetJ(self):
        self.reset()

        self.time = pygame.time.get_ticks()
        self.endTime = pygame.time.get_ticks() + JOSHUA_TIME
        self.timing = True


class Sunny(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)

        self.setImage("INLYSSunny.png")
        self.setSize(60, 60)
        self.position = (320, 400)
        self.__moveSpeedC = 5
        self.moveSpeed = self.__moveSpeedC
        self.boundAction = self.STOP

    def setStopLeft(self):
        if self.left+29 < 0:
            self.moveSpeed = 0
        else:
            self.moveSpeed = self.__moveSpeedC

    def setStopRight(self):
        if self.right-29 > self.screenWidth:
            self.moveSpeed = 0
        else:
            self.moveSpeed = self.__moveSpeedC

    def process(self):
        self.moveSpeed = self.__moveSpeedC
        if self.isKeyPressed(pygame.K_LEFT):
            self.setStopLeft()
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.setStopRight()
            self.x += self.moveSpeed


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pygame.mixer.music.load("neverlikedyoursmile.mp3")
        pygame.mixer.music.set_volume(0.2)
        self.setImage("scenepark.png")

        self.joshua = Joshua(self)
        self.sunny = Sunny(self)

        self.numCoins = 10
        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))

        self.sndcoin = Sound("eatingsound.mp3")
        self.sndcoin.volume(0.3)
        self.sndinlys = Sound("inlys.mp3")
        self.sndinlys.volume(0.3)

        self.sprites = [self.sunny, self.coins, self.joshua]

        pygame.mixer.music.play()

    def process(self):
        for coin in self.coins:
            if coin.collidesWith(self.sunny):
                coin.reset()
                self.sndcoin.play()

        if self.joshua.collidesWith(self.sunny):
            self.sndinlys.play()
            self.sunny.setImage("INLYSSunnyP.png")
            self.sunny.setSize(60, 60)
            self.joshua.resetJ()

        if self.joshua.timing:
            self.joshua.time = pygame.time.get_ticks()
            if self.joshua.time >= self.joshua.endTime:
                self.sunny.setImage("INLYSSunny.png")
                self.sunny.setSize(60, 60)
                self.joshua.timing = False
                self.joshua.endTime = 0
                self.joshua.time = 0

    def update(self):
        isPlaying = pygame.mixer.music.get_busy()
        if not isPlaying:
            pygame.mixer.music.play()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
