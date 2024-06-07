For sake of convenience, if a variable or method is built into simpleGE.py,
they won't be mentioned. This applies to redefined variables. The only exception is if a method is redefined.
Also, __init__ isn't mentioned.


Imports: pygame, simpleGE, random

Constants: JOSHUA_TIME, TOTAL_TIME

    JOSHUA_TIME: the time (in seconds) in which Sunny it takes before reverting back to INLYSSunny.png
    from INLYSSunnyP.png

    TOTAL_TIME: The time at which the game timer starts

Classes: LblTimer(simpleGE.Label), LblScore(simpleGE.Label), Sound(simpleGE.Sound), Coin(simpleGE.Sprite),
Joshua(Coin), Sunny(simpleGE.Sprite), Instructions(simpleGE.Scene), Game(simpleGE.Scene),


LblScore: It's a sprite that displays the score.


LblTimer: It's a sprite that displays the time.


Sound: It's the same as simpleGE.Sound with the addition of a volume setter for convenience.
(It's for convenience of typing.)

    Methods: volume(self, value)

        volume(self, value) takes a number between 0.0 to 1.0. spits out 0.5
        if the input isn't a float value.


Coin: It is a coin sprite.

    Variables etc.: self.minSpeed, self.maxSpeed, self.value

        self.minSpeed: an integer that gives the minimum speed at which Coin can fall

        self.maxSpeed: an integer that gives the maximum speed at which Coin can fall

        self.value: an integer that tells how many points Coin is worth

    Methods: reset(self), checkBounds(self)

        reset(self): brings the the coin to the top of the window at a random x value. This is also run on creation.


        checkBounds(self): checks if the coin has hit the bottom of the screen


Joshua: It's a Coin object that has negative value.


Sunny: It's the player character sprite.

    Variables etc.: self.moveSpeed, self.__moveSpeedC

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


Game: It holds all game data and loads all necessary. Created from a simpleGE.Scene object.

    Variables etc.: self.joshuas, self.sunny, self.numCoins, self.coins, self.sndcoin, self.inlys, self.sprites,
    self.timer

        self.joshuas: an list of instances of Joshua

        self.sunny: an instance of Sunny

        self.numCoins: an integer that gives the number of coins on the screen

        self.numJoshuas: an integer that gives the number of Joshuas on the screen

        self.coins: a list of coin instances.

        self.sndcoin: the coin collection Sound instance

        self.sndinlys: Joshua-Sunny collision sound

        self.sprites: a list with all sprite instances

        self.timer: a simpleGE.Timer instance

        self.timerJ: a simpleGE.Timer instance specifically for keep track of time after Joshua-Sunny collisions

        self.timingJ: a boolean variable that tells whether the timerJ is on.

    Methods:process(self), update(self)

        process(self): checks Sunny and Coin collisions and Sunny and Joshua collisions,
        When Sunny and Coin collide, self.sndcoin plays and coin resets.
        When Sunny and Joshua collide, self.sndinlys plays, and sets the image of self.sunny to
        INLYSSunnyP.png and runs self.joshua.resetJ() and changes the score based on joshua.value
        Tells when should have image of self.sunny set to INLYSSunny.png using

        update(self): checks if the music has stopped. If it has, it replays it from the beginning.
        updates the time displayed and checks if it goes below zero. If it does, it goes back to
        Instructions.


Instructions: It has instructions and a play and quit button.

    Variables etc.: self.s, self.prevScore, self.directions, self.btnStart, self.btnQuit, self.lblPrevScore
    self.sprites

        self.s: boolean variable that tells main whether to create the game instance or not.
        Set to False by default

        self.prevScore: stores the score from the previous game. Set to 0 by default.

        self.directions: a simpleGE.MultiLabel instance. It is used to display the instructions.

        self.btnStart: a simpleGE.Button instance. It plays the game when clicked.

        self.btnQuit: a simpleGE.Button instance. It quits the game when clicked.

        self.lblPrevScore: a simpleGE.Label instance. It is used to display the score from the previous game.

    Methods: update(self)

        update(self): If start is clicked, it sets self.s to True and quits the instructions.
        If quit is clicked, it quits the instructions.


main: runs the game and instructions. It also pulls score for the game and puts it in Instructions
to display previous score.

    Variables: lastScore, game, instructions

        lastScore: variable that stores the score from the previous game

        game: stores the Game instance

        instructions: stores the Instructions instance

