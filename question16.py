"""
Imagine you are creating a super mario game.
you need to define a class to represent Mario.
What would it look like? If you aren't familiar with 
super mario, use your own  favorite video or board game to 
model a player.
"""
import random

class Mario():

    object_count=0  #there should only one mario
    enimey_pos_x = random.randrange(0,10)
    enimey_pos_y = 0
    bullet_x = 0
    bullet_y = 0
    def __init__(self):
        Mario.object_count = Mario.object_count + 1
        if(Mario.object_count > 1):
            raise("There should be only one mario at game!")
        else:
            self.life = 3
            self.coins = 0
            self.bullets = 0
            self.level = 0
            self.pos_x = 0
            self.pos_y = 0

    def collide(self):
        if self.pos_x == Mario.enimey_pos_x and self.pos_y == Mario.enimey.pos_y:
            del self
            print('gameover')

    def jump(self):
        self.pos_y += 1

    def  forward(self):
        self.pos_x += 1

    def fire(self):
        if self.bullets > 0:
            self.bullets -= 1

            #bullet with run only for 10m (suppose)
            for i in range(10):
                Mario.bullet_x = self.pos_x
                Mario.bullet_y = i
                if(Mario.enimey_pos_x == Mario.bullet_x and Mario.enimey_pos_y== Mario.bullet_y):
                    del Mario.enimey_pos_x
                    del Mario.enimey_pos_y

    
