#coding:utf8
#py3 pip install pygame

import pygame

class Player(pygame.sprite.Sprite):
    lvlLimit=100
    def __init__(self,x,y):
        super().__init__()
        #Définit les stats du joueur
        self._pdv=10
        self._atk=1
        self._deF=1
        self._exp=0
        self._lvl=1
        self.speed=3
        #Définit le sprite du joueur
        self.sprite_sheet=pygame.image.load("Entities/player2.png")
        self.image=self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect=self.image.get_rect()
        self.position=[x,y]
        self.images={
            "down":self.get_image(0,0),
            "left":self.get_image(0,32),
            "right":self.get_image(0,64),
            "up":self.get_image(0,96)
        }

        #Définit les hitbox du joueur
        self.feet=pygame.Rect(0,0,self.rect.width*0.5,12)
        self.old_position=self.position.copy()

    #Enregistre la position précédente du joueur
    def save_location(self):
        self.old_position=self.position.copy()
    
    #Change le sprite du joueur en fct de sa direction de déplacement
    def change_animation(self,name):
        self.image=self.images[name]
        self.image.set_colorkey((0,0,0))

    #Déplace le joueur
    def move_up(self):self.position[1]-=self.speed
    def move_down(self):self.position[1]+=self.speed
    def move_left(self):self.position[0]-=self.speed
    def move_right(self):self.position[0]+=self.speed

    #Actualise la position de la caméra par rapport au joueur
    def update(self):
        self.rect.topleft=self.position
        self.feet.midbottom=self.rect.midbottom
    
    def move_back(self):
        self.position=self.old_position
        self.rect.topleft=self.position
        self.feet.midbottom=self.rect.midbottom
    
    def get_image(self,x,y):
        # Surface d'affichage du sprite
        image=pygame.Surface([32,32])
        # Affiche le sprite
        image.blit(self.sprite_sheet,(0,0), # Pour décaler le sprite dans la surface d'affichage
        (x,y,32,32)) # Pour découper le sprite en "morceaux" et les afficher
        return image
    

    