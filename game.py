#coding:utf8
#py3 pip install pygame
#py3 pip install pytmx
#py3 pip install pyscroll
import pygame, pytmx, pyscroll
from player import *
from tiles import Tile
#import sauvegarde

tileD5 = Tile("TILE_D5", "")
tileE6 = Tile("TILE_E6", "LFD/Map/TileE6/tileE6.tmx")
tileF5 = Tile("TILE_F5", "")
tileE4 = Tile("TILE_E4", "")
tileE5 = Tile("TILE_E5", "LFD/Map/TileE5/tileE5.tmx", tileD5, tileE6, tileF5, tileE4)

class Game:
    def __init__(self):
        # Création de la fenêtre
        self.screen=pygame.display.set_mode((400,400))
        pygame.display.set_caption("Light Fight of Darkness 0.0.1.0")

        # Chargement de la tuile principale (tmx)
        self.current_map="TILE_E5"
        tmx_data=pytmx.util_pygame.load_pygame("LFD/Map/TileE5/tileE5.tmx")
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # Création du joueur (placement automatique)
        player_position=tmx_data.get_object_by_name("player")
        self.player=Player(player_position.x,player_position.y)
        # Dessin du groupe de calques
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=10)
        self.group.add(self.player)
        # Gestion des collisions
        self.walls=[]
        for obj in tmx_data.objects:
            if obj.type=="collision":
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        
        # ----- Définit les différentes collisions pour changer de tuile -----
        # Collision de passage de E5 à E4
        switch_e4=tmx_data.get_object_by_name("E5-E4")
        self.switch_e5_e4=pygame.Rect(switch_e4.x,switch_e4.y,switch_e4.width,switch_e4.height)
        # Collision de passage de E5 à D5
        switch_d5=tmx_data.get_object_by_name("E5-D5")
        self.switch_e5_d5=pygame.Rect(switch_d5.x,switch_d5.y,switch_d5.width,switch_d5.height)
        # Collision de passage de E5 à F5
        switch_f5=tmx_data.get_object_by_name("E5-F5")
        self.switch_e5_f5=pygame.Rect(switch_f5.x,switch_f5.y,switch_f5.width,switch_f5.height)
        # Collision de passage de E5 à E6
        switch_e6=tmx_data.get_object_by_name("E5-E6")
        self.switch_e5_e6=pygame.Rect(switch_e6.x,switch_e6.y,switch_e6.width,switch_e6.height)
        # Collision d'entrée de la maison
        enter_houseH=tmx_data.get_object_by_name("entreMaison1-E5")
        self.house1_e5=pygame.Rect(enter_houseH.x,enter_houseH.y,enter_houseH.width,enter_houseH.height)

    #Récupère les touches enfoncées par l'utilisateur
    def handle_input(self):
        #Récupère la touche enfoncée
        pressed=pygame.key.get_pressed()
        #Déplace le joueur vers le haut
        if pressed[pygame.K_z]:
            self.player.change_animation("up")
            self.player.move_up()
        #Déplace le joueur vers le bas
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation("down")
        #Déplace le joueur vers la gauche
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation("left")
        #Déplace le joueur vers la droite
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation("right")
        else:pass
    
    # -------- ZONE DESERT --------



    # -------- ZONE PLAINE --------

    # TUILE E5

    def switch_E5_house1(self):
        self.current_map="HOUSE1_E5"

        # Chargement de la tuile (tmx)
        tmx_data=pytmx.util_pygame.load_pygame("Map/HouseH/houseH.tmx")
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        # Dessin du groupe de calques
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=10)
        self.group.add(self.player)

        # Gestion des collisions
        self.walls=[]
        for obj in tmx_data.objects:
            if obj.type=="collision":
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        
        # Définit l'entrée/sortie de la maison (collision)
        exit_houseH=tmx_data.get_object_by_name("exit_houseH")
        self.house1_e5=pygame.Rect(exit_houseH.x,exit_houseH.y,exit_houseH.width,exit_houseH.height)

        # Définit le spawn du joueur
        spawn_point=tmx_data.get_object_by_name("houseH_spawn")
        self.player.position[0]=spawn_point.x
        self.player.position[1]=spawn_point.y-20

    def switch_house1_E5(self):
        """
        Change de tuile (Maison -> E5), spawn devant la maison.
        """
        self.current_map="TILE_E5"
        # Chargement de la carte (tmx)
        tmx_data=pytmx.util_pygame.load_pygame("Map/TileE5/tileE5.tmx")
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # Dessin du groupe de calques
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=10)
        self.group.add(self.player)
        # Gestion des collisions
        self.walls=[]
        for obj in tmx_data.objects:
            if obj.type=="collision":
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        # Définit l'entrée/sortie de la maison (collision)
        enter_houseH=tmx_data.get_object_by_name("entreMaison1-E5")
        self.house1_e5=pygame.Rect(enter_houseH.x,enter_houseH.y,enter_houseH.width,enter_houseH.height)
        # Définit le point de spawn du joueur
        spawn_point=tmx_data.get_object_by_name("sortieMaison1-E5")
        self.player.position[0]=spawn_point.x
        self.player.position[1]=spawn_point.y+15

    def switch_E5_E6(self):
        """
        Change de tuile (E5 -> E6), donc le joueur spawn à l'ouest.
        """
        self.current_map="TILE_E6"
        # Chargement de la carte (tmx)
        tmx_data=pytmx.util_pygame.load_pygame("Map/TileE6/tileE6.tmx")
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # Dessin du groupe de calques
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=10)
        self.group.add(self.player)

        # Définit le point de spawn du joueur
        #spawn_point=tmx_data.get_object_by_name("West-E6")
        self.player.position[0]=32 #spawn_point.x
        self.player.position[1]=157 #spawn_point.y

        # ----- COLLISIONS -----
        self.walls=[]
        for obj in tmx_data.objects:
            if obj.type=="collision":
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        
        # ----- Définit les différentes collisions pour changer de tuile -----
        # Collision de passage de E6 à E5
        switch_E5=tmx_data.get_object_by_name("E6-E5")
        self.switch_e6_e5=pygame.Rect(switch_E5.x,switch_E5.y,switch_E5.width,switch_E5.height)
        # Collision de passage de E6 à D6
        switch_D6=tmx_data.get_object_by_name("E6-D6")
        self.switch_e6_d6=pygame.Rect(switch_D6.x,switch_D6.y,switch_D6.width,switch_D6.height)
        # Collision de passage de E6 à F6
        switch_F6=tmx_data.get_object_by_name("E6-F6")
        self.switch_e6_f6=pygame.Rect(switch_F6.x,switch_F6.y,switch_F6.width,switch_F6.height)


    # TUILE E6

    def switch_E6_E5(self):
        """
        Change de tuile (E6 -> E5), spawn à l'ouest.
        """
        self.current_map="TILE_E5"
        # Chargement de la carte (tmx)
        tmx_data=pytmx.util_pygame.load_pygame("Map/TileE5/tileE5.tmx")
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # Dessin du groupe de calques
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=10)
        self.group.add(self.player)

        # ----- COLLISIONS -----
        self.walls=[]
        for obj in tmx_data.objects:
            if obj.type=="collision":
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))

        # ----- Définit les différentes collisions pour changer de tuile -----
        # Collision de passage de E5 à E4
        switch_e4=tmx_data.get_object_by_name("E5-E4")
        self.switch_e5_e4=pygame.Rect(switch_e4.x,switch_e4.y,switch_e4.width,switch_e4.height)
        # Collision de passage de E5 à D5
        switch_d5=tmx_data.get_object_by_name("E5-D5")
        self.switch_e5_d5=pygame.Rect(switch_d5.x,switch_d5.y,switch_d5.width,switch_d5.height)
        # Collision de passage de E5 à F5
        switch_f5=tmx_data.get_object_by_name("E5-F5")
        self.switch_e5_f5=pygame.Rect(switch_f5.x,switch_f5.y,switch_f5.width,switch_f5.height)
        # Collision de passage de E5 à E6
        switch_e6=tmx_data.get_object_by_name("E5-E6")
        self.switch_e5_e6=pygame.Rect(switch_e6.x,switch_e6.y,switch_e6.width,switch_e6.height)
        # Collision d'entrée de la maison
        enter_houseH=tmx_data.get_object_by_name("entreMaison1-E5")
        self.house1_e5=pygame.Rect(enter_houseH.x,enter_houseH.y,enter_houseH.width,enter_houseH.height)

        # Définit le point de spawn du joueur
        spawn_point=tmx_data.objects_by_name("Est-E5")
        self.player.position[0]=spawn_point.x-20
        self.player.position[1]=spawn_point.y



    def update(self):
        self.group.update()
        # -------- CHANGEMENTS DE TUILE --------
        # TUILE E5
        if self.current_map=="TILE_E5":
            if self.player.feet.colliderect(self.house1_e5):
                self.switch_E5_house1()
            elif self.player.feet.colliderect(self.switch_e5_d5):
                self.switch_E5_D5()
            elif self.player.feet.colliderect(self.switch_e5_e6):
                self.switch_E5_E6()
        
        # MAISON E5
        elif self.current_map=="HOUSE1_E5":
            if self.player.feet.colliderect(self.house1_e5):
                self.switch_house1_E5()
            
        # TUILE E6
        elif self.current_map=="TILE_E6":
            if self.player.feet.colliderect(self.switch_e6_e5):
                self.switch_E6_E5()

        # MECANISME DE COLLISION
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls)>-1:
                sprite.move_back()

    # Lance le jeu
    def run(self):
        clock=pygame.time.Clock()
        running=True
        while running:
            # Mémorise la position du joueur
            self.player.save_location()
            # Fait se déplacer le joueur
            self.handle_input()
            # Rafraîchit la carte
            self.update()
            # Centre le joueur
            self.group.center(self.player.rect.center)
            # Dessine la carte
            self.group.draw(self.screen)
            pygame.display.flip()
            # Sert à fermer la fenetre
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                
            # On attend un peu sinon le joueur se tp
            clock.tick(70)
        pygame.quit()
