from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor


app = Ursina()


rass_block = load_texture("assets/rass block.jpg")
sky_texture = load_texture("assets/sky.jpg")
dirt_texture = load_texture("assets/dirt.jpg")
stone_texture = load_texture("assets/stone.png")
oak_texture = load_texture("assets/oak.png")
iron_texture = load_texture("assets/iron.jpg")

current_texture = rass_block

def update():
    global current_texture
    if held_keys['1']:current_texture = rass_block
    if held_keys['2']:current_texture = dirt_texture
    if held_keys['3']:current_texture = oak_texture
    if held_keys['4']:current_texture = stone_texture
    if held_keys['5']:current_texture = iron_texture


    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()    


def input(key):
    if key  == 'p':
        quit()


noise = PerlinNoise(octaves=2,seed=420690)
amp = 3
freq = 12

class sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            scale = 150,
            texture = sky_texture,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2,0.3),
            color = color.white,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4)

        )     
    def active(self):
        self.position = Vec2(0.1,-0.5)
        self.rotation = Vec3(90, -10, 0)  

    def passive(self):
        self.rotation=Vec3(150, -10, 0)
        self.position=Vec2(0.4, -0.4)
                

class Voxel(Button):
    def __init__(self, position = (0,0,0) , texture=rass_block):
        super().__init__(
            parent = scene,
            model='cube',
            color=color.white,
            highlight_color=color.lime,
            texture=texture,
            position = position,
            origin_y = 0.5
        )
    def input(self,key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel(position= self.position + mouse.normal, texture=current_texture)
            if key == "left mouse down":
                destroy(self) 

for z in range(25):
    for x in range(25):
        voxel = Voxel((x,0,z))









player = FirstPersonController()
sky = Sky()
hand = Hand()


app.run()