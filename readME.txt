For sake of convenience, if a variable or function is built into simpleGE.py,
they won't be mentioned. The only exception is if a function is redefined.

Imports: pygame, simpleGE, random
Constants: JOSHUA_TIME
    JOSHUA_TIME: the time (in milliseconds) in which Sunny reverts back to INLYSSunny.png
    from INLYSSunnyP.png


Classes: Sound(simpleGE.Sound), Coin(simpleGE.Sprite),
Joshua(Coin), Sunny(simpleGE.Sprite), Game(simpleGE.Scene)

Sound: It's the same as simpleGE.Sound with the addition of a volume setter for convenience.
(It's for convenience of typing since I have multiple sounds)
    Methods: volume(self, value)
        volume(self, value) takes a number between 0.0 to 1.0. spits out 0.5
        if the input isn't a float value.

Coin: It is a coin sprite.
    Variables etc.: self.minSpeed, self.maxSpeed
        minSpeed: an integer that gives the minimum speed at which Coin can fall
        maxSpeed: an integer that gives the maximum speed at which Coin can fall
    Methods: reset(self), checkBounds(self)
        reset(self): brings the the coin to the top of the window at a random x value

        checkBounds(self): checks if the coin has hit the bottom of the screen

Joshua: It's a specialized Coin.
    Variables etc.: self.timing, self.time, self.endTime
        self.timing: it is a bool variable responsible that is set to true
        when we want to keep grabbing runtime. Set to False by default.

        self.time: gives the current runtime in milliseconds.

        self.endTime: gives the end time. it is set to 0 by default

    Methods: resetJ(self)
        resetJ(self): executes reset(self), changes self.timing to True,
        sets self.time to current runtime,
        sets self.endTime = self.time - JOSHUA_TIME

Sunny: It's the player character sprite.
    Variables etc.: self.moveSpeed, self.moveSpeedC
        self.__moveSpeedC: Tells the number of pixels player can move per frame and remains constant.
        created so it can be referenced again by other

        self.moveSpeed: Tells the number of pixels player can move per frame and can be changed.

    Methods: setStopLeft(self), setStopRight(self), process(self)
        checkStopLeft(self): checks if the sprite has reached left border (with wiggle room),
        and sets self.moveSpeed to 0 if it has, otherwise it sets self.moveSpeed to self.__moveSpeedC

        checkStopRight(self): checks if the sprite has reached right border (with wiggle room),
        and sets self.moveSpeed to 0 if it has, otherwise it sets self.moveSpeed to self.__moveSpeedC

        process(self): Tells how the sprite should move. Sets self.moveSpeed to self.moveSpeedC.
        If right arrow is pressed, it runs checkStopRight(self) then moves right at speed of self.moveSpeed.
        If left arrow is pressed, it runs checkStopLeft(self) then moves left at speed of self.moveSpeed.
Game: It holds all game data. Created from a simpleGE.Scene object.
Automatically loads sets volume of music and plays it. Also sets volume of Sound instances.
    Variables etc.: self.joshua, self.sunny, self.numCoins, self.coins
        self.joshua: an instance of Joshua

        self.sunny: an instance of Sunny

        self.numCoins: an integer that gives the number of coins on the screen

        self.coins: a list of coin instances.

        self.sndcoin: the coin collection Sound instance

        self.inlys: Joshua-Sunny collision sound

        self.sprites: a list with all sprite instances

    Methods:process(self), update(self)
        process(self): checks Sunny and Coin collisions and Sunny and Joshua collisions,
        When Sunny and Coin collide, self.sndcoin plays and coin resets.
        When Sunny and Joshua collide, self.inlys plays, and sets the image of self.sunny to
        INLYSSunnyP.png and runs self.joshua.resetJ().
        Tells when should have image of self.sunny set to INLYSSunny.png using

        update(self): checks if the music has stopped, if it has it replays it from the beginning.