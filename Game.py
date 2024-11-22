# (Lab) Final Game - CS120_801
# Lanre Yakubu 
"""
Created on Sun Nov 22, 2024
"""

import pygame, simpleGE, random

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("character.png")
        self.setSize(50, 50)
        self.position = (50, 400)
        self.inAir = True
        self.dy = 0
        self.fall_timer = 0

    def process(self):
        if self.inAir:
            self.addForce(0.2, 270)
        
        if self.y > self.scene.screen.get_height() - 50:
            if self.fall_timer > 1.0:
                self.scene.transition_to_instructions = True
                pygame.mixer.Sound("letstryagain.wav").play()
            self.fall_timer += self.scene.gameTimer.getElapsedTime()
            return
        else:
            self.fall_timer = 0

        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy = 0

        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5
        if self.scene.isKeyPressed(pygame.K_UP):
            if not self.inAir:
                self.addForce(5, 90)
                self.inAir = True

        self.inAir = True
        for platform in self.scene.platforms:
            if self.collidesWith(platform):                
                if self.dy > 0:
                    self.bottom = platform.top
                    self.dy = 0
                    self.inAir = False
                    break

class Platform(simpleGE.Sprite):
    def __init__(self, scene, position, speed):
        super().__init__(scene)
        self.position = position
        self.setImage("2dplatform.png")
        self.setSize(50, 20)
        self.moveSpeed = speed
        self.dx = -self.moveSpeed

    def process(self):
        self.x += self.dx
        if self.x < 20:
            self.hide()
            self.y = random.randint(100, 400)
        randomnum = random.randint(1, 100)
        if randomnum <= 2:
            if not self.visible:
                self.show()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bg001.png")
        self.setCaption("arrows to move and jump. drag platforms around")

        self.charlie = Charlie(self)
        self.gameTimer = simpleGE.Timer()
        self.gameTimer.start()
        self.scoreTimer = simpleGE.Timer()
        self.scoreTimer.start()

        self.score = 0
        self.platformSpeed = 2
        self.platforms = [
            Platform(self, (100, 100), self.platformSpeed),
            Platform(self, (150, 250), self.platformSpeed),
            Platform(self, (200, 350), self.platformSpeed),
            Platform(self, (250, 450), self.platformSpeed),
            Platform(self, (300, 350), self.platformSpeed),
            Platform(self, (350, 350), self.platformSpeed),
            Platform(self, (450, 100), self.platformSpeed),
            Platform(self, (350, 150), self.platformSpeed),
            Platform(self, (200, 450), self.platformSpeed),
            Platform(self, (250, 250), self.platformSpeed),
            Platform(self, (300, 350), self.platformSpeed),
            Platform(self, (350, 450), self.platformSpeed),
            Platform(self, (100, 200), self.platformSpeed),
            Platform(self, (150, 450), self.platformSpeed),
            Platform(self, (200, 250), self.platformSpeed),
            Platform(self, (250, 350), self.platformSpeed),
            Platform(self, (100, 400), self.platformSpeed),
            Platform(self, (150, 450), self.platformSpeed),
            Platform(self, (100, 400), self.platformSpeed),
            Platform(self, (150, 450), self.platformSpeed),
            Platform(self, (100, 400), self.platformSpeed),
            Platform(self, (150, 450), self.platformSpeed)
        ]

        self.lblScore = simpleGE.Label()
        self.lblScore.center = (50, 15)
        self.lblTime = simpleGE.Label()
        self.lblTime.center = (60, 50)

        self.sprites = [self.charlie, *self.platforms, self.lblScore, self.lblTime]
        self.gameOver = False
        self.transition_to_instructions = False

        pygame.mixer.music.load("Background_music.wav")
        pygame.mixer.music.play(-1)

    def process(self):
        if self.gameOver:
            return
        if self.transition_to_instructions:
            pygame.mixer.music.stop()
            self.stop()

        super().process()
        current_time = self.gameTimer.getElapsedTime()
        self.lblTime.text = f" Time: {current_time:.2f}s"

        if self.scoreTimer.getElapsedTime() >= 5:
            self.score += 5
            self.platformSpeed += 0.6
            for platform in self.platforms:
                platform.dx = -self.platformSpeed
            self.scoreTimer.start()

        self.lblScore.text = f" Score: {self.score}"

class Instruction(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("bg001.png")
        self.response = "quit"

        self.instruction = simpleGE.MultiLabel()
        self.instruction.textLines = [
            "You are the main character in this adventure.",
            "Navigate using the left and right arrow keys",
            "and jump to stay on the platforms.",
            "Avoid falling off the platforms to keep playing.",
            "Best of luck!"
        ]
        self.instruction.center = (320, 240)
        self.instruction.size = (500, 300)

        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 50)

        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (Up)"
        self.btnPlay.center = (320, 400)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (Down)"
        self.btnQuit.center = (320, 450)

        self.sprites = [self.instruction, self.lblScore, self.btnPlay, self.btnQuit]

    def process(self):
        super().process()
        if self.btnQuit.clicked:
            self.response = "quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "play"
            self.stop()
        if self.isKeyPressed(pygame.K_UP):
            self.response = "play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.response = "quit"
            self.stop()

def main():
    pygame.init()
    keepGoing = True
    score = 0
    while keepGoing:
        instruction = Instruction(score)
        instruction.start()
        if instruction.response == "play":
            game = Game()
            game.start()
            score = game.score
            if game.transition_to_instructions:
                continue
        else:
            keepGoing = False
    pygame.quit()

if __name__ == "__main__":
    main()
