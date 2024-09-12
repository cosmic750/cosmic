import random
import sys
import pygame
import itertools
import json
import os

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
cloud = pygame.image.load('R.jpg').convert_alpha()
cloud1 = pygame.image.load('R - Copy.jpg').convert_alpha()
info = pygame.image.load('R.png').convert_alpha()
info_h = pygame.image.load('R (1).png').convert_alpha()
back_arrow = pygame.image.load('d.png').convert_alpha()
ba_h = pygame.image.load('d1.png').convert_alpha()
nxt_pg = pygame.image.load('e.png').convert_alpha()
nxt_pg_h = pygame.image.load('e1.png').convert_alpha()
shopping_icon = pygame.image.load('shopping icon.png').convert_alpha()
shopping_icon_h = pygame.image.load('shopping icon hover.png').convert_alpha()
coin = pygame.image.load('coin.png').convert_alpha()
coin_s = pygame.image.load('coin_s.png').convert_alpha()
settings_icon = pygame.image.load('gear-icon-png-10.png').convert_alpha()
settings_icon_h = pygame.image.load('gear-icon-png-11.png').convert_alpha()
play_button = pygame.image.load('start-green-play-icon-1.png').convert_alpha()
play_button_h = pygame.image.load('start-green-play-icon-2.png').convert_alpha()
bar_chart = pygame.image.load('bar-chart-transparent.png').convert_alpha()
bar_chart_h = pygame.image.load('bar-chart-transparent1.png').convert_alpha()
spin_wheel = pygame.image.load('spinning wheel.png').convert_alpha()
spin_wheel_h = pygame.image.load('spinning wheel1.png').convert_alpha()
home_icon = pygame.image.load('home_icon.png').convert_alpha()
home_icon_h = pygame.image.load('home_icon1.png').convert_alpha()
alien1 = pygame.image.load('alien.png').convert_alpha()
cn1 = pygame.image.load('chicken_n.png').convert_alpha()
flower1 = pygame.image.load('flower.png').convert_alpha()
mars1 = pygame.image.load('mars.png').convert_alpha()
plane1 = pygame.image.load('plane.png').convert_alpha()
smurf1 = pygame.image.load('smurf.png').convert_alpha()
exit_icon = pygame.image.load('exit icon.png').convert_alpha()
shield = pygame.image.load('shield.png').convert_alpha()
image = pygame.image.load('cloud.png').convert_alpha()

skrub = True

alpha_value = 255

image.set_alpha(128)

processed_objects = set()
processed_objects1 = set()
processed_obj = set()
processed_obj1 = set()
pro_obj = set()
pro_obj1 = set()
process_object = set()
process_object1 = set()
ChosenTime = 0
CTime = 0
ChooseTime = 0
ChooseT = 0

true = True
false = False

rainbow_colours = [
    (255, 0, 0),  # Red
    (255, 64, 0),  # Red-Orange
    (255, 127, 0),  # Orange
    (255, 191, 0),  # Orange-Yellow
    (255, 255, 0),  # Yellow
    (128, 255, 0),  # Yellow-Green
    (0, 255, 0),  # Green
    (0, 191, 128),  # Green-Cyan
    (0, 128, 255),  # Cyan
    (0, 0, 255),  # Blue
    (44, 0, 239),  # Blue-Indigo
    (88, 0, 239),  # Indigo
    (118, 0, 225),  # Indigo-Violet
    (148, 0, 211)  # Violet
]

color_cycle = itertools.cycle(rainbow_colours)
player_colour = next(color_cycle)  # Initialize block color

frame_count = 0  # Frame counter

restart_button_color = (0, 0, 0)
restart_button_rect = pygame.Rect(233.3, 450, 150, 50)
home_button_rect = pygame.Rect(635, 450, 150, 50)
back_rect = back_arrow.get_rect(bottomleft=(20, 580))
next_rect = nxt_pg.get_rect(bottomright=(880, 580))
info_rect = info.get_rect(topright=(880, 100))
shop_rect = shopping_icon.get_rect(topleft=(90, 80))
settings_rect1 = settings_icon.get_rect(midtop=(500, 100))
play_rect = play_button.get_rect(midbottom=(500, 500))
back_rect1 = back_arrow.get_rect(midleft=(10, 300))
bar_chart_rect = bar_chart.get_rect(bottomleft=(105, 500))
wheel_rect = spin_wheel.get_rect(bottomright=(911, 510))
home_rect = home_icon.get_rect(midright=(950, 300))
pygame.display.set_caption('Cosmic Ascension')
font = pygame.font.SysFont('Trebuchet MS', 50)
font1 = pygame.font.SysFont('Trebuchet MS', 30)
font2 = pygame.font.SysFont('Trebuchet MS', 20)
font3 = pygame.font.SysFont('Trebuchet MS', 90)
font4 = pygame.font.SysFont('Trebuchet MS', 40)
font_1 = pygame.font.SysFont('Trebuchet MS', 35)
font_2 = pygame.font.SysFont('Trebuchet MS', 35)
font_3 = pygame.font.SysFont('Trebuchet MS', 30)
font_4 = pygame.font.SysFont('Trebuchet MS', 35)

home_text = font1.render('Home', True, 'White')

red = [200, 0, 0]
bright_green = [0, 255, 0]
pink = [255, 120, 203]
blue = [0, 0, 180]
yellow = 'Yellow'
purple = 'Purple'
bright_red = [255, 0, 0]
bright_blue = [0, 0, 255]
orange = 'Orange'
white = [255, 255, 255]
black = [0, 0, 0]
grey = [128, 128, 128]
default_green = [0, 190, 0]

colour_list = [default_green]
designs_list = []
custom_skins_list = []

pcc = default_green
scc = black
ctcs = default_green
cstrs = black
dstrs = black
dcc = black
dsc = default_green

t2ext = font_1.render('Primary Colours', True, pcc)
t3ext = font_1.render('Secondary Colours', True, scc)

t2ext_rect = t2ext.get_rect(topleft=(200, 140))
t3ext_rect = t3ext.get_rect(topright=(800, 140))

colour = font4.render('Colours', True, ctcs)
cs = font4.render('Custom Skins', True, cstrs)
ds = font4.render('Designs', True, dstrs)

colourr = colour.get_rect(topleft=(210, 90))
csr = cs.get_rect(midtop=(500, 90))
dsr = ds.get_rect(topright=(790, 90))

red_colour = black
bright_green_colour = black
pink_colour = black
blue_colour = black
yellow_colour = black
purple_colour = black
bright_red_colour = black
bright_blue_colour = black
orange_colour = black
white_colour = black
black_colour = black
grey_colour = black
default_green_colour = default_green

stripes_colour = black
outline_colour = black
spotty_colour = black
diamond_colour = black
rainbow_colour = black
ic_colour = black

cn_colour = black
alien_colour = black
flower_colour = black
mars_colour = black
plane_colour = black
smurf_colour = black

NoneColour = black
ExtrasCol = black
ms_colour = black

red_text = font2.render('Red', True, red_colour)  # re render
bright_green_text = font2.render('Bright Green', True, bright_green_colour)  # re render
pink_text = font2.render('Pink', True, pink_colour)  # re render
blue_text = font2.render('Blue', True, blue_colour)  # re render
yellow_text = font2.render('Yellow', True, yellow_colour)  # re render
purple_text = font2.render('Purple', True, purple_colour)  # re render
bright_red_text = font2.render('Bright Red', True, bright_red_colour)  # re render
bright_blue_text = font2.render('Bright Blue', True, bright_blue_colour)  # re render
orange_text = font2.render('Orange', True, orange_colour)  # re render
white_text = font2.render('White', True, white_colour)  # re render
black_text = font2.render('Black', True, black_colour)  # re render
grey_text = font2.render('Grey', True, grey_colour)  # re render
default_green_text = font2.render('Green', True, default_green_colour)  # re render

stripes_text = font2.render('Stripes', True, stripes_colour)
outline_text = font2.render('Outline', True, outline_colour)
spotty_text = font2.render('Spotty', True, spotty_colour)
diamond_text = font2.render('Diamonds', true, diamond_colour)
rainbow_text = font2.render('Rainbow', True, rainbow_colour)
ic_text = font1.render('Inner Circle', True, ic_colour)

cn_text = font1.render('Chicken Nugget', True, cn_colour)
alien_text = font1.render('Alien', True, alien_colour)
flower_text = font1.render('Flower', true, flower_colour)
mars_text = font1.render('Mars', true, mars_colour)
plane_text = font1.render('Plane', true, plane_colour)
smurf_text = font1.render('Smurf Cat', true, smurf_colour)

NoneText = font1.render('None', True, NoneColour)
ExtrasTex = font4.render('Extras', True, ExtrasCol)
extrasTex = font1.render('Extras', True, black)
ms_text = font1.render('Main Shop', True, ms_colour)

laxa = 'On'

autosave_text = font1.render('Autosave: ' + laxa, true, black)
autosave_rect = autosave_text.get_rect(topright=(800, 130))

account1 = True
account2 = False
account3 = False
account4 = False

default_green_rect = default_green_text.get_rect(bottomleft=(180, 450))
red_rect = red_text.get_rect(bottomleft=(280, 450))
pink_rect = pink_text.get_rect(bottomleft=(345, 450))
blue_rect = blue_text.get_rect(bottomleft=(415, 450))
yellow_rect = yellow_text.get_rect(midbottom=(515, 450))
purple_rect = purple_text.get_rect(bottomright=(650, 450))
bright_red_rect = bright_red_text.get_rect(bottomright=(790, 450))
bright_green_rect = bright_green_text.get_rect(bottomleft=(180, 490))
bright_blue_rect = bright_blue_text.get_rect(bottomleft=(375, 490))
orange_rect = orange_text.get_rect(bottomleft=(550, 490))
white_rect = white_text.get_rect(bottomleft=(670, 490))
black_rect = black_text.get_rect(bottomleft=(180, 530))
grey_rect = grey_text.get_rect(bottomleft=(270, 530))

stripes_rect = stripes_text.get_rect(topleft=(180, 460))
outline_rect = outline_text.get_rect(topleft=(300, 460))
spotty_rect = spotty_text.get_rect(topleft=(420, 460))
ic_rect = ic_text.get_rect(topleft=(670, 460))
diamond_rect = diamond_text.get_rect(topleft=(530, 460))
rainbow_rect = rainbow_text.get_rect(topleft=(180, 500))

cn_rect = cn_text.get_rect(topleft=(180, 460))
alien_rect = alien_text.get_rect(topleft=(410, 460))
flower_rect = flower_text.get_rect(topleft=(500, 460))
mars_rect = mars_text.get_rect(topleft=(610, 460))
plane_rect = plane_text.get_rect(topleft=(700, 460))
smurf_rect = smurf_text.get_rect(topleft=(180, 500))

NoneRect = NoneText.get_rect(topleft=(750, 500))
ExtrasRec = ExtrasTex.get_rect(midright=(980, 570))
extrasRec = extrasTex.get_rect(center=(500, 20))
ms_rect = ms_text.get_rect(center=(500, 575))

playtime = 0
invalid_key = False
blit_text02 = False
lower_alpha = True
font_3.set_underline(True)
font_2.set_underline(True)
font_4.set_underline(True)
font3.set_bold(True)
t_text = font.render('Time:', True, 'Black')
s_text = 'Score: '
shoppingg_text = font1.render('Shop:', True, 'Black')
shoppingg_rect = shoppingg_text.get_rect(topleft=(120, 40))

home_screen = True
game_start = False
game_started = False
information = False
end_screen = False
clrs = False
cstm_skins = False
dsgns = False
game_settings = False
character_customisation = False
statistics = False
wheel_spinner = False
colours = True
customm_skins = False
desins = False
primary_colors = True
secondary_colors = False
play = False
levels = False
design_selection = True
design_customisation = False
game_stats = False
shop_stats = False
time_stats = False
tp_confirmation = False
switch_accounts = False
revival_screen = False
extras = False
misc = True
accessories = False

line1 = pygame.Surface((10, 600))
line2 = pygame.Surface((1000, 10))

line1.fill(black)
line2.fill(black)

line1_rect = line1.get_rect(center=(328.3, 300))
line2_rect = line2.get_rect(center=(500, 300))
line3_rect = line1.get_rect(center=(661.7, 300))

red_price = 13
pink_price = 12
blue_price = 12
yellow_price = 11
purple_price = 11
bright_red_price = 15
bright_green_price = 14
bright_blue_price = 19
orange_price = 11
white_price = 17
black_price = 18
grey_price = 17

stripes_price = 28
outline_price = 25
spotty_price = 32
diamonds_price = 36
rainbow_price = 47
ic_price = 30

alien_price = 41
nugget_price = 50
flower_price = 45
mars_price = 46
plane_price = 48
smurf_price = 49

tcks = 0
key_names = {
    pygame.K_SPACE: 'SPACE',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9',
    pygame.K_q: 'Q',
    pygame.K_w: 'W',
    pygame.K_e: 'E',
    pygame.K_r: 'R',
    pygame.K_t: 'T',
    pygame.K_y: 'Y',
    pygame.K_u: 'U',
    pygame.K_i: 'I',
    pygame.K_o: 'O',
    pygame.K_p: 'P',
    pygame.K_a: 'A',
    pygame.K_s: 'S',
    pygame.K_d: 'D',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_z: 'Z',
    pygame.K_x: 'X',
    pygame.K_c: 'C',
    pygame.K_v: 'V',
    pygame.K_b: 'B',
    pygame.K_n: 'N',
    pygame.K_m: 'M',
    pygame.K_RETURN: 'RETURN',
    pygame.K_UP: 'UP',
    pygame.K_KP_ENTER: 'ENTER'
}

tickk = 60.0
jump_default = pygame.K_SPACE
jump = jump_default
jump_string = key_names.get(jump)
text_colour = black
text0 = font_2.render('Controls', True, black)
text00 = font1.render('Jump Key:', True, black)
text01 = font_3.render(jump_string, True, text_colour)
text02 = font2.render('click to change', True, black)
text0_rect = text0.get_rect(midleft=(170, 300))
text00_rect = text00.get_rect(midleft=(170, 360))
text01_rect = text01.get_rect(midleft=(315, 360))
text02_rect = text02.get_rect(midleft=(290, 395))

rrrct = pygame.Rect(0, 0, 495, 600)
rrct = pygame.Rect(505, 0, 495, 600)

balance = 0
currency_spent = 0
primary_colour = default_green
secondary_colour = None
design = None
custom_skin = None
x = 50
y = 513
player = pygame.Surface((40, 40))
player_rect = player.get_rect(bottomleft=(x, y))
player.fill(primary_colour)
pygame.display.set_icon(cn1)
player_rect1 = player.get_rect(topleft=(480, 450))

ticks = 0
pass_key = True
ticks_pk = True
stage1 = False
stage2 = False
stage3 = False
stage4 = False
change_jump_key = False
velocity_y = 0
gravity = 0.5
jump_strength = -6.2
a_m = 0
can_jump = True
spawn_pos_y = list(range(0, 900))
SpawnPosY = list(range(87, 500))
enemies_t = []
enemies_c = []  # List for circles
enemies_s = []
shields_l = []
shields_sl = []
clouds_l = []
clouds_sl = []
ig_l = []
exc_sl = []
enemy_wave_l = []
scores = []  # List to store scores
game_durations = [x / 4.42857142 for x in scores]
enemy_spawn_delay = 1100
esd_key = True
esd_key1 = True
esd_key2 = True
enemy_allow_spawn = True
wave_spawn = 0
wave_spawn_s = 0
wave_spawn_k = True
wave = False
last_enemy_spawn_time = 0
crt = 0
last_wave_time = 0
key = True
wave_active = False
blit_stage4 = True
txtt = 'Press ' + jump_string + ' to start.'
balance_text = font4.render(str(balance), True, black)
text = font.render(txtt, True, (0, 0, 0))
ctc = default_green
cstr = black
dstr = black
gsc = default_green
ccc = black
mtc = default_green
atc = black
colour = font4.render('Colours', True, ctc)
colour_r = colour.get_rect(topleft=(180, 40))
cs = font4.render('Custom Skins', True, cstr)
cs_r = cs.get_rect(midtop=(500, 40))
ds = font4.render('Designs', True, dstr)
ds_r = ds.get_rect(topright=(820, 40))
misc_text = font4.render('Miscellaneous', True, mtc)
acc_text = font4.render('Accessories', True, atc)
game_settings_text = font_1.render('Game Settings', True, gsc)
character_customisation_text = font_1.render('Character Customisation', True, ccc)
game_settings_rect = game_settings_text.get_rect(topleft=(130, 42.5))
character_customisation_rect = character_customisation_text.get_rect(topright=(870, 42.5))
box_width = 800
box_height = 50
box_x = 100
box_y = 40
box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
box1_width = 700
box1_height = 470
box1_x = 150
box1_y = 87
box1_rect = pygame.Rect(box1_x, box1_y, box1_width, box1_height)
line3 = pygame.Surface((6, 470))
line4 = pygame.Surface((700, 6))
line3.fill(black)
line4.fill(black)
pk = False
pk1 = False

gameplay_rect = pygame.Rect(0, 0, 497, 297)
time_rect1 = pygame.Rect(0, 303, 497, 297)
shop_rect11 = pygame.Rect(503, 0, 497, 297)
rect23 = pygame.Rect(503, 303, 497, 297)

tax = font1.render('Design Selection', true, dsc)
tax1 = font1.render('Design Customisation', True, dcc)
tax_r = tax.get_rect(topleft=(200, 150))
tax1_r = tax1.get_rect(topleft=(520, 150))

item_rect = pygame.Rect(160, 97, 105, 105)
item_rect1 = pygame.Rect(275, 97, 105, 105)
item_rect2 = pygame.Rect(390, 97, 105, 105)
item_rect3 = pygame.Rect(505, 97, 105, 105)
item_rect4 = pygame.Rect(620, 97, 105, 105)
item_rect5 = pygame.Rect(735, 97, 105, 105)
item_rect6 = pygame.Rect(160, 262, 105, 105)
item_rect7 = pygame.Rect(275, 262, 105, 105)
item_rect8 = pygame.Rect(390, 262, 105, 105)
item_rect9 = pygame.Rect(505, 262, 105, 105)
item_rect10 = pygame.Rect(620, 262, 105, 105)
item_rect11 = pygame.Rect(735, 262, 105, 105)
item_rect12 = pygame.Rect(160, 427, 105, 105)
shop_text = font1.render('Shop', True, 'Black')
shop_trect = shop_text.get_rect(midtop=(500, 0))
settings_text = font1.render('Settings', True, black)
settings_rect = settings_text.get_rect(midtop=(500, 0))

game_counter = 0
total_balance_collected = balance

enact_ig = False

cet = 0
cet1 = 0
cet2 = 0
cet3 = 0
cet4 = 0
cet5 = 0
cet6 = 0
cet7 = 0

t1cks = 0

slider_x, slider_y = 200, 310
slider_width, slider_height = 250, 10
handle_size = 20
slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)

slider_x1, slider_y1 = 200, 470
slider_width1, slider_height1 = 250, 10
handle_size1 = 20
slider_rect1 = pygame.Rect(slider_x1, slider_y1, slider_width1, slider_height1)

slider_x5, slider_y5 = 550, 320
slider_width5, slider_height5 = 250, 10
handle_size5 = 20
slider_rect5 = pygame.Rect(slider_x5, slider_y5, slider_width5, slider_height5)

slider_x2, slider_y2 = 170, 150
slider_width2, slider_height2 = 300, 10
handle_size2 = 20
slider_rect2 = pygame.Rect(slider_x2, slider_y2, slider_width2, slider_height2)

slider_x3, slider_y3 = 550, 450
slider_width3, slider_height3 = 250, 10
handle_size3 = 20
slider_rect3 = pygame.Rect(slider_x3, slider_y3, slider_width3, slider_height3)

# Slider range
min_value = 1
max_value = 14
stripe_width = 4

min_value1 = 1
max_value1 = 10
outline_size = 4

min_value5 = 1
max_value5 = 20
radius_length = 10

min_value2 = 0.5
max_value2 = 3
step2 = 0.1
game_speed_multiplier = 1
last_game_speed_multiplier = game_speed_multiplier

min_value3 = 1
max_value3 = 10
colour_change_interval = 3.0
step_size = 0.01

dragging = False
dragging1 = False
dragging2 = False
dragging5 = False
dragging3 = False

sa_text1 = font2.render('Switch Accounts', True, black)
exit_rect = exit_icon.get_rect(topleft=(160, 8))
sa_rect = sa_text1.get_rect(topleft=(10, 10))

spawn_shields = False
spawn_powerup = False
spawn_coin = False


def draw_stripes(surface, colour1):
    global stripe_width
    if colour1 is not None:  # Only draw stripes if color is not None
        for t in range(0, surface.get_width(), stripe_width * 2):  # Adjust width based on surface
            pygame.draw.rect(surface, colour1, (t, 0, stripe_width, surface.get_height()))


spot_radius = 7  # Larger radius for smoother circles
spot_spacing = 20  # Increase spacing to make the spots more distinct


# Create a grid of spots
def draw_spots(surface, num=40):
    if secondary_colour is not None:
        for f in range(spot_spacing // 2, num, spot_spacing):
            for g in range(spot_spacing // 2, num, spot_spacing):
                pygame.draw.circle(surface, secondary_colour, (g, f), spot_radius)


def draw_circle(radius, center):
    if secondary_colour is not None:
        pygame.draw.circle(screen, secondary_colour, center, radius)


spot_radius1 = 5
spot_spacing1 = 10


# Create a grid of spots
def draw_diamonds(surface):
    for c in range(spot_spacing1 // 2, 40, spot_spacing1):
        for d in range(spot_spacing1 // 2, 40, spot_spacing1):
            pygame.draw.circle(surface, secondary_colour, (d, c), spot_radius1)


rect1 = pygame.Rect(197.5, 107, 30, 30)
rect2 = pygame.Rect(312.5, 107, 30, 30)
rect3 = pygame.Rect(427.5, 107, 30, 30)
rect4 = pygame.Rect(542.5, 107, 30, 30)
rect5 = pygame.Rect(657.5, 107, 30, 30)
rect6 = pygame.Rect(772.5, 107, 30, 30)
rect7 = pygame.Rect(197.5, 272, 30, 30)
rect8 = pygame.Rect(312.5, 272, 30, 30)
rect9 = pygame.Rect(427.5, 272, 30, 30)
rect10 = pygame.Rect(542.5, 272, 30, 30)
rect11 = pygame.Rect(657.5, 272, 32, 32)
rect12 = pygame.Rect(772.5, 272, 30, 30)
rect13 = pygame.Rect(197.5, 437, 30, 30)
color = 180, 180, 180, 255
txxt = font4.render('Insufficient balance!', True, black)
txxxt = font4.render('Invalid Key!', True, black)
rrect = txxt.get_rect(midtop=(500, 450))
reect = txxxt.get_rect(midtop=(500, 450))
rrrect = pygame.Rect(300, 445, 400, 60)
reeect = pygame.Rect(350, 445, 300, 60)
lticks = 0
rect14 = pygame.Rect(150, 90, 230.333, 232)
rect15 = pygame.Rect(386.333, 90, 230.333, 232)
rect16 = pygame.Rect(619.667, 90, 230.333, 232)
rect17 = pygame.Rect(150, 328, 230.333, 227)
rect18 = pygame.Rect(386.333, 328, 230.333, 227)
rect19 = pygame.Rect(619.667, 328, 230.333, 227)

inverted_gravity = False

ttx = font1.render('Account 1', True, white)
ttx1 = font1.render('Account 2', true, white)
ttx2 = font1.render('Account 3', True, white)
ttx3 = font1.render('Account 4', true, white)
rect24 = pygame.Rect(150, 200, 250, 50)
rect25 = pygame.Rect(600, 200, 250, 50)
rect26 = pygame.Rect(150, 350, 250, 50)
rect27 = pygame.Rect(600, 350, 250, 50)
ttx_rect = ttx.get_rect(center=(275, 225))
ttx1_rect = ttx1.get_rect(center=(725, 225))
ttx2_rect = ttx2.get_rect(center=(275, 375))
ttx3_rect = ttx3.get_rect(center=(725, 375))

jump_key_pressed = 0

Y_Rect = pygame.Rect(240, 475, 120, 50)
N_Rect = pygame.Rect(640, 475, 120, 50)

angle = 0


def restore_defaults_design():
    global primary_colour, secondary_colour, default_green, custom_skin, design
    primary_colour = default_green
    secondary_colour = None
    custom_skin = None
    design = None


def restart_game():
    global game_start, game_started, information, end_screen, ticks, pass_key, ticks_pk, velocity_y, enemies_t, \
        enemies_c, enemies_s, esd_key1, esd_key2, stage1, stage2, stage3, stage4, enemy_spawn_delay, \
        last_enemy_spawn_time, esd_key, enemy_allow_spawn, wave_spawn, wave_spawn_s, wave_spawn_k, wave, enemy_wave_l, crt, \
        last_wave_time, key, wave_active, blit_stage4, x, y, game_counter, shields_l, spawn_shields, shields_sl, clouds_l, \
        clouds_sl, lower_alpha, alpha_value, ig_l, inverted_gravity, enact_ig, cet5, rand_c, CTime, cet4, cet3, \
        cet2, cet1, cet, processed_obj, processed_objects, processed_obj1, processed_objects1, pro_obj, pro_obj1, randomise_c, \
        randomise_chosen_time, ChosenTime, ChooseTime, revival_screen, angle
    angle = 0
    cet5 = 0
    rand_c = True
    randomise_c = True
    randomise_chosen_time = True
    CTime = 0
    ChosenTime = 0
    ChooseTime = 0
    cet4 = 0
    cet3 = 0
    cet2 = 0
    cet1 = 0
    cet = 0
    processed_obj = set()
    pro_obj1 = set()
    processed_obj1 = set()
    processed_objects1 = set()
    processed_objects = set()
    pro_obj = set()
    enact_ig = False
    ig_l = []
    inverted_gravity = False
    game_start = True
    game_started = False
    information = False
    end_screen = False
    ticks = 0
    key = True
    pass_key = True
    ticks_pk = True
    esd_key = True
    esd_key1 = True
    esd_key2 = True
    enemy_allow_spawn = True
    wave_spawn = 0
    wave_spawn_s = 0  # Reset wave_spawn_s
    wave_spawn_k = True
    wave = False
    enemy_wave_l = []
    stage1 = False
    stage2 = False
    stage3 = False
    stage4 = False
    revival_screen = False
    enemy_spawn_delay = 1100
    last_enemy_spawn_time = 0
    velocity_y = 0
    crt = 0
    last_wave_time = 0
    blit_stage4 = True
    x = 50
    y = 513
    enemies_t = []  # Reset triangle enemies list
    enemies_c = []  # Reset circle enemies list
    enemies_s = []  # Reset square enemies list
    shields_l = []
    shields_sl = []
    clouds_l = []
    clouds_sl = []
    spawn_shields = False
    wave_active = False
    game_counter += 1
    alpha_value = 255
    lower_alpha = False


def restart_game1():
    global game_start, game_started, information, end_screen, ticks, pass_key, ticks_pk, velocity_y, enemies_t, \
        enemies_c, enemies_s, esd_key1, esd_key2, stage1, stage2, stage3, stage4, enemy_spawn_delay, \
        last_enemy_spawn_time, esd_key, enemy_allow_spawn, wave_spawn, wave_spawn_s, wave_spawn_k, wave, enemy_wave_l, crt, \
        last_wave_time, key, wave_active, blit_stage4, home_screen, x, y, game_counter, shields_l, spawn_shields, shields_sl, \
        clouds_sl, clouds_l, lower_alpha, alpha_value, inverted_gravity, ig_l, enact_ig, cet5, rand_c, CTime, cet4, cet3, \
        cet2, cet1, cet, processed_obj, processed_objects, processed_obj1, processed_objects1, pro_obj, pro_obj1, randomise_c, \
        randomise_chosen_time, ChosenTime, ChooseTime, revival_screen, angle
    angle = 0
    revival_screen = False
    cet5 = 0
    rand_c = True
    randomise_c = True
    randomise_chosen_time = True
    CTime = 0
    ChosenTime = 0
    ChooseTime = 0
    cet4 = 0
    cet3 = 0
    cet2 = 0
    cet1 = 0
    cet = 0
    processed_obj = set()
    pro_obj1 = set()
    processed_obj1 = set()
    processed_objects1 = set()
    processed_objects = set()
    pro_obj = set()
    enact_ig = False
    ig_l = []
    inverted_gravity = False
    game_start = False
    game_started = False
    information = False
    end_screen = False
    home_screen = True
    ticks = 0
    key = True
    pass_key = True
    ticks_pk = True
    esd_key = True
    esd_key1 = True
    esd_key2 = True
    enemy_allow_spawn = True
    wave_spawn = 0
    wave_spawn_s = 0  # Reset wave_spawn_s
    wave_spawn_k = True
    wave = False
    enemy_wave_l = []
    stage1 = False
    stage2 = False
    stage3 = False
    stage4 = False
    enemy_spawn_delay = 1100
    last_enemy_spawn_time = 0
    velocity_y = 0
    crt = 0
    last_wave_time = 0
    blit_stage4 = True
    x = 50
    y = 513
    enemies_t = []  # Reset triangle enemies list
    enemies_c = []  # Reset circle enemies list
    enemies_s = []  # Reset square enemies list
    shields_l = []
    shields_sl = []
    clouds_sl = []
    clouds_l = []
    spawn_shields = False
    wave_active = False
    game_counter += 1
    lower_alpha = False
    alpha_value = 255


tp_rect = pygame.Rect(350, 500, 300, 45)


class Enemy_triangle:
    def __init__(self):
        self.x = 1100
        self.y = random.choice(spawn_pos_y)
        self.size = 60
        self.color = 'Yellow'
        self.speed = 5
        self.points = self.calculate_points()

    def reset(self):
        self.x = 1100

    def calculate_points(self):
        half_size = self.size / 2
        return [
            (self.x - 100, self.y),  # Right vertex
            (self.x - self.size, self.y - half_size),  # Top left vertex
            (self.x - self.size, self.y + half_size)  # Bottom left vertex [mirrored]
        ]

    def move(self):
        self.x -= self.speed
        self.points = self.calculate_points()

    def draw(self):
        pygame.draw.polygon(screen, pygame.Color(self.color), self.points)

    def get_rect(self):
        min_x = min(point[0] for point in self.points)
        max_x = max(point[0] for point in self.points)
        min_y = min(point[1] for point in self.points)
        max_y = max(point[1] for point in self.points)
        return pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)


class Enemy_circle:
    def __init__(self):
        self.x = 1100
        self.y = random.choice(spawn_pos_y)
        self.radius = 25
        self.colour = 'Red'
        self.speed = 6.4

    def reset(self):
        self.x = 1100

    def draw(self):
        pygame.draw.circle(screen, pygame.Color(self.colour), (self.x, self.y), self.radius)

    def move(self):
        self.x -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x - 30, self.y - 30, 50, 50)


class Enemy_square:
    def __init__(self):
        self.x = 1100
        self.y = random.choice(spawn_pos_y)
        self.length = 50
        self.width = 50
        self.colour = 'Blue'
        self.speed = 7.3

    def reset(self):
        self.x = 1100

    def move(self):
        self.x -= self.speed

    def draw(self):
        enemy_sq = pygame.Surface((self.length, self.width))
        enemy_sq.fill(self.colour)
        screen.blit(enemy_sq, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.length, self.width)


class enemy_wave_1:
    def __init__(self):
        y_list = [50, 300]
        enmy1 = random.choice(y_list)
        self.ac_enmy1 = int(enmy1)
        y_list.remove(enmy1)
        enmy2 = int(' '.join(map(str, y_list)))
        self.enmy2 = enmy2
        self.enemy1 = self.Enemy1(self.ac_enmy1)
        self.enemy2 = self.Enemy2(self.enmy2)

    class Enemy1:
        def __init__(self, p):
            self.x = 1100
            self.y = p
            self.length = 50
            self.width = 250
            self.colour = 'Black'
            self.speed = 4.8

        def move(self):
            self.x -= self.speed

        def draw(self):
            enemy_sq = pygame.Surface((self.length, self.width))
            enemy_sq.fill(self.colour)
            screen.blit(enemy_sq, (self.x, self.y))

        def get_rect(self):
            return pygame.Rect(self.x, self.y, self.length, self.width)

    class Enemy2:
        def __init__(self, o):
            self.x = 1100
            self.y = o
            self.length = 50
            self.width = 250
            self.colour = 'Black'
            self.speed = 4.8

        def move(self):
            self.x -= self.speed
            if self.x <= 420:
                self.colour = 'Green'

        def draw(self):
            enemy_sq = pygame.Surface((self.length, self.width))
            enemy_sq.fill(self.colour)
            screen.blit(enemy_sq, (self.x, self.y))


class SpawnShield:
    def __init__(self):
        self.x = 1100
        self.y = random.choice(SpawnPosY)
        self.speed = 5

    def move(self):
        self.x -= self.speed

    def draw(self):
        screen.blit(shield, (self.x, self.y))

    def get_rect(self):
        return shield.get_rect(topleft=(self.x, self.y))


class SpawnCloud:
    def __init__(self):
        self.x = 1100
        self.y = random.choice(SpawnPosY)
        self.speed = 5

    def move(self):
        self.x -= self.speed

    def draw(self):
        screen.blit(image, (self.x, self.y))

    def get_rect(self):
        return image.get_rect(topleft=(self.x, self.y))


class ExtraCoin:
    def __init__(self):
        self.speed = 6
        self.lst = (2, 2, 2, 2, 2, 3, 3, 5)
        self.coin_amount = random.choice(self.lst)
        self.text = font1.render(f'+{self.coin_amount}', True, bright_green)
        self.x = 1100
        self.y = random.choice(SpawnPosY)

    def move(self):
        self.x -= self.speed

    def draw(self):
        screen.blit(coin, (self.x, self.y))
        screen.blit(self.text, (self.x + 15, self.y + 30))

    def get_rect(self):
        return coin.get_rect(topleft=(self.x, self.y))


class HasCloud:
    def __init__(self):
        self.time_limit = 15


class HasShield:
    def __init__(self):
        self.pass_key = False
        self.colour = black
        self.lives = 5
        self.length = 10
        self.width = 60
        self.x = player_rect.x + 50
        self.y = (player_rect.y - 10) + (-.5 * self.width + 30)
        self.time_limit = 14

    def draw(self):
        if self.lives != 0:
            pygame.draw.rect(screen, self.colour, HasShield().get_rect())

    def update(self):
        shield_rect = HasShield().get_rect()
        triangle_rect = Enemy_triangle().get_rect()
        circle_rect = Enemy_circle().get_rect()
        square_rect = Enemy_square().get_rect()
        if self.pass_key:
            if (shield_rect.colliderect(triangle_rect) or shield_rect.colliderect(circle_rect) or
                    shield_rect.colliderect(square_rect)):
                self.lives -= 1
                self.pass_key = False
        self.width = self.lives * 10
        self.y = (player_rect.y - 10) + (-.5 * self.width + 30)

        if not (shield_rect.colliderect(triangle_rect) or shield_rect.colliderect(circle_rect) or
                shield_rect.colliderect(square_rect)):
            self.pass_key = True

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.length, self.width)


def revive():
    global a_score
    if a_score >= 50:
        return True
    return False


def truncate(number, decimals=0):
    multiplier = 10 ** decimals
    return int(number * multiplier) / multiplier


def save_score(score1):
    scores.append(score1)


def get_highest_score():
    if scores:
        return max(scores)
    return 0


def get_lowest_score():
    if scores:
        return min(scores)
    return 0


def get_highest_game_duration():
    if game_durations:
        return max(game_durations)
    return 0


def get_lowest_game_duration():
    if game_durations:
        return min(game_durations)
    return 0


enemy_triangle = Enemy_triangle()
enemy_circle = Enemy_circle()
enemy_square = Enemy_square()

pkk = False
purchases = 0

average_score = 0
average_game_duration = 0

gs_text = font4.render('Game Stats', True, black)
tgp_text = font1.render(f'Total Games Played: {game_counter}', True, black)
tj_text = font1.render(f'Total Jumps: {jump_key_pressed}', true, black)
try:
    avj_text = font1.render(f'Average Jumps Per Game: {round(jump_key_pressed / game_counter), 1}', true, black)
except ZeroDivisionError:
    avj_text = font1.render(f'Average Jumps Per Game: 0', true, black)
bgd_text = font1.render(f'Highest Game Duration: {round(get_highest_game_duration(), 1)} seconds', True, black)
avgd_text = font1.render(f'Average Game Duration: {round(average_game_duration, 1)} seconds', true, black)
lgd_text = font1.render(f'Lowest Game Duration: {get_lowest_game_duration()} seconds', true, black)
bs_text = font1.render(f'Highest Score: {get_highest_score()}', True, black)
as_text = font1.render(f'Average Score: {round(average_score, 1)}', true, black)
ls_text = font1.render(f'Lowest Score: {get_lowest_score()}', true, black)
gp_text = font_4.render('Gameplay:', true, black)
gd_text = font_4.render('Game Durations:', true, black)
s_text1 = font_4.render('Scores:', true, black)
gs_rect = gs_text.get_rect(midtop=(500, 40))
tgp_rect = tgp_text.get_rect(topleft=(180, 135))
tj_rect = tj_text.get_rect(topleft=(180, 170))
avj_rect = avj_text.get_rect(topleft=(180, 205))
bgd_rect = bgd_text.get_rect(topleft=(180, 290))
avgd_rect = avgd_text.get_rect(topleft=(180, 325))
lgd_rect = lgd_text.get_rect(topleft=(180, 360))
bs_rect = bs_text.get_rect(topleft=(180, 445))
as_rect = as_text.get_rect(topleft=(180, 480))
ls_rect = ls_text.get_rect(topleft=(180, 515))
gp_rect = gp_text.get_rect(topleft=(180, 85))
gd_rect = gd_text.get_rect(topleft=(180, 245))
s_rect5 = s_text1.get_rect(topleft=(180, 400))

randomise_chosen_time = True
randomise_c = True
rand_c = True
random_c = True
times_iterated = 0
times_i = 0
timing_list1 = list(range(15, 40))
timing_list2 = [round(x, 1) for x in [i * 0.1 for i in range(150, 601)]]

pk00 = True

# Initialize real-life accumulated playtime variables
rla_playtime = 0
rla_playtime_h = 0
rla_playtime_m = 0
rla_playtime_s = 0

# Calculate initial playtime based on current ticks
playtime = round(pygame.time.get_ticks() / 1000)
playtime_h = round(playtime // 3600)
playtime_m = round((playtime % 3600) // 60)
playtime_s = round(playtime % 60)
autosave = True
avjpg = 0

lster = [26, 27, 28, 30, 32, 34]
lester = random.choice(lster)

try:
    with open("account_data.json") as AccountDataFile:
        AccountData = json.load(AccountDataFile)
        account1 = AccountData.get("Account1", True)
        account2 = AccountData.get("Account2", False)
        account3 = AccountData.get("Account3", False)
        account4 = AccountData.get("Account4", False)
except FileNotFoundError:
    pass

if account1:
    try:
        with open("player_data.json") as PlayerData:
            data = json.load(PlayerData)
            rla_playtime = data.get("TPlaytime", 0)
            rla_playtime_h = data.get("PlaytimeHours", 0)
            rla_playtime_m = data.get("PlaytimeMinutes", 0)
            rla_playtime_s = data.get("PlaytimeSeconds", 0)
            total_balance_collected = data.get("TotalBalanceCollected", 0)
            currency_spent = data.get("CurrencySpent", 0)
            purchases = data.get("Purchases", 0)
            balance = data.get("Balance", 0)
            game_counter = data.get("GameCounter", 0)
            jump_key_pressed = data.get("JumpCounter", 0)
            avjpg = data.get("AverageJumps/Game", 0)
            scores = data.get("Scores", [])
            colour_list = data.get("ColoursOwned", [default_green])
            designs_list = data.get("DesignsOwned", [])
            custom_skins_list = data.get("CustomSkinsOwned", [])
            primary_colour = data.get("PrimaryColour", default_green)
            secondary_colour = data.get("SecondaryColour", None)
            design = data.get("EquippedDesign", None)
            custom_skin = data.get("EquippedCustomSkin", None)
            jump = data.get("Jump", pygame.K_SPACE)
            jump_string = data.get("JumpKey", "SPACE")
            game_speed_multiplier = data.get("GameSpeedMultiplier", 1.0)
            stripe_width = data.get("StripeWidth", 4)
            outline_size = data.get("OutlineSize", 4)
            radius_length = data.get("RadiusLength", 10)
            colour_change_interval = data.get("ColourChangeInterval", 3.0)
    except FileNotFoundError:
        pass

    try:
        with open("autosavestate.json") as AutoState:
            data1 = json.load(AutoState)
            autosave = data1.get("AutoSaveState", True)
    except FileNotFoundError:
        pass

if account2:
    try:
        with open("player_data1.json") as PlayerData:
            data = json.load(PlayerData)
            rla_playtime = data.get("TPlaytime", 0)
            rla_playtime_h = data.get("PlaytimeHours", 0)
            rla_playtime_m = data.get("PlaytimeMinutes", 0)
            rla_playtime_s = data.get("PlaytimeSeconds", 0)
            total_balance_collected = data.get("TotalBalanceCollected", 0)
            currency_spent = data.get("CurrencySpent", 0)
            purchases = data.get("Purchases", 0)
            balance = data.get("Balance", 0)
            game_counter = data.get("GameCounter", 0)
            jump_key_pressed = data.get("JumpCounter", 0)
            avjpg = data.get("AverageJumps/Game", 0)
            scores = data.get("Scores", [])
            colour_list = data.get("ColoursOwned", [default_green])
            designs_list = data.get("DesignsOwned", [])
            custom_skins_list = data.get("CustomSkinsOwned", [])
            primary_colour = data.get("PrimaryColour", default_green)
            secondary_colour = data.get("SecondaryColour", None)
            design = data.get("EquippedDesign", None)
            custom_skin = data.get("EquippedCustomSkin", None)
            jump = data.get("Jump", pygame.K_SPACE)
            jump_string = data.get("JumpKey", "SPACE")
            game_speed_multiplier = data.get("GameSpeedMultiplier", 1.0)
            stripe_width = data.get("StripeWidth", 4)
            outline_size = data.get("OutlineSize", 4)
            radius_length = data.get("RadiusLength", 10)
            colour_change_interval = data.get("ColourChangeInterval", 3.0)
    except FileNotFoundError:
        pass

    try:
        with open("autosavestate1.json") as AutoState:
            data1 = json.load(AutoState)
            autosave = data1.get("AutoSaveState", True)
    except FileNotFoundError:
        pass

if account3:
    try:
        with open("player_data2.json") as PlayerData:
            data = json.load(PlayerData)
            rla_playtime = data.get("TPlaytime", 0)
            rla_playtime_h = data.get("PlaytimeHours", 0)
            rla_playtime_m = data.get("PlaytimeMinutes", 0)
            rla_playtime_s = data.get("PlaytimeSeconds", 0)
            total_balance_collected = data.get("TotalBalanceCollected", 0)
            currency_spent = data.get("CurrencySpent", 0)
            purchases = data.get("Purchases", 0)
            balance = data.get("Balance", 0)
            game_counter = data.get("GameCounter", 0)
            jump_key_pressed = data.get("JumpCounter", 0)
            avjpg = data.get("AverageJumps/Game", 0)
            scores = data.get("Scores", [])
            colour_list = data.get("ColoursOwned", [default_green])
            designs_list = data.get("DesignsOwned", [])
            custom_skins_list = data.get("CustomSkinsOwned", [])
            primary_colour = data.get("PrimaryColour", default_green)
            secondary_colour = data.get("SecondaryColour", None)
            design = data.get("EquippedDesign", None)
            custom_skin = data.get("EquippedCustomSkin", None)
            jump = data.get("Jump", pygame.K_SPACE)
            jump_string = data.get("JumpKey", "SPACE")
            game_speed_multiplier = data.get("GameSpeedMultiplier", 1.0)
            stripe_width = data.get("StripeWidth", 4)
            outline_size = data.get("OutlineSize", 4)
            radius_length = data.get("RadiusLength", 10)
            colour_change_interval = data.get("ColourChangeInterval", 3.0)
    except FileNotFoundError:
        pass

    try:
        with open("autosavestate2.json") as AutoState:
            data1 = json.load(AutoState)
            autosave = data1.get("AutoSaveState", True)
    except FileNotFoundError:
        pass

if account4:
    try:
        with open("player_data3.json") as PlayerData:
            data = json.load(PlayerData)
            rla_playtime = data.get("TPlaytime", 0)
            rla_playtime_h = data.get("PlaytimeHours", 0)
            rla_playtime_m = data.get("PlaytimeMinutes", 0)
            rla_playtime_s = data.get("PlaytimeSeconds", 0)
            total_balance_collected = data.get("TotalBalanceCollected", 0)
            currency_spent = data.get("CurrencySpent", 0)
            purchases = data.get("Purchases", 0)
            balance = data.get("Balance", 0)
            game_counter = data.get("GameCounter", 0)
            jump_key_pressed = data.get("JumpCounter", 0)
            avjpg = data.get("AverageJumps/Game", 0)
            scores = data.get("Scores", [])
            colour_list = data.get("ColoursOwned", [default_green])
            designs_list = data.get("DesignsOwned", [])
            custom_skins_list = data.get("CustomSkinsOwned", [])
            primary_colour = data.get("PrimaryColour", default_green)
            secondary_colour = data.get("SecondaryColour", None)
            design = data.get("EquippedDesign", None)
            custom_skin = data.get("EquippedCustomSkin", None)
            jump = data.get("Jump", pygame.K_SPACE)
            jump_string = data.get("JumpKey", "SPACE")
            game_speed_multiplier = data.get("GameSpeedMultiplier", 1.0)
            stripe_width = data.get("StripeWidth", 4)
            outline_size = data.get("OutlineSize", 4)
            radius_length = data.get("RadiusLength", 10)
            colour_change_interval = data.get("ColourChangeInterval", 3.0)
    except FileNotFoundError:
        pass

    try:
        with open("autosavestate3.json") as AutoState:
            data1 = json.load(AutoState)
            autosave = data1.get("AutoSaveState", True)
    except FileNotFoundError:
        pass


class MouseHover:
    mp = pygame.mouse.get_pos()

    def __init__(self):
        self.radius = 6
        self.interior = white
        self.exterior = red
        self.outline = 3

    def draw(self):
        pygame.draw.circle(screen, self.interior, mp, self.radius)
        pygame.draw.circle(screen, self.exterior, mp, self.radius, self.outline)


my_instance = MouseHover()

# Calculate the initial handle position based on the starting value
slider_range = slider_width - handle_size
handle_x = (stripe_width - min_value) / (max_value - min_value) * slider_range + slider_x
handle_rect = pygame.Rect(handle_x - handle_size // 2, slider_y - handle_size // 2, handle_size, 30)

slider_range1 = slider_width1 - handle_size1
handle_x1 = (outline_size - min_value1) / (max_value1 - min_value1) * slider_range1 + slider_x1
handle_rect1 = pygame.Rect(handle_x1 - handle_size1 // 2, slider_y1 - handle_size1 // 2, handle_size1, 30)

slider_range5 = slider_width5 - handle_size5
handle_x5 = (radius_length - min_value5) / (max_value5 - min_value5) * slider_range5 + slider_x5
handle_rect5 = pygame.Rect(handle_x5 - handle_size5 // 2, slider_y5 - handle_size5 // 2, handle_size5, 30)

slider_range2 = slider_width2 - handle_size2
handle_x2 = (game_speed_multiplier - min_value2) / (max_value2 - min_value2) * slider_range2 + slider_x2
handle_rect2 = pygame.Rect(handle_x2 - handle_size2 // 2, slider_y2 - handle_size2 // 2, handle_size2, 30)

slider_range3 = slider_width3 - handle_size3
handle_x3 = (colour_change_interval - min_value3) / (max_value3 - min_value3) * slider_range3 + slider_x3
handle_rect3 = pygame.Rect(handle_x3 - handle_size3 // 2, slider_y3 - handle_size3 // 2, handle_size3, 30)

running = True
quit2 = False
quit3 = False

# Initialize a variable to store the accumulated playtime
accumulated_playtime = rla_playtime

# Variable to store the previous tick value
previous_ticks = pygame.time.get_ticks()

while running:
    alien = pygame.transform.rotate(alien1, angle)
    cn = pygame.transform.rotate(cn1, angle)
    flower = pygame.transform.rotate(flower1, angle)
    mars = pygame.transform.rotate(mars1, angle)
    plane = pygame.transform.rotate(plane1, angle)
    smurf = pygame.transform.rotate(smurf1, angle)
    cloud.set_alpha(alpha_value)
    cloud1.set_alpha(alpha_value)
    if inverted_gravity:
        angle = 180
    if not inverted_gravity:
        angle = 0
    if jump is None:
        jump = pygame.K_SPACE
    if jump_string is None:
        jump_string = "SPACE"
    text01 = font1.render(jump_string, True, text_colour)
    game_durations = [x / 4.42857142 for x in scores]

    # Get the current tick count
    current_ticks = pygame.time.get_ticks()

    # Calculate the elapsed time in seconds since the last update
    elapsed_time = (current_ticks - previous_ticks) / 1000  # Convert to seconds

    # Update accumulated playtime
    accumulated_playtime += elapsed_time

    # Save the current tick value for the next iteration
    previous_ticks = current_ticks

    # Calculate the total playtime in hours, minutes, and seconds
    playtime_h = int(accumulated_playtime // 3600)
    playtime_m = int((accumulated_playtime % 3600) // 60)
    playtime_s = int(accumulated_playtime % 60)

    # Handle overflow (when seconds or minutes go over 60)
    if playtime_s >= 60:
        playtime_m += playtime_s // 60
        playtime_s %= 60

    if playtime_m >= 60:
        playtime_h += playtime_m // 60
        playtime_m %= 60

    try:
        average_score = sum(scores) / len(scores)
    except ZeroDivisionError:
        average_score = 0
    try:
        average_game_duration = sum(game_durations) / len(game_durations)
    except ZeroDivisionError:
        average_game_duration = 0
    gs_text = font4.render('Game Stats', True, black)
    tgp_text = font1.render(f'Total Games Played: {game_counter}', True, black)
    tj_text = font1.render(f'Total Jumps: {jump_key_pressed}', true, black)
    try:
        avjpg = round(jump_key_pressed / game_counter, 1)
    except ZeroDivisionError:
        avjpg = 0
    avj_text = font1.render(f'Average Jumps Per Game: {avjpg}', true, black)
    bgd_text = font1.render(f'Highest Game Duration: {round(get_highest_game_duration(), 1)} seconds', True, black)
    avgd_text = font1.render(f'Average Game Duration: {round(average_game_duration, 1)} seconds', true, black)
    lgd_text = font1.render(f'Lowest Game Duration: {round(get_lowest_game_duration(), 1)} seconds', true, black)
    bs_text = font1.render(f'Highest Score: {get_highest_score()}', True, black)
    as_text = font1.render(f'Average Score: {round(average_score, 1)}', true, black)
    ls_text = font1.render(f'Lowest Score: {get_lowest_score()}', true, black)
    gp_text = font_4.render('Gameplay:', true, black)
    gd_text = font_4.render('Game Durations:', true, black)
    s_text1 = font_4.render('Scores:', true, black)

    # Update the saved playtime before quitting
    rla_playtime = playtime
    rla_playtime_h = playtime_h
    rla_playtime_m = playtime_m
    rla_playtime_s = playtime_s
    total_balance_collected = total_balance_collected
    currency_spent = currency_spent
    purchases = purchases
    jump = jump
    jump_string = jump_string
    playtime = playtime_s + (playtime_m * 60) + (playtime_h * 3600)
    data = {
        "TPlaytime": rla_playtime,
        "PlaytimeHours": rla_playtime_h,
        "PlaytimeMinutes": rla_playtime_m,
        "PlaytimeSeconds": rla_playtime_s,
        "TotalBalanceCollected": total_balance_collected,
        "CurrencySpent": currency_spent,
        "Purchases": purchases,
        "Balance": balance,
        "GameCounter": game_counter,
        "JumpCounter": jump_key_pressed,
        "AverageJumps/Game": avjpg,
        "Scores": scores,
        "ColoursOwned": colour_list,
        "DesignsOwned": designs_list,
        "CustomSkinsOwned": custom_skins_list,
        "PrimaryColour": primary_colour,
        "SecondaryColour": secondary_colour,
        "EquippedDesign": design,
        "EquippedCustomSkin": custom_skin,
        "JumpKey": jump_string,
        "Jump": jump,
        "GameSpeedMultiplier": game_speed_multiplier,
        "StripeWidth": stripe_width,
        "OutlineSize": outline_size,
        "RadiusLength": radius_length,
        "ColourChangeInterval": colour_change_interval
    }

    data1 = {
        "AutoSaveState": autosave
    }

    AccountData = {
        "Account1": account1,
        "Account2": account2,
        "Account3": account3,
        "Account4": account4
    }

    if custom_skin is not None:
        design = None
    if custom_skin is None:
        player_rect = player.get_rect(bottomleft=(x, y))
        if design == 'rainbow':
            if game_start or game_started:
                player.fill(player_colour)
        if design != 'rainbow':
            player.fill(primary_colour)
        if design == 'stripes':
            draw_stripes(player, secondary_colour)
        if design == 'outline':
            pygame.draw.rect(screen, secondary_colour, player_rect, outline_size)
        if design == 'spotty':
            if game_start or game_started:
                draw_spots(player)
        if design == 'diamonds':
            if game_start or game_started:
                draw_diamonds(player)
        if design is None:
            player.fill(primary_colour)
    secondary_list = colour_list.copy()
    primary_list = colour_list.copy()
    try:
        secondary_list.remove(secondary_colour)
        primary_list.remove(primary_colour)
    except ValueError:
        pass
    mp = pygame.mouse.get_pos()
    if last_game_speed_multiplier != game_speed_multiplier and not dragging2:
        # Reverse the effect of the last multiplier
        tickk /= last_game_speed_multiplier

        # Apply the new multiplier
        tickk *= game_speed_multiplier
        last_game_speed_multiplier = game_speed_multiplier

    if quit3:
        if account1:
            with open("autosavestate.json", "w") as AutoState:
                json.dump(data1, AutoState, indent=2)
        if account2:
            with open("autosavestate1.json", "w") as AutoState:
                json.dump(data1, AutoState, indent=2)
        if account3:
            with open("autosavestate2.json", "w") as AutoState:
                json.dump(data1, AutoState, indent=2)
        if account4:
            with open("autosavestate3.json", "w") as AutoState:
                json.dump(data1, AutoState, indent=2)
        if autosave:
            if account1:
                with open("player_data.json", "w") as PlayerData:
                    json.dump(data, PlayerData, indent=2)
            if account2:
                with open("player_data1.json", "w") as PlayerData:
                    json.dump(data, PlayerData, indent=2)
            if account3:
                with open("player_data2.json", "w") as PlayerData:
                    json.dump(data, PlayerData, indent=2)
            if account4:
                with open("player_data3.json", "w") as PlayerData:
                    json.dump(data, PlayerData, indent=2)
            with open("account_data.json", "w") as AccountDataFile:
                json.dump(AccountData, AccountDataFile, indent=2)
            print('Progress saved!')
        if not autosave:
            print("Your progress has not been saved.")
        running = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit2:
            if account1:
                with open("autosavestate.json", "w") as AutoState:
                    json.dump(data1, AutoState, indent=2)
            if account2:
                with open("autosavestate1.json", "w") as AutoState:
                    json.dump(data1, AutoState, indent=2)
            if account3:
                with open("autosavestate2.json", "w") as AutoState:
                    json.dump(data1, AutoState, indent=2)
            if account4:
                with open("autosavestate3.json", "w") as AutoState:
                    json.dump(data1, AutoState, indent=2)

            if autosave:
                if account1:
                    with open("player_data.json", "w") as PlayerData:
                        json.dump(data, PlayerData, indent=2)

                if account2:
                    with open("player_data1.json", "w") as PlayerData:
                        json.dump(data, PlayerData, indent=2)

                if account3:
                    with open("player_data2.json", "w") as PlayerData:
                        json.dump(data, PlayerData, indent=2)

                if account4:
                    with open("player_data3.json", "w") as PlayerData:
                        json.dump(data, PlayerData, indent=2)

                with open("account_data.json", "w") as AccountDataFile:
                    json.dump(AccountData, AccountDataFile, indent=2)
                print('Progress saved!')

            if not autosave:
                print("Your progress has not been saved.")
            if not switch_accounts:
                pygame.quit()
                sys.exit()
            if switch_accounts:
                running = None

        if event.type == pygame.KEYDOWN:
            if event.key == jump:
                if game_start or game_started and can_jump:
                    jump_key_pressed += 1
                    if inverted_gravity:
                        velocity_y = -jump_strength
                    else:
                        velocity_y = jump_strength
                    can_jump = False
            if event.key == jump and pass_key and game_start:
                game_start = False
                game_started = True
                pass_key = False
                ticks = pygame.time.get_ticks()
            if event.key == jump and can_jump and game_started:
                if inverted_gravity:
                    velocity_y = -jump_strength
                else:
                    velocity_y = jump_strength
                can_jump = False
        if event.type == pygame.KEYUP and game_started:
            if event.key == jump:
                can_jump = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ms_rect.collidepoint(mp):
                if extras:
                    clrs = True
                    extras = False
            if (clrs or dsgns or cstm_skins) and ExtrasRec.collidepoint(mp):
                clrs = False
                dsgns = False
                cstm_skins = False
                extras = True
            if sa_rect.collidepoint(mp) or exit_rect.collidepoint(mp):
                if home_screen:
                    quit3 = True
            if autosave_rect.collidepoint(mp) and game_settings:
                autosave = not autosave
            if N_Rect.collidepoint(mp) and tp_confirmation:
                tp_confirmation = False
                game_settings = True
            if Y_Rect.collidepoint(mp) and tp_confirmation:
                running = False
            if back_rect.collidepoint(mp) and statistics:
                statistics = False
                home_screen = True
            if back_rect.collidepoint(mp) and game_stats:
                game_stats = False
                statistics = True
            if back_rect.collidepoint(mp) and shop_stats:
                shop_stats = False
                statistics = True
            if back_rect.collidepoint(mp) and time_stats:
                time_stats = False
                statistics = True
            if gameplay_rect.collidepoint(mp) and statistics:
                game_stats = True
                statistics = False
            if shop_rect11.collidepoint(mp) and statistics:
                shop_stats = True
                statistics = False
            if time_rect1.collidepoint(mp) and statistics:
                time_stats = True
                statistics = False
            if rrrct.collidepoint(mp) and play:
                play = False
                game_start = True
            if rrct.collidepoint(mp) and play:
                play = False
                levels = True
            if clrs:
                if item_rect1.collidepoint(mp) or rect2.collidepoint(mp):
                    if balance >= red_price and red not in colour_list:
                        colour_list.append(red)
                        colour_list.append('red')
                        balance -= red_price
                        currency_spent += red_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= red_price and red not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect2.collidepoint(mp) or rect3.collidepoint(mp):
                    if balance >= pink_price and pink not in colour_list:
                        colour_list.append(pink)
                        colour_list.append('pink')
                        balance -= pink_price
                        currency_spent += pink_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= pink_price and pink not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect3.collidepoint(mp) or rect4.collidepoint(mp):
                    if balance >= blue_price and blue not in colour_list:
                        colour_list.append(blue)
                        colour_list.append('blue')
                        balance -= blue_price
                        currency_spent += blue_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= blue_price and blue not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect4.collidepoint(mp) or rect5.collidepoint(mp):
                    if balance >= yellow_price and yellow not in colour_list:
                        colour_list.append(yellow)
                        balance -= yellow_price
                        currency_spent += yellow_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= yellow_price and yellow not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect5.collidepoint(mp) or rect6.collidepoint(mp):
                    if balance >= purple_price and purple not in colour_list:
                        colour_list.append(purple)
                        balance -= purple_price
                        currency_spent += purple_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= purple_price and purple not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect6.collidepoint(mp) or rect7.collidepoint(mp):
                    if balance >= bright_red_price and bright_red not in colour_list:
                        colour_list.append(bright_red)
                        colour_list.append('bright red')
                        balance -= bright_red_price
                        currency_spent += bright_red_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= bright_red_price and bright_red not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect7.collidepoint(mp) or rect8.collidepoint(mp):
                    if balance >= bright_green_price and bright_green not in colour_list:
                        colour_list.append(bright_green)
                        colour_list.append('bright green')
                        balance -= bright_green_price
                        currency_spent += bright_green_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= bright_green_price and bright_green not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect8.collidepoint(mp) or rect9.collidepoint(mp):
                    if balance >= bright_blue_price and bright_blue not in colour_list:
                        colour_list.append(bright_blue)
                        colour_list.append('bright blue')
                        balance -= bright_blue_price
                        currency_spent += bright_blue_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= bright_blue_price and bright_blue not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect9.collidepoint(mp) or rect10.collidepoint(mp):
                    if balance >= orange_price and orange not in colour_list:
                        colour_list.append(orange)
                        balance -= orange_price
                        currency_spent += orange_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= orange_price and orange not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect10.collidepoint(mp) or rect11.collidepoint(mp):
                    if balance >= white_price and white not in colour_list:
                        colour_list.append(white)
                        colour_list.append('white')
                        balance -= white_price
                        currency_spent += white_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= white_price and white not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect11.collidepoint(mp) or rect12.collidepoint(mp):
                    if balance >= black_price and black not in colour_list:
                        colour_list.append(black)
                        colour_list.append('black')
                        balance -= black_price
                        currency_spent += black_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= black_price and black not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if item_rect12.collidepoint(mp) or rect13.collidepoint(mp):
                    if balance >= grey_price and grey not in colour_list:
                        colour_list.append(grey)
                        colour_list.append('grey')
                        balance -= grey_price
                        currency_spent += grey_price
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                    elif not balance >= grey_price and grey not in colour_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
            if dsgns:
                if rect14.collidepoint(mp):
                    if balance >= stripes_price and 'stripes' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= stripes_price
                        currency_spent += stripes_price
                        designs_list.append('stripes')
                    elif not balance >= stripes_price and 'stripes' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect15.collidepoint(mp):
                    if balance >= outline_price and 'outline' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= outline_price
                        currency_spent += outline_price
                        designs_list.append('outline')
                    elif balance < outline_price and 'outline' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect16.collidepoint(mp):
                    if balance >= spotty_price and 'spotty' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= spotty_price
                        currency_spent += spotty_price
                        designs_list.append('spotty')
                    elif balance < spotty_price and 'spotty' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect17.collidepoint(mp):
                    if balance >= ic_price and 'inner circle' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= ic_price
                        currency_spent += ic_price
                        designs_list.append('inner circle')
                    elif balance < ic_price and 'inner circle' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect18.collidepoint(mp):
                    if balance >= diamonds_price and 'diamonds' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= diamonds_price
                        currency_spent += diamonds_price
                        designs_list.append('diamonds')
                    if balance < diamonds_price and 'diamonds' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect19.collidepoint(mp):
                    if balance >= rainbow_price and 'rainbow' not in designs_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= rainbow_price
                        currency_spent += rainbow_price
                        designs_list.append('rainbow')
                    if balance < rainbow_price and 'rainbow' not in designs_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
            if cstm_skins:
                if rect14.collidepoint(mp):
                    if balance >= nugget_price and 'cn' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= nugget_price
                        currency_spent += nugget_price
                        custom_skins_list.append('cn')
                    if balance < nugget_price and 'cn' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect15.collidepoint(mp):
                    if balance >= alien_price and 'alien' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= alien_price
                        currency_spent += alien_price
                        custom_skins_list.append('alien')
                    if balance < alien_price and 'alien' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect16.collidepoint(mp):
                    if balance >= flower_price and 'flower' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= flower_price
                        currency_spent += flower_price
                        custom_skins_list.append('flower')
                    if balance < flower_price and 'flower' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect17.collidepoint(mp):
                    if balance >= mars_price and 'mars' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= mars_price
                        currency_spent += mars_price
                        custom_skins_list.append('mars')
                    if balance < mars_price and 'mars' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect18.collidepoint(mp):
                    if balance >= plane_price and 'plane' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= plane_price
                        currency_spent += plane_price
                        custom_skins_list.append('plane')
                    if balance < plane_price and 'plane' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
                if rect19.collidepoint(mp):
                    if balance >= smurf_price and 'smurf' not in custom_skins_list:
                        pygame.mixer.music.load(
                            'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                        pygame.mixer.music.play()
                        purchases += 1
                        balance -= smurf_price
                        currency_spent += smurf_price
                        custom_skins_list.append('smurf')
                    if balance < smurf_price and 'smurf' not in custom_skins_list:
                        pk1 = True
                        tcks = pygame.time.get_ticks()
            elif back_rect1.collidepoint(mp):
                if cstm_skins or dsgns:
                    cstm_skins = False
                    home_screen = True
                    dsgns = False
                if clrs:
                    home_screen = True
                    clrs = False
            if play_rect.collidepoint(mp) and home_screen:
                home_screen = False
                game_started = None
                play = True
            if handle_rect2.collidepoint(event.pos) and game_settings:
                dragging2 = True
            if tp_rect.collidepoint(mp) and game_settings:
                tp_confirmation = True
                game_settings = False
            if cs_r.collidepoint(mp):  # Check if mouse is on the 'Custom skins' rectangle
                if clrs or dsgns or cstm_skins:
                    clrs = False  # Switch states
                    dsgns = False
                    cstm_skins = True  # Enable the custom skins screen
            if colour_r.collidepoint(mp):
                if clrs or dsgns or cstm_skins:
                    clrs = True
                    dsgns = False
                    cstm_skins = False
            if ds_r.collidepoint(mp) and secondary_colour is not None:
                if clrs or dsgns or cstm_skins:
                    clrs = False
                    dsgns = True
                    cstm_skins = False
            if ds_r.collidepoint(mp) and secondary_colour is None:
                if clrs or dsgns or cstm_skins:
                    pkk = True
                    t1cks = pygame.time.get_ticks()
            if info_rect.collidepoint(mp) and home_screen:
                information = True
                home_screen = False
            elif back_rect.collidepoint(mp) and information:
                information = False
                home_screen = True
            if shop_rect.collidepoint(mp) and home_screen:
                home_screen = False
                clrs = True
            if game_settings_rect.collidepoint(mp):
                if game_settings or character_customisation:
                    game_settings = True
                    character_customisation = False
            if character_customisation_rect.collidepoint(mp):
                if game_settings or character_customisation:
                    game_settings = False
                    character_customisation = True
            if back_rect1.collidepoint(mp):
                if game_settings or character_customisation:
                    game_settings = False
                    character_customisation = False
                    home_screen = True
            if text01_rect.collidepoint(mp) and game_settings:
                blit_text02 = True
                text01 = font_3.render(jump_string, True, text_colour)
            if not text01_rect.collidepoint(mp) and game_settings:
                blit_text02 = False
                text01 = font_3.render(jump_string, True, text_colour)
            if settings_rect1.collidepoint(mp) and home_screen:
                home_screen = False
                game_settings = True
            if bar_chart_rect.collidepoint(mp) and home_screen:
                home_screen = False
                statistics = True
            if wheel_rect.collidepoint(mp) and home_screen:
                home_screen = False
                wheel_spinner = True
            if home_rect.collidepoint(mp) and game_start:
                game_start = False
                home_screen = True
            if colours and character_customisation:
                if t2ext_rect.collidepoint(mp) and secondary_colors:
                    primary_colors = True
                    secondary_colors = False
                if t3ext_rect.collidepoint(mp) and primary_colors:
                    primary_colors = False
                    secondary_colors = True
            if dsr.collidepoint(mp) and character_customisation:
                desins = True
                colours = False
                customm_skins = False
            if csr.collidepoint(mp) and character_customisation:
                customm_skins = True
                colours = False
                desins = False
            if colourr.collidepoint(mp) and character_customisation:
                colours = True
                customm_skins = False
                desins = False
            elif restart_button_rect.collidepoint(mp) and end_screen:  # Check for restart button click
                end_screen = False
                game_start = True
                restart_game()  # Restart the game
            if character_customisation and design_selection and desins:
                if stripes_rect.collidepoint(mp) and 'stripes' in designs_list:
                    design = 'stripes'
                if outline_rect.collidepoint(mp) and 'outline' in designs_list:
                    design = 'outline'
                if spotty_rect.collidepoint(mp) and 'spotty' in designs_list:
                    design = 'spotty'
                if diamond_rect.collidepoint(mp) and 'diamonds' in designs_list:
                    design = 'diamonds'
                if rainbow_rect.collidepoint(mp) and 'rainbow' in designs_list:
                    design = 'rainbow'
                if ic_rect.collidepoint(mp) and 'inner circle' in designs_list:
                    design = 'inner circle'
                if NoneRect.collidepoint(mp):
                    design = None
            if character_customisation and customm_skins:
                if cn_rect.collidepoint(mp) and 'cn' in custom_skins_list:
                    custom_skin = 'cn'
                if alien_rect.collidepoint(mp) and 'alien' in custom_skins_list:
                    custom_skin = 'alien'
                if flower_rect.collidepoint(mp) and 'flower' in custom_skins_list:
                    custom_skin = 'flower'
                if mars_rect.collidepoint(mp) and 'mars' in custom_skins_list:
                    custom_skin = 'mars'
                if plane_rect.collidepoint(mp) and 'plane' in custom_skins_list:
                    custom_skin = 'plane'
                if smurf_rect.collidepoint(mp) and 'smurf' in custom_skins_list:
                    custom_skin = 'smurf'
                if NoneRect.collidepoint(mp):
                    custom_skin = None
            if primary_colors and character_customisation and colours:
                if default_green_rect.collidepoint(mp):
                    if secondary_colour == [0, 190, 0]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [0, 190, 0]
                    if secondary_colour != [0, 190, 0]:
                        primary_colour = [0, 190, 0]
                if red_rect.collidepoint(mp) and [200, 0, 0] in colour_list:
                    if secondary_colour == [200, 0, 0]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [200, 0, 0]
                    if secondary_colour != [200, 0, 0]:
                        primary_colour = [200, 0, 0]
                if pink_rect.collidepoint(mp) and [255, 120, 203] in colour_list:
                    if secondary_colour == [255, 120, 203]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [255, 120, 203]
                    if secondary_colour != [255, 120, 203]:
                        primary_colour = [255, 120, 203]
                if blue_rect.collidepoint(mp) and [0, 0, 180] in colour_list:
                    if secondary_colour == [0, 0, 180]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [0, 0, 180]
                    if secondary_colour != [0, 0, 180]:
                        primary_colour = [0, 0, 180]
                if yellow_rect.collidepoint(mp) and yellow in colour_list:
                    if secondary_colour == yellow:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = yellow
                    if secondary_colour != yellow:
                        primary_colour = yellow
                if purple_rect.collidepoint(mp) and purple in colour_list:
                    if secondary_colour == purple:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = purple
                    if secondary_colour != purple:
                        primary_colour = purple
                if bright_red_rect.collidepoint(mp) and [255, 0, 0] in colour_list:
                    if secondary_colour == [255, 0, 0]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [255, 0, 0]
                    if secondary_colour != [255, 0, 0]:
                        primary_colour = [255, 0, 0]
                if bright_green_rect.collidepoint(mp) and [0, 255, 0] in colour_list:
                    if secondary_colour == [0, 255, 0]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [0, 255, 0]
                    if secondary_colour != [0, 255, 0]:
                        primary_colour = [0, 255, 0]
                if bright_blue_rect.collidepoint(mp) and [0, 0, 255] in colour_list:
                    if secondary_colour == [0, 0, 255]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [0, 0, 255]
                    if secondary_colour != [0, 0, 255]:
                        primary_colour = [0, 0, 255]
                if orange_rect.collidepoint(mp) and orange in colour_list:
                    if secondary_colour == orange:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = orange
                    if secondary_colour != orange:
                        primary_colour = orange
                if white_rect.collidepoint(mp) and [255, 255, 255] in colour_list:
                    if secondary_colour == [255, 255, 255]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [255, 255, 255]
                    if secondary_colour != [255, 255, 255]:
                        primary_colour = [255, 255, 255]
                if black_rect.collidepoint(mp) and [0, 0, 0] in colour_list:
                    if secondary_colour == [0, 0, 0]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [0, 0, 0]
                    if secondary_colour != [0, 0, 0]:
                        primary_colour = [0, 0, 0]
                if grey_rect.collidepoint(mp) and [128, 128, 128] in colour_list:
                    if secondary_colour == [128, 128, 128]:
                        secondary_colour = random.choice(secondary_list)
                        primary_colour = [128, 128, 128]
                    if secondary_colour != [128, 128, 128]:
                        primary_colour = [128, 128, 128]

            if secondary_colors and character_customisation and colours:
                if default_green_rect.collidepoint(mp):
                    if primary_colour == [0, 190, 0]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [0, 190, 0]
                    if primary_colour != [0, 190, 0]:
                        secondary_colour = [0, 190, 0]
                if red_rect.collidepoint(mp) and [200, 0, 0] in colour_list:
                    if primary_colour == [200, 0, 0]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [200, 0, 0]
                    if primary_colour != [200, 0, 0]:
                        secondary_colour = [200, 0, 0]
                if pink_rect.collidepoint(mp) and [255, 120, 203] in colour_list:
                    if primary_colour == [255, 120, 203]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [255, 120, 203]
                    if primary_colour != [255, 120, 203]:
                        secondary_colour = [255, 120, 203]
                if blue_rect.collidepoint(mp) and [0, 0, 180] in colour_list:
                    if primary_colour == [0, 0, 180]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [0, 0, 180]
                    if primary_colour != [0, 0, 180]:
                        secondary_colour = [0, 0, 180]
                if yellow_rect.collidepoint(mp) and yellow in colour_list:
                    if primary_colour == yellow:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = yellow
                    if primary_colour != yellow:
                        secondary_colour = yellow
                if purple_rect.collidepoint(mp) and purple in colour_list:
                    if primary_colour == purple:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = purple
                    if primary_colour != purple:
                        secondary_colour = purple
                if bright_red_rect.collidepoint(mp) and [255, 0, 0] in colour_list:
                    if primary_colour == [255, 0, 0]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [255, 0, 0]
                    if primary_colour != [255, 0, 0]:
                        secondary_colour = [255, 0, 0]
                if bright_green_rect.collidepoint(mp) and [0, 255, 0] in colour_list:
                    if primary_colour == [0, 255, 0]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [0, 255, 0]
                    if primary_colour != [0, 255, 0]:
                        secondary_colour = [0, 255, 0]
                if bright_blue_rect.collidepoint(mp) and [0, 0, 255] in colour_list:
                    if primary_colour == [0, 0, 255]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [0, 0, 255]
                    if primary_colour != [0, 0, 255]:
                        secondary_colour = [0, 0, 255]
                if orange_rect.collidepoint(mp) and orange in colour_list:
                    if primary_colour == orange:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = orange
                    if primary_colour != orange:
                        secondary_colour = orange
                if white_rect.collidepoint(mp) and [255, 255, 255] in colour_list:
                    if primary_colour == [255, 255, 255]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [255, 255, 255]
                    if primary_colour != [255, 255, 255]:
                        secondary_colour = [255, 255, 255]
                if black_rect.collidepoint(mp) and [0, 0, 0] in colour_list:
                    if primary_colour == [0, 0, 0]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [0, 0, 0]
                    if primary_colour != [0, 0, 0]:
                        secondary_colour = [0, 0, 0]
                if grey_rect.collidepoint(mp) and [128, 128, 128] in colour_list:
                    if primary_colour == [128, 128, 128]:
                        primary_colour = random.choice(primary_list)
                        secondary_colour = [128, 128, 128]
                    if primary_colour != [128, 128, 128]:
                        secondary_colour = [128, 128, 128]
            if tax_r.collidepoint(mp) and design_customisation and desins and character_customisation:
                design_selection = True
                design_customisation = False
            if tax1_r.collidepoint(mp) and design_selection and desins and character_customisation:
                design_selection = False
                design_customisation = True
            if handle_rect.collidepoint(event.pos) and character_customisation and desins and 'stripes' in designs_list:
                dragging = True
            if handle_rect1.collidepoint(
                    event.pos) and character_customisation and desins and design_customisation and 'outline' in designs_list:
                dragging1 = True
            if (handle_rect5.collidepoint(mp) and character_customisation and desins and design_customisation and
                    'inner circle' in designs_list):
                dragging5 = True
            if handle_rect3.collidepoint(
                    mp) and character_customisation and desins and design_customisation and 'rainbow' in designs_list:
                dragging3 = True

        if event.type == pygame.MOUSEBUTTONDOWN and back_rect1.collidepoint(mp):
            if clrs or dsgns or cstm_skins:
                clrs = False
                dsgns = False
                cstm_skins = False
                home_screen = True
        if event.type == pygame.KEYDOWN and blit_text02 and game_settings:
            changed_key = event.key
            if key_names.get(changed_key) is not None:
                jump = changed_key
                jump_string = key_names.get(jump)
                text01 = font1.render(jump_string, True, text_colour)
            elif key_names.get(changed_key) is None:
                invalid_key = True
                lticks = pygame.time.get_ticks()
            blit_text02 = False
        if event.type == pygame.MOUSEBUTTONUP:
            dragging2 = False
            dragging = False
            dragging1 = False
            dragging5 = False
            dragging3 = False
        if event.type == pygame.MOUSEMOTION and dragging1 and character_customisation and desins:
            # Update handle position
            mouse_x, _ = event.pos
            new_x1 = max(slider_x1, min(mouse_x - handle_size1 // 2, slider_x1 + slider_width1 - handle_size1))
            handle_rect1.x = new_x1
            # Update slider value
            outline_size = int(((handle_rect1.x - slider_x1) / slider_range1) * (max_value1 - min_value1) + min_value1)
        if event.type == pygame.MOUSEMOTION and game_settings:
            if dragging2:
                mouse_x, _ = event.pos
                new_x = max(slider_x2, min(mouse_x - handle_size2 // 2, slider_x2 + slider_width2 - handle_size2))
                handle_rect2.x = new_x

                # Update slider value as a float
                game_speed_multiplier = (((handle_rect2.x - slider_x2) / slider_range2) * (
                        max_value2 - min_value2) + min_value2)

                # Snap to nearest step (0.1 increments)
                game_speed_multiplier = round(game_speed_multiplier / step2) * step2
        if event.type == pygame.MOUSEMOTION and dragging and character_customisation and desins:
            # Update handle position
            mouse_x, _ = event.pos
            new_x = max(slider_x, min(mouse_x - handle_size // 2, slider_x + slider_width - handle_size))
            handle_rect.x = new_x

            # Update slider value
            stripe_width = int(((handle_rect.x - slider_x) / slider_range) * (max_value - min_value) + min_value)
        if event.type == pygame.MOUSEMOTION and dragging5:
            # Update handle position
            mouse_x, _ = event.pos
            new_x5 = max(slider_x5, min(mouse_x - handle_size5 // 2, slider_x5 + slider_width5 - handle_size5))
            handle_rect5.x = new_x5

            # Update slider value
            radius_length = int(((handle_rect5.x - slider_x5) / slider_range5) * (max_value5 - min_value5) + min_value5)
        if event.type == pygame.MOUSEMOTION and dragging3:
            # Update handle position
            mouse_x, _ = event.pos
            new_x3 = max(slider_x3, min(mouse_x - handle_size3 // 2, slider_x3 + slider_width3 - handle_size3))
            handle_rect3.x = new_x3

            # Update slider value
            colour_change_interval = ((handle_rect3.x - slider_x3) / slider_range3) * (
                    max_value3 - min_value3) + min_value3
            colour_change_interval = round(
                colour_change_interval / step_size) * step_size  # Round to the nearest step size
    if restart_button_rect.collidepoint(mp) and end_screen:
        restart_game()
    if home_button_rect.collidepoint(mp) and end_screen:
        restart_game1()

    if home_screen:
        game_started = False
        screen.fill((50, 100, 180))
        t1ext = font1.render('Play:', True, black)
        info_text = font1.render('Information:', True, black)
        settings_text1 = font1.render('Settings:', True, black)
        statistics_text = font1.render('Statistics:', True, black)
        ws_text = font1.render('Wheel Spinner:', True, black)
        acc_text = font1.render('Account 1', true, black)
        acc_text2 = font1.render('Account 2', true, black)
        acc_text3 = font1.render('Account 3', True, black)
        acc_text4 = font1.render('Account 4', true, black)
        acc_rect = acc_text.get_rect(topright=(990, 0))
        info_trect = info_text.get_rect(midtop=(835, 40))
        t1ext_rect = t1ext.get_rect(midbottom=(500, 370))
        settings_rect2 = settings_text1.get_rect(midtop=(500, 40))
        statistics_rect = statistics_text.get_rect(center=(175, 355))
        ws_rect = ws_text.get_rect(center=(840, 350))
        screen.blit(line1, line1_rect)
        screen.blit(line2, line2_rect)
        screen.blit(line1, line3_rect)
        balance_text = font4.render(str(balance), True, black)
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))
        if play_rect.collidepoint(mp):
            screen.blit(play_button_h, play_rect)
        if not play_rect.collidepoint(mp):
            screen.blit(play_button, play_rect)
        if info_rect.collidepoint(mp):
            screen.blit(info_h, info_rect)
        if not info_rect.collidepoint(mp):
            screen.blit(info, info_rect)
        if shop_rect.collidepoint(mp):
            screen.blit(shopping_icon_h, shop_rect)
        if not shop_rect.collidepoint(mp):
            screen.blit(shopping_icon, shop_rect)
        if settings_rect1.collidepoint(mp):
            screen.blit(settings_icon_h, settings_rect1)
        if not settings_rect1.collidepoint(mp):
            screen.blit(settings_icon, settings_rect1)
        if bar_chart_rect.collidepoint(mp):
            screen.blit(bar_chart_h, bar_chart_rect)
        if not bar_chart_rect.collidepoint(mp):
            screen.blit(bar_chart, bar_chart_rect)
        if wheel_rect.collidepoint(mp):
            screen.blit(spin_wheel_h, wheel_rect)
        if not wheel_rect.collidepoint(mp):
            screen.blit(spin_wheel, wheel_rect)
        screen.blit(t1ext, t1ext_rect)
        screen.blit(info_text, info_trect)
        screen.blit(shoppingg_text, shoppingg_rect)
        screen.blit(settings_text1, settings_rect2)
        screen.blit(statistics_text, statistics_rect)
        screen.blit(ws_text, ws_rect)
        screen.blit(sa_text1, sa_rect)
        screen.blit(exit_icon, exit_rect)
        if account1:
            screen.blit(acc_text, acc_rect)
        if account2:
            screen.blit(acc_text2, acc_rect)
        if account3:
            screen.blit(acc_text3, acc_rect)
        if account4:
            screen.blit(acc_text4, acc_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if statistics:
        screen.fill((50, 100, 180))
        stats_text = font1.render('Statistics', true, white)
        game_text = font.render('Gameplay', true, black)
        shop_text1 = font.render('Shop Stats', True, black)
        time_text = font.render('Time Stats', True, black)
        stats_rect = stats_text.get_rect(midtop=(500, 10))
        game_rect1 = game_text.get_rect(center=(248.5, 148.5))
        shop_rect1 = shop_text1.get_rect(center=(751.5, 148.5))
        time_rect = time_text.get_rect(center=(248.5, 451.5))

        if back_rect.collidepoint(mp):
            screen.blit(ba_h, back_rect)
        if not back_rect.collidepoint(mp):
            screen.blit(back_arrow, back_rect)

        screen.blit(line1, (497, 0))
        screen.blit(line2, line2_rect)
        screen.blit(game_text, game_rect1)
        screen.blit(shop_text1, shop_rect1)
        screen.blit(time_text, time_rect)
        if gameplay_rect.collidepoint(mp):
            pygame.draw.rect(screen, black, gameplay_rect, 4)
        if time_rect1.collidepoint(mp):
            pygame.draw.rect(screen, black, time_rect1, 4)
        if shop_rect11.collidepoint(mp):
            pygame.draw.rect(screen, black, shop_rect11, 4)
        if rect23.collidepoint(mp):
            pygame.draw.rect(screen, black, rect23, 4)
        my_instance.draw()

        screen.blit(stats_text, stats_rect)
        pygame.display.flip()
        clock.tick(600)

    if game_stats:
        screen.fill((50, 100, 180))
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, black, box1_rect, 3)
        pygame.draw.rect(screen, black, box_rect, 3)
        screen.blit(gs_text, gs_rect)
        screen.blit(tgp_text, tgp_rect)
        screen.blit(tj_text, tj_rect)
        screen.blit(avj_text, avj_rect)
        screen.blit(gd_text, gd_rect)
        screen.blit(bgd_text, bgd_rect)
        screen.blit(avgd_text, avgd_rect)
        screen.blit(lgd_text, lgd_rect)
        screen.blit(s_text1, s_rect5)
        screen.blit(bs_text, bs_rect)
        screen.blit(as_text, as_rect)
        screen.blit(ls_text, ls_rect)
        screen.blit(gp_text, gp_rect)
        if back_rect.collidepoint(mp):
            screen.blit(ba_h, back_rect)
            statistics = True
            game_stats = False
        if not back_rect.collidepoint(mp):
            screen.blit(back_arrow, back_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if shop_stats:
        screen.fill((50, 100, 180))
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        c_text = font_4.render('Currency:', True, black)
        tce_text = font1.render(f'Total Currency Earned: {total_balance_collected}', True, black)
        tcs_text = font1.render(f'Total Currency Spent: {currency_spent}', true, black)
        p_text = font_4.render('Purchases:', True, black)
        tip_text = font1.render(f'Total Item Purchases: {purchases}', true, black)
        ss_text1 = font4.render('Shop Stats', True, black)
        balance_stringg = font4.render('Balance:', True, black)
        balance_string = font4.render(str(balance), True, black)
        ss_rect = ss_text1.get_rect(midtop=(500, 40))
        c_rect = c_text.get_rect(topleft=(180, 100))
        tce_rect = tce_text.get_rect(topleft=(180, 150))
        tcs_rect = tcs_text.get_rect(topleft=(180, 185))
        p_rect = p_text.get_rect(topleft=(180, 225))
        tip_rect = tip_text.get_rect(topleft=(180, 275))
        screen.blit(c_text, c_rect)
        screen.blit(tce_text, tce_rect)
        screen.blit(tcs_text, tcs_rect)
        screen.blit(p_text, p_rect)
        screen.blit(tip_text, tip_rect)
        screen.blit(ss_text1, ss_rect)
        screen.blit(balance_stringg, (180, 490))
        screen.blit(coin, (345, 495))
        screen.blit(balance_string, (385, 490))
        if back_rect.collidepoint(mp):
            screen.blit(ba_h, back_rect)
            statistics = True
            shop_stats = False
        if not back_rect.collidepoint(mp):
            screen.blit(back_arrow, back_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if time_stats:
        screen.fill((50, 100, 180))
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        time_stats = font4.render('Time Stats', True, black)
        time_rect = time_stats.get_rect(midtop=(500, 40))
        playtime_seconds = str(playtime_s).zfill(2)
        playtime_minutes = str(playtime_m).zfill(2)
        playtime_hours = str(playtime_h).zfill(2)
        combined_string = font4.render('Playtime: ' + playtime_hours + ':' + playtime_minutes + ':' + playtime_seconds,
                                       True, black)
        screen.blit(combined_string, (180, 100))
        screen.blit(time_stats, time_rect)
        if back_rect.collidepoint(mp):
            screen.blit(ba_h, back_rect)
            statistics = True
            time_stats = False
        if not back_rect.collidepoint(mp):
            screen.blit(back_arrow, back_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if play:
        screen.fill((50, 100, 180))
        tyxt = font4.render('Endless', true, black)
        tyxt1 = font4.render('Levels', true, black)
        screen.blit(line1, (495, 0))
        screen.blit(tyxt, (190, 265))
        screen.blit(tyxt1, (690, 265))
        pygame.draw.rect(screen, black, rrrct, 10)
        pygame.draw.rect(screen, black, rrct, 10)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if game_start:
        screen.fill((50, 100, 180))
        home_text1 = font1.render('Home', True, black)
        home_trect = home_text1.get_rect(midright=(925, 220))
        txtt = 'Press ' + jump_string + ' to start.'
        text = font.render(txtt, True, (0, 0, 0))
        text_rect = text.get_rect(center=(500, 280))
        character_customisation = False
        balance_text = font4.render(str(balance), True, black)
        highest_score = get_highest_score()
        highest_score_text = font1.render(f'High Score: {highest_score}', True, 'Black')
        screen.blit(highest_score_text, (20, 100))
        screen.blit(text, text_rect)
        if custom_skin is None:
            screen.blit(player, player_rect)
        screen.blit(cloud, (0, 0))
        screen.blit(cloud, (200, 0))
        screen.blit(cloud, (400, 0))
        screen.blit(cloud, (600, 0))
        screen.blit(cloud, (800, 0))
        screen.blit(cloud, (0, 513))
        screen.blit(cloud, (200, 513))
        screen.blit(cloud, (400, 513))
        screen.blit(cloud, (600, 513))
        screen.blit(cloud, (800, 513))
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))
        if home_rect.collidepoint(mp):
            screen.blit(home_icon_h, home_rect)
        if not home_rect.collidepoint(mp):
            screen.blit(home_icon, home_rect)
        screen.blit(home_text1, home_trect)
        if design == 'outline':
            pygame.draw.rect(screen, secondary_colour, player_rect, outline_size)
        if design == 'inner circle':
            draw_circle(radius_length, (player_rect.x + 20, player_rect.y + 20))
        if design == 'diamonds':
            draw_diamonds(player)
        if design == 'rainbow':
            frame_count += 1
            if frame_count >= colour_change_interval:
                frame_count = 0  # Reset frame counter
                player_colour = next(color_cycle)  # Get the next color in the cycle
        if custom_skin == 'cn':
            player_rect = cn.get_rect(bottomleft=(x, y))
            screen.blit(cn, player_rect)
        if custom_skin == 'alien':
            player_rect = alien.get_rect(bottomleft=(x, y))
            screen.blit(alien, player_rect)
        if custom_skin == 'flower':
            player_rect = flower.get_rect(bottomleft=(x, y))
            screen.blit(flower, player_rect)
        if custom_skin == 'mars':
            player_rect = mars.get_rect(bottomleft=(x, y))
            screen.blit(mars, player_rect)
        if custom_skin == 'plane':
            player_rect = plane.get_rect(bottomleft=(x, y))
            screen.blit(plane, player_rect)
        if custom_skin == 'smurf':
            player_rect = smurf.get_rect(bottomleft=(x, y))
            screen.blit(smurf, player_rect)
        pygame.display.flip()
        clock.tick(tickk)

    if game_settings:
        game_started = False
        if autosave:
            laxa = 'On'
        if not autosave:
            laxa = 'Off'
        autosave_text = font1.render('Autosave: ' + laxa, true, black)
        screen.fill((50, 100, 180))
        gsc = default_green
        tp1_text = font1.render('Terminate Progress', True, black)
        tp1_rect = tp1_text.get_rect(center=(500, 520))
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        screen.blit(settings_text, settings_rect)
        screen.blit(game_settings_text, game_settings_rect)
        screen.blit(character_customisation_text, character_customisation_rect)
        screen.blit(text0, text0_rect)
        screen.blit(text00, text00_rect)
        screen.blit(text01, text01_rect)
        screen.blit(autosave_text, autosave_rect)
        if tp_rect.collidepoint(mp):
            pygame.draw.rect(screen, bright_red, tp_rect)
        if not tp_rect.collidepoint(mp):
            pygame.draw.rect(screen, red, tp_rect)
        screen.blit(tp1_text, tp1_rect)
        if back_rect1.collidepoint(mp):
            screen.blit(ba_h, back_rect1)
        if not back_rect1.collidepoint(mp):
            screen.blit(back_arrow, back_rect1)
        if character_customisation_rect.collidepoint(mp):
            ccc = grey
        if not character_customisation_rect.collidepoint(mp):
            ccc = black
        if text01_rect.collidepoint(mp):
            text_colour = grey
        if not text01_rect.collidepoint(mp):
            text_colour = black
        if blit_text02:
            text_colour = default_green
            text04 = font2.render('press any key to change or', True, black)
            text05 = font2.render('click anywhere else to cancel', True, black)
            screen.blit(text04, text02_rect)
            screen.blit(text05, (text02_rect.x, text02_rect.y + 24))
        if not blit_text02:
            screen.blit(text02, text02_rect)
        game_settings_text = font_1.render('Game Settings', True, gsc)
        character_customisation_text = font_1.render('Character Customisation', True, ccc)
        pygame.draw.rect(screen, grey, slider_rect2)
        pygame.draw.rect(screen, white, handle_rect2)
        pygame.draw.rect(screen, black, handle_rect2, 2)
        text1111 = font1.render(f'Game Speed: {game_speed_multiplier:.1f}x', True,
                                black)  # Display with 1 decimal place
        screen.blit(text1111, (slider_x2, slider_y2 - 50))
        text01 = font_3.render(jump_string, True, text_colour)

        surfa = pygame.Surface((700, 10))
        surfa.fill(black)

        screen.blit(surfa, (150, 250))

        if invalid_key:
            current_tcks = -1 * (lticks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, reeect)
            screen.blit(txxxt, reect)
            if truncate(current_tcks / 1000) >= 2:
                invalid_key = False
        my_instance.draw()

        pygame.display.flip()
        clock.tick(600)

    if tp_confirmation:
        screen.fill((50, 100, 180))
        laxative = font.render('Do you wish to proceed?', True, red)
        laxatives = font1.render('Yes', True, black)
        laxative1 = font1.render('No', True, black)
        laxative_rect = laxative.get_rect(center=(500, 100))
        laxatives_rect = laxatives.get_rect(center=(300, 500))
        laxative1_rect = laxative1.get_rect(center=(700, 500))
        if Y_Rect.collidepoint(mp):
            pygame.draw.rect(screen, bright_red, Y_Rect)
        if not Y_Rect.collidepoint(mp):
            pygame.draw.rect(screen, red, Y_Rect)
        if N_Rect.collidepoint(mp):
            pygame.draw.rect(screen, bright_green, N_Rect)
        if not N_Rect.collidepoint(mp):
            pygame.draw.rect(screen, default_green, N_Rect)
        screen.blit(laxative, laxative_rect)
        screen.blit(laxatives, laxatives_rect)
        screen.blit(laxative1, laxative1_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if character_customisation:
        game_started = False
        screen.fill((50, 100, 180))

        ccc = default_green
        back_rect1 = back_arrow.get_rect(midleft=(10, 300))
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        pygame.draw.rect(screen, black, pygame.Rect(150, 87, 700, 50), 3)

        screen.blit(settings_text, settings_rect)
        game_settings_text = font_1.render('Game Settings', True, gsc)
        character_customisation_text = font_1.render('Character Customisation', True, ccc)
        screen.blit(game_settings_text, game_settings_rect)
        screen.blit(character_customisation_text, character_customisation_rect)
        if back_rect1.collidepoint(mp):
            screen.blit(ba_h, back_rect1)
        if not back_rect1.collidepoint(mp):
            screen.blit(back_arrow, back_rect1)
        if game_settings_rect.collidepoint(mp):
            gsc = grey
        if not game_settings_rect.collidepoint(mp):
            gsc = black

        if colourr.collidepoint(mp) and not colours:
            ctcs = grey
        if not colourr.collidepoint(mp) and not colours:
            ctcs = black
        if colours:
            player_rect1.x = 480
            player_rect1.y = 370
            toxt = font1.render('Colour Key:', True, black)
            toxt1 = font1.render('Green - is equipped as Primary Colour.', True, default_green)
            toxt2 = font1.render('Green - is equipped as Secondary Colour.', True, default_green)
            toxt3 = font1.render('Red - owned but not equipped.', True, red)
            toxt4 = font1.render('Black - is not owned.', True, black)
            screen.blit(toxt, (180, 200))
            screen.blit(toxt3, (180, 280))
            screen.blit(toxt4, (180, 320))
            screen.blit(default_green_text, default_green_rect)
            screen.blit(red_text, red_rect)
            screen.blit(pink_text, pink_rect)
            screen.blit(blue_text, blue_rect)
            screen.blit(yellow_text, yellow_rect)
            screen.blit(purple_text, purple_rect)
            screen.blit(bright_red_text, bright_red_rect)
            screen.blit(bright_green_text, bright_green_rect)
            screen.blit(bright_blue_text, bright_blue_rect)
            screen.blit(orange_text, orange_rect)
            screen.blit(white_text, white_rect)
            screen.blit(black_text, black_rect)
            screen.blit(grey_text, grey_rect)
            ctcs = default_green
            screen.blit(t2ext, t2ext_rect)
            screen.blit(t3ext, t3ext_rect)
            if primary_colors:
                screen.blit(toxt1, (180, 240))
                pcc = default_green
                if t3ext_rect.collidepoint(mp):
                    scc = grey
                if not t3ext_rect.collidepoint(mp):
                    scc = black

                if [0, 190, 0] == primary_colour:
                    default_green_colour = [0, 190, 0]
                if [0, 190, 0] != primary_colour:
                    default_green_colour = red
                if [200, 0, 0] == primary_colour:
                    red_colour = default_green
                if [200, 0, 0] != primary_colour and [200, 0, 0] in colour_list:
                    red_colour = red
                if [200, 0, 0] != primary_colour and [200, 0, 0] not in colour_list:
                    red_colour = black
                if [255, 120, 203] == primary_colour:
                    pink_colour = default_green
                if [255, 120, 203] != primary_colour and [255, 120, 203] in colour_list:
                    pink_colour = red
                if [255, 120, 203] not in colour_list:
                    pink_colour = black
                if [0, 0, 180] == primary_colour:
                    blue_colour = default_green
                if [0, 0, 180] not in colour_list:
                    blue_colour = black
                if [0, 0, 180] in colour_list and [0, 0, 180] != primary_colour:
                    blue_colour = red
                if yellow == primary_colour:
                    yellow_colour = default_green
                if yellow not in colour_list:
                    yellow_colour = black
                if yellow != primary_colour and yellow in colour_list:
                    yellow_colour = red
                if purple not in colour_list:
                    purple_colour = black
                if purple == primary_colour:
                    purple_colour = default_green
                if purple != primary_colour and purple in colour_list:
                    purple_colour = red
                if [255, 0, 0] == primary_colour:
                    bright_red_colour = default_green
                if [255, 0, 0] in colour_list and [255, 0, 0] != primary_colour:
                    bright_red_colour = red
                if [255, 0, 0] not in colour_list:
                    bright_red_colour = black
                if [0, 255, 0] not in colour_list:
                    bright_green_colour = black
                if [0, 255, 0] == primary_colour:
                    bright_green_colour = default_green
                if [0, 255, 0] != primary_colour and [0, 255, 0] in colour_list:
                    bright_green_colour = red
                if [0, 0, 255] not in colour_list:
                    bright_blue_colour = black
                if [0, 0, 255] == primary_colour:
                    bright_blue_colour = default_green
                if [0, 0, 255] in colour_list and [0, 0, 255] != primary_colour:
                    bright_blue_colour = red
                if orange in colour_list and orange != primary_colour:
                    orange_colour = red
                if orange == primary_colour:
                    orange_colour = default_green
                if orange not in colour_list:
                    orange_colour = black
                if [255, 255, 255] not in colour_list:
                    white_colour = black
                if [255, 255, 255] == primary_colour:
                    white_colour = default_green
                if [255, 255, 255] in colour_list and [255, 255, 255] != primary_colour:
                    white_colour = red
                if [0, 0, 0] in colour_list and [0, 0, 0] != primary_colour:
                    black_colour = red
                if [0, 0, 0] not in colour_list:
                    black_colour = black
                if [0, 0, 0] == primary_colour:
                    black_colour = default_green
                if [128, 128, 128] == primary_colour:
                    grey_colour = default_green
                if [128, 128, 128] != primary_colour and [128, 128, 128] in colour_list:
                    grey_colour = red
                if [128, 128, 128] not in colour_list:
                    grey_colour = black
                red_text = font1.render('Red', True, red_colour)  # re render
                bright_green_text = font1.render('Bright Green', True, bright_green_colour)  # re render
                pink_text = font1.render('Pink', True, pink_colour)  # re render
                blue_text = font1.render('Blue', True, blue_colour)  # re render
                yellow_text = font1.render('Yellow', True, yellow_colour)  # re render
                purple_text = font1.render('Purple', True, purple_colour)  # re render
                bright_red_text = font1.render('Bright Red', True, bright_red_colour)  # re render
                bright_blue_text = font1.render('Bright Blue', True, bright_blue_colour)  # re render
                orange_text = font1.render('Orange', True, orange_colour)  # re render
                white_text = font1.render('White', True, white_colour)  # re render
                black_text = font1.render('Black', True, black_colour)  # re render
                grey_text = font1.render('Grey', True, grey_colour)  # re render
                default_green_text = font1.render('Green', True, default_green_colour)  # re render

            if secondary_colors:
                screen.blit(toxt2, (180, 240))
                scc = default_green
                if t2ext_rect.collidepoint(mp):
                    pcc = grey
                if not t2ext_rect.collidepoint(mp):
                    pcc = black

                if default_green == secondary_colour:
                    default_green_colour = default_green
                    red_text = font1.render('Red', True, red_colour)  # re render
                    bright_green_text = font1.render('Bright Green', True, bright_green_colour)  # re render
                    pink_text = font1.render('Pink', True, pink_colour)  # re render
                    blue_text = font1.render('Blue', True, blue_colour)  # re render
                    yellow_text = font1.render('Yellow', True, yellow_colour)  # re render
                    purple_text = font1.render('Purple', True, purple_colour)  # re render
                    bright_red_text = font1.render('Bright Red', True, bright_red_colour)  # re render
                    bright_blue_text = font1.render('Bright Blue', True, bright_blue_colour)  # re render
                    orange_text = font1.render('Orange', True, orange_colour)  # re render
                    white_text = font1.render('White', True, white_colour)  # re render
                    black_text = font1.render('Black', True, black_colour)  # re render
                    grey_text = font1.render('Grey', True, grey_colour)  # re render
                    default_green_text = font1.render('Green', True, default_green_colour)  # re render
                if [0, 190, 0] == secondary_colour:
                    default_green_colour = [0, 190, 0]
                if [0, 190, 0] != secondary_colour:
                    default_green_colour = red
                if [200, 0, 0] == secondary_colour:
                    red_colour = default_green
                if [200, 0, 0] != secondary_colour and [200, 0, 0] in colour_list:
                    red_colour = red
                if [200, 0, 0] != secondary_colour and [200, 0, 0] not in colour_list:
                    red_colour = black
                if [255, 120, 203] == secondary_colour:
                    pink_colour = default_green
                if [255, 120, 203] != secondary_colour and [255, 120, 203] in colour_list:
                    pink_colour = red
                if [255, 120, 203] not in colour_list:
                    pink_colour = black
                if [0, 0, 180] == secondary_colour:
                    blue_colour = default_green
                if [0, 0, 180] not in colour_list:
                    blue_colour = black
                if [0, 0, 180] in colour_list and [0, 0, 180] != secondary_colour:
                    blue_colour = red
                if yellow == secondary_colour:
                    yellow_colour = default_green
                if yellow not in colour_list:
                    yellow_colour = black
                if yellow != secondary_colour and yellow in colour_list:
                    yellow_colour = red
                if purple not in colour_list:
                    purple_colour = black
                if purple == secondary_colour:
                    purple_colour = default_green
                if purple != secondary_colour and purple in colour_list:
                    purple_colour = red
                if [255, 0, 0] == secondary_colour:
                    bright_red_colour = default_green
                if [255, 0, 0] in colour_list and [255, 0, 0] != secondary_colour:
                    bright_red_colour = red
                if [255, 0, 0] not in colour_list:
                    bright_red_colour = black
                if [0, 255, 0] not in colour_list:
                    bright_green_colour = black
                if [0, 255, 0] == secondary_colour:
                    bright_green_colour = default_green
                if [0, 255, 0] != secondary_colour and [0, 255, 0] in colour_list:
                    bright_green_colour = red
                if [0, 0, 255] not in colour_list:
                    bright_blue_colour = black
                if [0, 0, 255] == secondary_colour:
                    bright_blue_colour = default_green
                if [0, 0, 255] in colour_list and [0, 0, 255] != secondary_colour:
                    bright_blue_colour = red
                if orange in colour_list and orange != secondary_colour:
                    orange_colour = red
                if orange == secondary_colour:
                    orange_colour = default_green
                if orange not in colour_list:
                    orange_colour = black
                if [255, 255, 255] not in colour_list:
                    white_colour = black
                if [255, 255, 255] == secondary_colour:
                    white_colour = default_green
                if [255, 255, 255] in colour_list and [255, 255, 255] != secondary_colour:
                    white_colour = red
                if [0, 0, 0] in colour_list and [0, 0, 0] != secondary_colour:
                    black_colour = red
                if [0, 0, 0] not in colour_list:
                    black_colour = black
                if [0, 0, 0] == secondary_colour:
                    black_colour = default_green
                if [128, 128, 128] == secondary_colour:
                    grey_colour = default_green
                if [128, 128, 128] != secondary_colour and [128, 128, 128] in colour_list:
                    grey_colour = red
                red_text = font1.render('Red', True, red_colour)  # re render
                bright_green_text = font1.render('Bright Green', True, bright_green_colour)  # re render
                pink_text = font1.render('Pink', True, pink_colour)  # re render
                blue_text = font1.render('Blue', True, blue_colour)  # re render
                yellow_text = font1.render('Yellow', True, yellow_colour)  # re render
                purple_text = font1.render('Purple', True, purple_colour)  # re render
                bright_red_text = font1.render('Bright Red', True, bright_red_colour)  # re render
                bright_blue_text = font1.render('Bright Blue', True, bright_blue_colour)  # re render
                orange_text = font1.render('Orange', True, orange_colour)  # re render
                white_text = font1.render('White', True, white_colour)  # re render
                black_text = font1.render('Black', True, black_colour)  # re render
                grey_text = font1.render('Grey', True, grey_colour)  # re render
                default_green_text = font1.render('Green', True, default_green_colour)  # re render

        if csr.collidepoint(mp) and not customm_skins:
            cstrs = grey
        if not csr.collidepoint(mp) and not customm_skins:
            cstrs = black
        if customm_skins:
            player_rect1.x = 480
            player_rect1.y = 500
            cstrs = default_green

            if 'cn' in custom_skins_list and custom_skin == 'cn':
                cn_colour = default_green
            if 'alien' in custom_skins_list and custom_skin == 'alien':
                alien_colour = default_green
            if 'flower' in custom_skins_list and custom_skin == 'flower':
                flower_colour = default_green
            if 'mars' in custom_skins_list and custom_skin == 'mars':
                mars_colour = default_green
            if 'plane' in custom_skins_list and custom_skin == 'plane':
                plane_colour = default_green
            if 'smurf' in custom_skins_list and custom_skin == 'smurf':
                smurf_colour = default_green
            if custom_skin is None:
                NoneColour = default_green

            if 'cn' in custom_skins_list and not custom_skin == 'cn':
                cn_colour = red
            if 'alien' in custom_skins_list and not custom_skin == 'alien':
                alien_colour = red
            if 'flower' in custom_skins_list and not custom_skin == 'flower':
                flower_colour = red
            if 'mars' in custom_skins_list and not custom_skin == 'mars':
                mars_colour = red
            if 'plane' in custom_skins_list and not custom_skin == 'plane':
                plane_colour = red
            if 'smurf' in custom_skins_list and not custom_skin == 'smurf':
                smurf_colour = red

            if 'cn' not in custom_skins_list:
                cn_colour = black
            if 'alien' not in custom_skins_list:
                alien_colour = black
            if 'flower' not in custom_skins_list:
                flower_colour = black
            if 'mars' not in custom_skins_list:
                mars_colour = black
            if 'plane' not in custom_skins_list:
                plane_colour = black
            if 'smurf' not in custom_skins_list:
                smurf_colour = black
            if custom_skin is not None:
                NoneColour = black

            cn_text = font1.render('Chicken Nugget', True, cn_colour)
            alien_text = font1.render('Alien', True, alien_colour)
            flower_text = font1.render('Flower', true, flower_colour)
            mars_text = font1.render('Mars', true, mars_colour)
            plane_text = font1.render('Plane', true, plane_colour)
            smurf_text = font1.render('Smurf Cat', true, smurf_colour)
            NoneText = font1.render('None', true, NoneColour)

            screen.blit(cn_text, cn_rect)
            screen.blit(alien_text, alien_rect)
            screen.blit(flower_text, flower_rect)
            screen.blit(mars_text, mars_rect)
            screen.blit(plane_text, plane_rect)
            screen.blit(smurf_text, smurf_rect)
            screen.blit(NoneText, NoneRect)

        if dsr.collidepoint(mp) and not desins:
            dstrs = grey
        if not dsr.collidepoint(mp) and not desins:
            dstrs = black
        if desins:
            player_rect1.x = 480
            player_rect1.y = 500
            dstrs = default_green
            screen.blit(tax, tax_r)
            screen.blit(tax1, tax1_r)
            if tax_r.collidepoint(mp) and not design_selection:
                dsc = grey
            if design_selection:
                dsc = default_green
                if 'stripes' in designs_list and design == 'stripes':
                    stripes_colour = default_green
                if 'outline' in designs_list and design == 'outline':
                    outline_colour = default_green
                if 'spotty' in designs_list and design == 'spotty':
                    spotty_colour = default_green
                if 'diamonds' in designs_list and design == 'diamonds':
                    diamond_colour = default_green
                if 'rainbow' in designs_list and design == 'rainbow':
                    rainbow_colour = default_green
                if 'inner circle' in designs_list and design == 'inner circle':
                    ic_colour = default_green
                if design is None:
                    NoneColour = default_green

                if 'stripes' in designs_list and design != 'stripes':
                    stripes_colour = red
                if 'outline' in designs_list and design != 'outline':
                    outline_colour = red
                if 'spotty' in designs_list and design != 'spotty':
                    spotty_colour = red
                if 'diamonds' in designs_list and design != 'diamonds':
                    diamond_colour = red
                if 'rainbow' in designs_list and design != 'rainbow':
                    rainbow_colour = red
                if 'inner circle' in designs_list and design != 'inner circle':
                    ic_colour = red

                if 'stripes' not in designs_list:
                    stripes_colour = black
                if 'outline' not in designs_list:
                    outline_colour = black
                if 'spotty' not in designs_list:
                    spotty_colour = black
                if 'diamonds' not in designs_list:
                    diamond_colour = black
                if 'rainbow' not in designs_list:
                    rainbow_colour = black
                if 'inner circle' not in designs_list:
                    ic_colour = black
                if design is not None:
                    NoneColour = black

                screen.blit(stripes_text, stripes_rect)
                screen.blit(outline_text, outline_rect)
                screen.blit(spotty_text, spotty_rect)
                screen.blit(diamond_text, diamond_rect)
                screen.blit(rainbow_text, rainbow_rect)
                screen.blit(ic_text, ic_rect)
                screen.blit(NoneText, NoneRect)

                stripes_text = font1.render('Stripes', True, stripes_colour)
                outline_text = font1.render('Outline', True, outline_colour)
                spotty_text = font1.render('Spotty', True, spotty_colour)
                diamond_text = font1.render('Diamonds', true, diamond_colour)
                rainbow_text = font1.render('Rainbow', True, rainbow_colour)
                ic_text = font1.render('Inner Circle', true, ic_colour)
                NoneText = font1.render('None', true, NoneColour)
            if design_customisation:
                dcc = default_green
                pygame.draw.rect(screen, grey, slider_rect)
                pygame.draw.rect(screen, white, handle_rect)
                pygame.draw.rect(screen, black, handle_rect, 2)
                pygame.draw.rect(screen, grey, slider_rect1)
                pygame.draw.rect(screen, white, handle_rect1)
                pygame.draw.rect(screen, black, handle_rect1, 2)
                pygame.draw.rect(screen, grey, slider_rect5)
                pygame.draw.rect(screen, white, handle_rect5)
                pygame.draw.rect(screen, black, handle_rect5, 2)
                pygame.draw.rect(screen, grey, slider_rect3)
                pygame.draw.rect(screen, white, handle_rect3)
                pygame.draw.rect(screen, black, handle_rect3, 2)
                taxt = font4.render('Stripes Design:', True, black)
                taxt1 = font4.render('Outline Design:', true, black)
                taxt2 = font4.render('Rainbow Design:', True, black)
                taxt3 = font4.render('Inner Circle:', true, black)
                text3333 = font1.render(f'Stripe Width: {stripe_width}px', True, black)
                text2222 = font1.render(f'Outline Size: {outline_size}px', True, black)
                text5555 = font1.render(f'Length: {radius_length}px', True, black)
                t5555ext = font1.render('Inner Circle Radius', True, black)
                t4444ext = font1.render('Colour Change', True, black)
                if colour_change_interval.is_integer():
                    display_value = f'{int(colour_change_interval)}'
                if not colour_change_interval.is_integer():
                    display_value = f'{colour_change_interval:.2f}'
                if tickk.is_integer():
                    display_value1 = f'{int(tickk)}'
                if not tickk.is_integer():
                    display_value1 = f'{tickk:.2f}'
                text4444 = font1.render(f'Interval: {display_value} Frames', True, black)
                t4xt = font2.render(f'{round(60 / colour_change_interval * game_speed_multiplier, 2)} colour changes/s',
                                    true, black)
                if game_speed_multiplier != last_game_speed_multiplier:
                    # Calculate the current ratio of the interval within the current range
                    current_ratio = (colour_change_interval - min_value3) / (max_value3 - min_value3)
                    # Adjust min and max based on the change in game_speed_multiplier
                    min_value3 *= game_speed_multiplier / last_game_speed_multiplier
                    max_value3 *= game_speed_multiplier / last_game_speed_multiplier
                    # Recalculate the colour_change_interval based on the new range
                    colour_change_interval = current_ratio * (max_value3 - min_value3) + min_value3

                    # Update the handle position based on the new interval value
                    handle_x3 = (colour_change_interval - min_value3) / (
                            max_value3 - min_value3) * slider_range3 + slider_x3
                    handle_rect3.x = handle_x3 - handle_size3 // 2

                    # Update the last multiplier value
                    last_game_speed_multiplier = game_speed_multiplier

                screen.blit(t4xt, (slider_x3, slider_y3 + 30))
                screen.blit(text4444, (slider_x3, slider_y3 - 50))
                screen.blit(t4444ext, (slider_x3, slider_y3 - 80))
                screen.blit(text5555, (slider_x5, slider_y5 - 50))
                screen.blit(t5555ext, (slider_x5, slider_y5 - 80))
                screen.blit(text2222, (slider_x1, slider_y1 - 50))
                screen.blit(text3333, (slider_x, slider_y - 50))
                screen.blit(taxt, (180, 210))
                screen.blit(taxt1, (180, 370))
                screen.blit(taxt3, (550, 190))
            if tax1_r.collidepoint(mp) and not design_customisation:
                dcc = grey
            if not tax1_r.collidepoint(mp) and not design_customisation:
                dcc = black
            if not tax_r.collidepoint(mp) and not design_selection:
                dsc = black
            tax = font1.render('Design Selection', true, dsc)
            tax1 = font1.render('Design Customisation', True, dcc)

        screen.blit(colour, colourr)
        screen.blit(cs, csr)
        screen.blit(ds, dsr)

        red_text = font1.render('Red', True, red_colour)  # re render
        bright_green_text = font1.render('Bright Green', True, bright_green_colour)  # re render
        pink_text = font1.render('Pink', True, pink_colour)  # re render
        blue_text = font1.render('Blue', True, blue_colour)  # re render
        yellow_text = font1.render('Yellow', True, yellow_colour)  # re render
        purple_text = font1.render('Purple', True, purple_colour)  # re render
        bright_red_text = font1.render('Bright Red', True, bright_red_colour)  # re render
        bright_blue_text = font1.render('Bright Blue', True, bright_blue_colour)  # re render
        orange_text = font1.render('Orange', True, orange_colour)  # re render
        white_text = font1.render('White', True, white_colour)  # re render
        black_text = font1.render('Black', True, black_colour)  # re render
        grey_text = font1.render('Grey', True, grey_colour)  # re render
        default_green_text = font1.render('Green', True, default_green_colour)  # re render

        t2ext = font_1.render('Primary Colours', True, pcc)
        t3ext = font_1.render('Secondary Colours', True, scc)

        colour = font4.render('Colours', True, ctcs)
        cs = font4.render('Custom Skins', True, cstrs)
        ds = font4.render('Designs', True, dstrs)

        if design == 'stripes':
            screen.blit(player, player_rect1)
        if design == 'outline':
            screen.blit(player, player_rect1)
            pygame.draw.rect(screen, secondary_colour, player_rect1, outline_size)
        if design == 'spotty':
            draw_spots(player)
            screen.blit(player, player_rect1)
        if design == 'inner circle':
            screen.blit(player, player_rect1)
            draw_circle(radius_length, (player_rect1.x + 20, player_rect1.y + 20))
        if design == 'diamonds':
            draw_diamonds(player)
            screen.blit(player, player_rect1)
        if design == 'rainbow':
            frame_count += 1
            if frame_count >= colour_change_interval:
                frame_count = 0  # Reset frame counter
                player_colour = next(color_cycle)  # Get the next color in the cycle
            player.fill(player_colour)
            screen.blit(player, player_rect1)
        if design is None and custom_skin is None:
            player.fill(primary_colour)
            screen.blit(player, player_rect1)
        if custom_skin == 'cn':
            player_rect1.y = 500
            player_rect1.x = 480
            screen.blit(cn, player_rect1)
        if custom_skin == 'alien':
            player_rect1.y = 500
            player_rect1.x = 480
            screen.blit(alien, player_rect1)
        if custom_skin == 'flower':
            player_rect1.y = 490
            player_rect1.x = 480
            screen.blit(flower, player_rect1)
        if custom_skin == 'mars':
            player_rect1.y = 500
            player_rect1.x = 480
            screen.blit(mars, player_rect1)
        if custom_skin == 'plane':
            player_rect1.y = 500
            player_rect1.x = 430
            screen.blit(plane, player_rect1)
        if custom_skin == 'smurf':
            player_rect1.y = 500
            player_rect1.x = 480
            screen.blit(smurf, player_rect1)

        if primary_colour == white or primary_colour == [255, 255, 255]:
            if design == 'spotty' or design == 'inner circle' or design == 'diamonds':
                pygame.draw.rect(screen, black, player_rect1, 1)
        if (secondary_colour == white or secondary_colour == [255, 255, 255] or primary_colour == [255, 255, 255] or
                primary_colour == white):
            if design == 'stripes':
                pygame.draw.rect(screen, black, player_rect1, 1)
        if secondary_colour == white or secondary_colour == [255, 255, 255]:
            if design == 'outline':
                pygame.draw.rect(screen, black, player_rect1, 1)
        my_instance.draw()

        pygame.display.flip()
        clock.tick(tickk)

    if clrs:
        game_started = False
        screen.fill((50, 100, 180))
        ctc = default_green
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        screen.blit(shop_text, shop_trect)
        mp = pygame.mouse.get_pos()
        if cs_r.collidepoint(mp):
            cstr = grey
        elif not cs_r.collidepoint(mp):
            cstr = black
        if ds_r.collidepoint(mp):
            dstr = grey
        elif not ds_r.collidepoint(mp):
            dstr = black
        colour = font4.render('Colours', True, ctc)
        cs = font4.render('Custom Skins', True, cstr)
        ds = font4.render('Designs', True, dstr)
        screen.blit(cs, cs_r)
        screen.blit(colour, colour_r)
        screen.blit(ds, ds_r)
        owned = font2.render('Owned', True, black)
        pygame.draw.rect(screen, white, item_rect)
        pygame.draw.rect(screen, white, item_rect1)
        pygame.draw.rect(screen, white, item_rect2)
        pygame.draw.rect(screen, white, item_rect3)
        pygame.draw.rect(screen, white, item_rect4)
        pygame.draw.rect(screen, white, item_rect5)
        pygame.draw.rect(screen, white, item_rect6)
        pygame.draw.rect(screen, white, item_rect7)
        pygame.draw.rect(screen, white, item_rect8)
        pygame.draw.rect(screen, white, item_rect9)
        pygame.draw.rect(screen, white, item_rect10)
        pygame.draw.rect(screen, white, item_rect11)
        pygame.draw.rect(screen, white, item_rect12)

        pygame.draw.rect(screen, black, item_rect, 3)
        pygame.draw.rect(screen, black, item_rect1, 3)
        pygame.draw.rect(screen, black, item_rect2, 3)
        pygame.draw.rect(screen, black, item_rect3, 3)
        pygame.draw.rect(screen, black, item_rect4, 3)
        pygame.draw.rect(screen, black, item_rect5, 3)
        pygame.draw.rect(screen, black, item_rect6, 3)
        pygame.draw.rect(screen, black, item_rect7, 3)
        pygame.draw.rect(screen, black, item_rect8, 3)
        pygame.draw.rect(screen, black, item_rect9, 3)
        pygame.draw.rect(screen, black, item_rect10, 3)
        pygame.draw.rect(screen, black, item_rect11, 3)
        pygame.draw.rect(screen, black, item_rect12, 3)

        font8 = pygame.font.SysFont('Trebuchet MS', 17)
        text2 = font2.render('Green', True, black)
        text3 = font2.render('Red', True, black)
        text4 = font2.render('Pink', True, black)
        text5 = font2.render('Blue', True, black)
        text6 = font2.render('Yellow', True, black)
        text7 = font2.render('Purple', True, black)
        text8 = font2.render('Bright Red', True, black)
        text9 = font8.render('Bright Green', True, black)
        text10 = font8.render('Bright Blue', True, black)
        text11 = font2.render('Orange', True, black)
        text12 = font2.render('White', True, black)
        text13 = font2.render('Black', True, black)
        text14 = font2.render('Grey', True, black)

        pygame.draw.rect(screen, default_green, rect1)  # i bookmarked here
        pygame.draw.rect(screen, red,
                         rect2)  # make it change to extras state when pressed (revive heart icon for when die on riveeve)
        pygame.draw.rect(screen, pink, rect3)
        pygame.draw.rect(screen, blue, rect4)
        pygame.draw.rect(screen, yellow, rect5)
        pygame.draw.rect(screen, purple, rect6)
        pygame.draw.rect(screen, bright_red, rect7)
        pygame.draw.rect(screen, bright_green, rect8)
        pygame.draw.rect(screen, bright_blue, rect9)
        pygame.draw.rect(screen, orange, rect10)
        pygame.draw.rect(screen, white, rect11)
        pygame.draw.rect(screen, black, rect12)
        pygame.draw.rect(screen, grey, rect13)

        pygame.draw.rect(screen, black, rect11, 2)

        screen.blit(text2, (185, 137))
        screen.blit(text3, (310, 137))
        screen.blit(text4, (425, 137))
        screen.blit(text5, (538, 137))
        screen.blit(text6, (645, 137))
        screen.blit(text7, (760, 137))
        screen.blit(text8, (166, 302))
        screen.blit(text9, (278.97, 308))
        screen.blit(text10, (400, 308))
        screen.blit(text11, (525, 302))
        screen.blit(text12, (645, 302))
        screen.blit(text13, (763.844, 302))
        screen.blit(text14, (190, 467))

        screen.blit(owned, (181, 160))
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))

        if red in colour_list or 'red' in colour_list:
            screen.blit(owned, (296, 160))
        if pink in colour_list or 'pink' in colour_list:
            screen.blit(owned, (411, 160))
        if blue in colour_list or 'blue' in colour_list:
            screen.blit(owned, (526, 160))
        if yellow in colour_list:
            screen.blit(owned, (641, 160))
        if purple in colour_list:
            screen.blit(owned, (756, 160))
        if bright_red in colour_list or 'bright red' in colour_list:
            screen.blit(owned, (181, 325))
        if bright_green in colour_list or 'bright green' in colour_list:
            screen.blit(owned, (296, 325))
        if bright_blue in colour_list or 'bright blue' in colour_list:
            screen.blit(owned, (411, 325))
        if orange in colour_list:
            screen.blit(owned, (526, 325))
        if white in colour_list or 'white' in colour_list:
            screen.blit(owned, (641, 325))
        if black in colour_list or 'black' in colour_list:
            screen.blit(owned, (756, 325))
        if grey in colour_list or 'grey' in colour_list:
            screen.blit(owned, (181, 490))

        if red not in colour_list and 'red' not in colour_list:
            price_text = font2.render(str(red_price), True, black)
            screen.blit(coin_s, (306, 165))
            screen.blit(price_text, (330, 163))
        if pink not in colour_list and 'pink' not in colour_list:
            price_text1 = font2.render(str(pink_price), True, black)
            screen.blit(coin_s, (421, 165))
            screen.blit(price_text1, (445, 163))
        if blue not in colour_list and 'blue' not in colour_list:
            price_text2 = font2.render(str(blue_price), True, black)
            screen.blit(coin_s, (536, 165))
            screen.blit(price_text2, (560, 163))
        if yellow not in colour_list:
            price_text3 = font2.render(str(yellow_price), True, black)
            screen.blit(coin_s, (651, 165))
            screen.blit(price_text3, (675, 163))
        if purple not in colour_list:
            price_text4 = font2.render(str(purple_price), True, black)
            screen.blit(coin_s, (766, 165))
            screen.blit(price_text4, (790, 163))
        if bright_red not in colour_list and 'bright red' not in colour_list:
            price_text5 = font2.render(str(bright_red_price), True, black)
            screen.blit(coin_s, (191, 332))
            screen.blit(price_text5, (213, 330))
        if bright_green not in colour_list and 'bright green' not in colour_list:
            price_text6 = font2.render(str(bright_green_price), True, black)
            screen.blit(coin_s, (306, 332))
            screen.blit(price_text6, (330, 330))
        if bright_blue not in colour_list and 'bright blue' not in colour_list:
            price_text7 = font2.render(str(bright_blue_price), True, black)
            screen.blit(coin_s, (421, 332))
            screen.blit(price_text7, (442, 330))
        if orange not in colour_list:
            price_text8 = font2.render(str(orange_price), True, black)
            screen.blit(coin_s, (536, 332))
            screen.blit(price_text8, (560, 330))
        if white not in colour_list and 'white' not in colour_list:
            price_text9 = font2.render(str(white_price), True, black)
            screen.blit(coin_s, (651, 332))
            screen.blit(price_text9, (672, 330))
        if black not in colour_list and 'black' not in colour_list:
            price_text10 = font2.render(str(black_price), True, black)
            screen.blit(coin_s, (766, 332))
            screen.blit(price_text10, (787, 330))
        if grey not in colour_list and 'grey' not in colour_list:
            price_text11 = font2.render(str(grey_price), True, black)
            screen.blit(coin_s, (191, 499))
            screen.blit(price_text11, (213, 497))

        if pk1:
            current_tcks = -1 * (tcks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            screen.blit(txxt, rrect)
            if truncate(current_tcks / 1000) >= 2:
                pk1 = False

        if pkk:
            current_t1cks = -1 * (t1cks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            txx1t = font1.render('Select secondary colour!', True, black)
            screen.blit(txx1t, (335, 455))
            if truncate(current_t1cks / 1000) >= 2:
                pkk = False
        if ExtrasRec.collidepoint(mp):
            ExtrasCol = (150, 150, 150)
        if not ExtrasRec.collidepoint(mp):
            ExtrasCol = black
        ExtrasTex = font4.render('Extras', True, ExtrasCol)

        if back_rect1.collidepoint(mp):
            screen.blit(ba_h, back_rect1)
        if not back_rect1.collidepoint(mp):
            screen.blit(back_arrow, back_rect1)
        balance_text = font4.render(str(balance), True, black)
        screen.blit(ExtrasTex, ExtrasRec)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if cstm_skins:
        game_started = False
        screen.fill((50, 100, 180))
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))
        cstr = default_green
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        screen.blit(line3, (380, 87))
        screen.blit(line3, (614, 87))
        screen.blit(line4, (150, 322))
        shop_text = font1.render('Shop', True, 'Black')
        screen.blit(shop_text, shop_trect)
        mp = pygame.mouse.get_pos()
        if colour_r.collidepoint(mp):
            ctc = grey
        elif not colour_r.collidepoint(mp):
            ctc = black
        if ds_r.collidepoint(mp):
            dstr = grey
        elif not ds_r.collidepoint(mp):
            dstr = black
        colour = font4.render('Colours', True, ctc)
        cs = font4.render('Custom Skins', True, cstr)
        ds = font4.render('Designs', True, dstr)
        screen.blit(cs, cs_r)
        screen.blit(colour, colour_r)
        screen.blit(ds, ds_r)
        if back_rect1.collidepoint(mp):
            screen.blit(ba_h, back_rect1)
        if not back_rect1.collidepoint(mp):
            screen.blit(back_arrow, back_rect1)
        balance_text = font4.render(str(balance), True, black)
        if ExtrasRec.collidepoint(mp):
            ExtrasCol = (150, 150, 150)
        if not ExtrasRec.collidepoint(mp):
            ExtrasCol = black
        ExtrasTex = font4.render('Extras', True, ExtrasCol)
        if rect14.collidepoint(mp):
            pygame.draw.rect(screen, black, rect14, 2)
        if rect15.collidepoint(mp):
            pygame.draw.rect(screen, black, rect15, 2)
        if rect16.collidepoint(mp):
            pygame.draw.rect(screen, black, rect16, 2)
        if rect17.collidepoint(mp):
            pygame.draw.rect(screen, black, rect17, 2)
        if rect18.collidepoint(mp):
            pygame.draw.rect(screen, black, rect18, 2)
        if rect19.collidepoint(mp):
            pygame.draw.rect(screen, black, rect19, 2)

        tgxt = font1.render('Chicken Nugget', True, black)
        tgxt1 = font1.render('Alien', True, black)
        tgxt2 = font1.render('Flower', True, black)
        tgxt3 = font1.render('Mars', True, black)
        tgxt4 = font1.render('Plane', true, black)
        tgxt5 = font1.render('Smurf Cat', true, black)
        sts = font2.render('scaled to size*', true, black)

        price = font4.render(str(nugget_price), true, black)
        price1 = font4.render(str(alien_price), true, black)
        price2 = font4.render(str(flower_price), True, black)
        price3 = font4.render(str(mars_price), true, black)
        price4 = font4.render(str(plane_price), True, black)
        price5 = font4.render(str(smurf_price), True, black)

        ownd = font4.render('Owned', True, black)

        screen.blit(tgxt, (165, 90))
        screen.blit(tgxt1, (470, 90))
        screen.blit(tgxt2, (690, 90))
        screen.blit(tgxt3, (240, 330))
        screen.blit(tgxt4, (470, 330))
        screen.blit(tgxt5, (670, 330))

        screen.blit(sts, (10, 10))
        screen.blit(cn, (245, 160))
        screen.blit(alien, (475, 170))
        screen.blit(flower, (720, 150))
        screen.blit(mars, (250, 400))
        screen.blit(plane, (425, 410))
        screen.blit(smurf, (720, 400))

        if 'cn' not in custom_skins_list:
            screen.blit(coin, (230, 260))
            screen.blit(price, (275, 257))
        if 'cn' in custom_skins_list:
            screen.blit(ownd, (210, 250))
        if 'alien' not in custom_skins_list:
            screen.blit(coin, (460, 260))
            screen.blit(price1, (505, 257))
        if 'alien' in custom_skins_list:
            screen.blit(ownd, (441, 250))
        if 'flower' not in custom_skins_list:
            screen.blit(coin, (690, 260))
            screen.blit(price2, (735, 257))
        if 'flower' in custom_skins_list:
            screen.blit(ownd, (672, 250))
        if 'mars' not in custom_skins_list:
            screen.blit(coin, (225, 490))
            screen.blit(price3, (270, 487))
        if 'mars' in custom_skins_list:
            screen.blit(ownd, (205, 480))
        if 'plane' not in custom_skins_list:
            screen.blit(coin, (460, 490))
            screen.blit(price4, (505, 487))
        if 'plane' in custom_skins_list:
            screen.blit(ownd, (441, 480))
        if 'smurf' not in custom_skins_list:
            screen.blit(coin, (690, 490))
            screen.blit(price5, (735, 487))
        if 'smurf' in custom_skins_list:
            screen.blit(ownd, (672, 480))

        if pkk:
            current_t1cks = -1 * (t1cks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            txx1t = font1.render('Select secondary colour!', True, black)
            screen.blit(txx1t, (335, 455))
            if truncate(current_t1cks / 1000) >= 2:
                pkk = False

        if pk1:
            current_tcks = -1 * (tcks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            screen.blit(txxt, rrect)
            if truncate(current_tcks / 1000) >= 2:
                pk1 = False
        screen.blit(ExtrasTex, ExtrasRec)
        my_instance.draw()

        pygame.display.flip()
        clock.tick(600)

    if dsgns:
        game_started = False
        screen.fill((50, 100, 180))
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))
        dstr = default_green
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        shop_text = font1.render('Shop', True, 'Black')
        screen.blit(shop_text, shop_trect)
        mp = pygame.mouse.get_pos()
        if ExtrasRec.collidepoint(mp):
            ExtrasCol = grey
        if not ExtrasRec.collidepoint(mp):
            ExtrasCol = black
        if colour_r.collidepoint(mp):
            ctc = grey
        elif not colour_r.collidepoint(mp):
            ctc = black
        if cs_r.collidepoint(mp):
            cstr = grey
        elif not cs_r.collidepoint(mp):
            cstr = black
        colour = font4.render('Colours', True, ctc)
        cs = font4.render('Custom Skins', True, cstr)
        ds = font4.render('Designs', True, dstr)
        screen.blit(cs, cs_r)
        screen.blit(colour, colour_r)
        screen.blit(ds, ds_r)
        if back_rect1.collidepoint(mp):
            screen.blit(ba_h, back_rect1)
        if not back_rect1.collidepoint(mp):
            screen.blit(back_arrow, back_rect1)
        balance_text = font4.render(str(balance), True, black)

        screen.blit(line3, (380, 87))
        screen.blit(line3, (614, 87))
        screen.blit(line4, (150, 322))

        tixt1 = font1.render('Stripes', true, black)
        tixt2 = font1.render('Outline', True, black)
        tixt3 = font1.render('Colour Changing', True, black)
        t3xt = font1.render('Rainbow Block', True, black)
        tixt4 = font1.render('Diamonds', true, black)
        tixt5 = font1.render('Spotty', True, black)
        tixt6 = font1.render('Inner Circle', True, black)
        screen.blit(tixt1, (220, 100))
        screen.blit(tixt2, (450, 100))
        screen.blit(tixt5, (690, 100))
        screen.blit(tixt4, (435, 335))
        screen.blit(tixt3, (625, 325))
        screen.blit(t3xt, (635, 355))
        screen.blit(tixt6, (195, 335))

        surfaa = pygame.Surface((40, 40))
        surfa1 = pygame.Surface((40, 40))
        surfa2 = pygame.Surface((40, 40))
        surfa3 = pygame.Surface((40, 40))
        surfaa.fill(primary_colour)
        surfa1.fill(primary_colour)
        surfa3.fill(primary_colour)
        s_rect = surfaa.get_rect(topleft=(480, 180))
        s_rect1 = surfaa.get_rect(topleft=(710, 180))
        s_rect2 = surfaa.get_rect(topleft=(247.5, 420))
        s_rect3 = surfaa.get_rect(topleft=(480, 420))
        s_rect4 = surfaa.get_rect(topleft=(710, 420))
        draw_stripes(surfa3, secondary_colour)
        screen.blit(surfa3, (247.5, 180))
        frame_count += 1
        if frame_count >= colour_change_interval:
            frame_count = 0  # Reset frame counter
            player_colour = next(color_cycle)  # Get the next color in the cycle
        surfa2.fill(player_colour)
        screen.blit(surfaa, s_rect)
        pygame.draw.rect(screen, secondary_colour, s_rect, outline_size)
        draw_spots(surfaa)
        screen.blit(surfaa, s_rect1)
        screen.blit(surfa1, s_rect2)
        screen.blit(surfa2, s_rect4)
        draw_circle(radius_length, (s_rect2.x + 20, s_rect2.y + 20))
        draw_diamonds(surfa1)
        screen.blit(surfa1, s_rect3)
        if primary_colour == white or secondary_colour == white:
            pygame.draw.rect(screen, black, (247.5, 180, 40, 40), 1)
            pygame.draw.rect(screen, black, s_rect, 1)
        if primary_colour == white:
            pygame.draw.rect(screen, black, s_rect1, 1)
            pygame.draw.rect(screen, black, s_rect2, 1)

        ownd = font4.render('Owned', true, black)
        screen.blit(ExtrasTex, ExtrasRec)
        if ExtrasRec.collidepoint(mp):
            ExtrasCol = (150, 150, 150)
        if not ExtrasRec.collidepoint(mp):
            ExtrasCol = black
        ExtrasTex = font4.render('Extras', True, ExtrasCol)

        text_price = font4.render(str(stripes_price), true, black)
        text_price1 = font4.render(str(outline_price), true, black)
        text_price2 = font4.render(str(spotty_price), True, black)
        text_price3 = font4.render(str(diamonds_price), True, black)
        text_price4 = font4.render(str(rainbow_price), true, black)
        text_price5 = font4.render(str(ic_price), true, black)

        if rect14.collidepoint(mp):
            pygame.draw.rect(screen, black, rect14, 2)
        if rect15.collidepoint(mp):
            pygame.draw.rect(screen, black, rect15, 2)
        if rect16.collidepoint(mp):
            pygame.draw.rect(screen, black, rect16, 2)
        if rect17.collidepoint(mp):
            pygame.draw.rect(screen, black, rect17, 2)
        if rect18.collidepoint(mp):
            pygame.draw.rect(screen, black, rect18, 2)
        if rect19.collidepoint(mp):
            pygame.draw.rect(screen, black, rect19, 2)

        if 'stripes' not in designs_list:
            screen.blit(coin, (230, 260))
            screen.blit(text_price, (275, 257))
        if 'stripes' in designs_list:
            screen.blit(ownd, (210, 250))
        if 'outline' not in designs_list:
            screen.blit(coin, (460, 260))
            screen.blit(text_price1, (505, 257))
        if 'outline' in designs_list:
            screen.blit(ownd, (441, 250))
        if 'spotty' not in designs_list:
            screen.blit(coin, (690, 260))
            screen.blit(text_price2, (735, 257))
        if 'spotty' in designs_list:
            screen.blit(ownd, (672, 250))
        if 'inner circle' not in designs_list:
            screen.blit(coin, (225, 490))
            screen.blit(text_price5, (270, 487))
        if 'inner circle' in designs_list:
            screen.blit(ownd, (205, 480))
        if 'diamonds' not in designs_list:
            screen.blit(coin, (460, 490))
            screen.blit(text_price3, (505, 487))
        if 'diamonds' in designs_list:
            screen.blit(ownd, (441, 480))
        if 'rainbow' not in designs_list:
            screen.blit(coin, (690, 490))
            screen.blit(text_price4, (735, 487))
        if 'rainbow' in designs_list:
            screen.blit(ownd, (672, 480))

        if pk1:
            current_tcks = -1 * (tcks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            screen.blit(txxt, rrect)
            if truncate(current_tcks / 1000) >= 2:
                pk1 = False

        pygame.display.flip()
        screen.blit(ExtrasTex, ExtrasRec)
        my_instance.draw()
        clock.tick(tickk)

    if extras:
        screen.fill((50, 100, 180))
        pygame.draw.rect(screen, white, box_rect)
        pygame.draw.rect(screen, white, box1_rect)
        pygame.draw.rect(screen, black, box_rect, 3)
        pygame.draw.rect(screen, black, box1_rect, 3)
        screen.blit(ms_text, ms_rect)
        screen.blit(extrasTex, extrasRec)
        misc_rect = misc_text.get_rect(topleft=(180, 40))
        acc_topright = (
            ((500 - misc_rect.topright[0]) * 2) + misc_rect.width + misc_rect.topright[0], misc_rect.y)  # amazing math
        acc_rect = acc_text.get_rect(topright=acc_topright)  # make it hover, change colour pressable etc

        if misc_rect.collidepoint(mp) and not misc:
            mtc = grey
        if not misc_rect.collidepoint(mp) and not misc:
            mtc = black
        if misc:
            mtc = default_green

        if acc_rect.collidepoint(mp) and misc:
            atc = grey
        if not acc_rect.collidepoint(mp) and misc:
            atc = black
        if accessories:
            atc = default_green

        misc_text = font4.render('Miscellaneous', True, mtc)
        acc_text = font4.render('Accessories', True, atc)

        screen.blit(acc_text, acc_rect)
        screen.blit(misc_text, misc_rect)
        ms_text = font1.render('Main Shop', True, ms_colour)
        if ms_rect.collidepoint(mp):
            ms_colour = grey
        if not ms_rect.collidepoint(mp):
            ms_colour = black
        if pk1:
            current_tcks = -1 * (tcks - pygame.time.get_ticks())
            pygame.draw.rect(screen, color, rrrect)
            screen.blit(txxt, rrect)
            if truncate(current_tcks / 1000) >= 2:
                pk1 = False
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if information:
        game_started = False
        screen.fill((50, 100, 180))
        font6 = pygame.font.SysFont('Trebuchet MS', 26)
        font7 = pygame.font.SysFont('Trebuchet MS', 35)
        it = font7.render('How to play?', True, 'Green')
        it1 = font6.render(f'Pressing {jump_string} allows you to jump and you must avoid all objects in order to',
                           True, (0, 0, 0))
        it2 = font6.render("survive. Try and see what score you can get!", True, (0, 0, 0))
        st = font7.render('What are stages?', True, 'Green')
        st1 = font6.render('Stages are difficulty levels. The higher the stage, the higher the difficulty.', True,
                           'Black')
        stg1 = font6.render('Stage 1: Spawns triangles at a steady enemy spawn rate.', True, 'Black')
        stg2 = font6.render('Stage 2: Now spawns circles and has a increased enemy spawn rate.', True, 'Black')
        stg3 = font6.render('Stage 3: Now spawns squares and has a faster enemy spawn rate.', True, 'Black')
        stg4 = font6.render('Stage 4: Waves can now occur and faster enemy spawn rates.', True, 'Black')
        wa = font7.render('What are waves?', True, 'Green')
        wat = font6.render('In a wave, 2 black rectangles will be coming towards you, but before they do,', True,
                           'Black')
        wat1 = font6.render('one will turn green and that rectangle is safe to pass.', True, 'Black')
        screen.blit(it, (20, 10))
        screen.blit(it1, (20, 50))
        screen.blit(it2, (20, 80))
        screen.blit(st, (20, 110))
        screen.blit(st1, (20, 155))
        screen.blit(stg1, (20, 190))
        screen.blit(stg2, (20, 225))
        screen.blit(stg3, (20, 260))
        screen.blit(stg4, (20, 295))
        screen.blit(wa, (20, 325))
        screen.blit(wat, (20, 365))
        screen.blit(wat1, (20, 400))
        back = font1.render('Go Back', True, 'Black')
        screen.blit(back, (26, 450))
        mp = pygame.mouse.get_pos()
        if back_rect.collidepoint(mp):
            screen.blit(ba_h, back_rect)
        else:
            screen.blit(back_arrow, back_rect)
        my_instance.draw()
        pygame.display.flip()
        clock.tick(600)

    if game_started:
        game_settings = False
        character_customisation = False
        clrs = False
        dsgns = False
        cstm_skins = False
        information = False
        balance_text = font4.render(str(balance), True, black)
        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn_time > enemy_spawn_delay and enemy_allow_spawn:
            enemies_t.append(Enemy_triangle())
            if stage2 or stage3 or stage4:
                enemies_c.append(Enemy_circle())  # Add circle enemy
            if stage3 or stage4:
                enemies_s.append(Enemy_square())
            last_enemy_spawn_time = current_time

        if not inverted_gravity:
            velocity_y += gravity
        elif inverted_gravity:
            velocity_y -= gravity

        y += velocity_y
        player_rect.y += velocity_y

        screen.fill((50, 100, 180))
        timing_list1 = timing_list1
        if ticks_pk:
            elapsed_time1 = round((pygame.time.get_ticks() - ticks) / 1000 * game_speed_multiplier, 1)
            text1 = font1.render('Time elapsed:', True, 'Black')
            e_t = str(elapsed_time1) + 's'
            e_t_text = font1.render(e_t, True, 'Black')
            if elapsed_time1 == 1:
                spawn_powerup = True
            if elapsed_time1 == 7:
                spawn_coin = True
            if elapsed_time1 < 10:
                stage1 = True
            if 10 <= elapsed_time1 < 30:
                stage1 = False
                stage2 = True
            if 30 <= elapsed_time1 < 50:
                stage2 = False
                stage3 = True
            if 50 <= elapsed_time1:
                stage3 = False
                stage4 = True
            if elapsed_time1 == 10:
                spawn_shields = True
            if elapsed_time1 == 19:
                enact_ig = True
            if elapsed_time1 == lester and spawn_shields:
                shields_sl.append(SpawnShield())
                spawn_shields = False

        if spawn_shields:
            for item in shields_sl:
                if item not in processed_objects1:
                    randomise_chosen_time = True
                    processed_objects1.add(item)
            if randomise_chosen_time:
                ChosenTime = random.choice(timing_list1) + 20
                cet1 = elapsed_time1
                times_iterated += 1
                randomise_chosen_time = False
            if round(elapsed_time1 - cet1, 1) >= ChosenTime:
                shields_sl.append(SpawnShield())

        if spawn_coin:
            for item in exc_sl:
                if item not in process_object1:
                    random_c = True
                    process_object1.add(item)
            if random_c:
                ChooseT = 25
                cet7 = elapsed_time1
                random_c = False

            if round(elapsed_time1 - cet7, 1) >= ChooseT:
                exc_sl.append(ExtraCoin())

        if enact_ig:
            for item in ig_l:
                if item not in pro_obj1:
                    rand_c = True
                    pro_obj1.add(item)

            if rand_c:
                CTime = random.choice(timing_list2)
                cet5 = elapsed_time1
                rand_c = False

            if round(elapsed_time1 - cet5, 1) >= CTime:
                ig_l.append('InGr')

            if CTime - 5 < round(elapsed_time1 - cet5, 1) < CTime:
                skext = font1.render('Inverted Gravity is approaching!', True, black)
                skext_rect = skext.get_rect(center=(500, 300))
                screen.blit(skext, skext_rect)

        if spawn_powerup:
            for item in clouds_sl:
                if item not in processed_obj1:
                    randomise_c = True
                    processed_obj1.add(item)
            if randomise_c:
                ChooseTime = random.choice(timing_list2) + 15
                cet3 = elapsed_time1
                times_i += 1
                randomise_c = False
            if round(elapsed_time1 - cet3, 1) >= ChooseTime:
                clouds_sl.append(SpawnCloud())
        if custom_skin is None:
            screen.blit(player, player_rect)
        if enemy_allow_spawn:
            for enemy_t in enemies_t:
                enemy_t.move()
                enemy_t.draw()
                if player_rect.colliderect(enemy_t.get_rect()):
                    if not revive():
                        player_rect.bottom = 600
                        velocity_y = 0
                        ticks_pk = False
                        game_started = False
                        end_screen = True
                        score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
                        a_score = int(truncate(score))
                        save_score(a_score)  # Save the current score

            for enemy_c in enemies_c:
                if stage2 or stage3 or stage4:
                    enemy_c.move()
                    enemy_c.draw()
                    if player_rect.colliderect(enemy_c.get_rect()):
                        player_rect.bottom = 600
                        velocity_y = 0
                        ticks_pk = False
                        game_started = False
                        end_screen = True
                        score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
                        a_score = int(truncate(score))
                        save_score(a_score)  # Save the current score

            for square in enemies_s:
                square.draw()
                square.move()
                if player_rect.colliderect(square.get_rect()):
                    player_rect.bottom = 600
                    velocity_y = 0
                    ticks_pk = False
                    game_started = False
                    end_screen = True
                    score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
                    a_score = int(truncate(score))
                    save_score(a_score)  # Save the current score

        for objec in clouds_sl:
            objec.draw()
            objec.move()
            if objec.get_rect().colliderect(player_rect):
                clouds_l.append(HasCloud())
                clouds_sl.remove(objec)

        for shield_obj in shields_sl:
            shield_obj.draw()
            shield_obj.move()
            if shield_obj.get_rect().colliderect(player_rect):
                shields_l.append(HasShield())
                shields_sl.remove(shield_obj)

        for item in exc_sl:
            if not item.get_rect().colliderect(player_rect):
                spawn_coin = False
            item.draw()
            item.move()
            if item.get_rect().colliderect(player_rect):
                spawn_coin = True
                balance += item.coin_amount
                pygame.mixer.music.load(
                    'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                pygame.mixer.music.play()
                exc_sl.remove(item)
            if item.x <= -10:
                spawn_coin = True

        for item in ig_l:
            tbxt = font4.render(f'{round(10 - (elapsed_time1 - cet4), 1)}', True, black)
            tbxt1 = font4.render('inverted gravity !11!1!', true, black)
            tbxt_rect = tbxt.get_rect(center=(500, 250))
            tbxt1_rect = tbxt1.get_rect(center=(500, 300))
            screen.blit(tbxt, tbxt_rect)
            screen.blit(tbxt1, tbxt1_rect)
            if item not in pro_obj:
                cet4 = elapsed_time1
                pro_obj.add(item)
            if 10 - (elapsed_time1 - cet4) <= 0:
                enact_ig = True
                ig_l.remove(item)
                inverted_gravity = False
            if 0 < 10 - (elapsed_time1 - cet4):
                enact_ig = False
                inverted_gravity = True

        for objec in clouds_l:
            txti = font4.render(f'{round(objec.time_limit - (elapsed_time1 - cet2), 1)}s', true, black)
            txto = font4.render('0s', true, black)
            txti_rect = txti.get_rect(center=(500, 350))
            txto_rect = txto.get_rect(center=(500, 350))
            if round(objec.time_limit - (elapsed_time1 - cet2), 1) >= 0:
                screen.blit(txti, txti_rect)
            if round(objec.time_limit - (elapsed_time1 - cet2), 1) < 0:
                screen.blit(txto, txto_rect)
            if objec not in processed_obj:
                cet2 = elapsed_time1
                processed_obj.add(objec)
            if not elapsed_time1 - cet2 >= objec.time_limit:
                spawn_powerup = False
            if elapsed_time1 - cet2 >= objec.time_limit:
                spawn_powerup = True
                lower_alpha = False
                if alpha_value == 255:
                    clouds_l.remove(objec)
            if lower_alpha:
                alpha_value = max(0, alpha_value - 2)
            if not lower_alpha:
                alpha_value = min(255, alpha_value + 2)
            if alpha_value == 255:
                lower_alpha = True
            if alpha_value == 0:
                lower_alpha = False

        for shield_obj in shields_l:
            if shield_obj not in processed_objects:
                cet = elapsed_time1
                processed_objects.add(shield_obj)
            if shield_obj.lives == 0 or elapsed_time1 - cet >= shield_obj.time_limit:
                spawn_shields = True
                shields_l.remove(shield_obj)
            if shield_obj.lives != 0 and elapsed_time1 - cet < shield_obj.time_limit:
                spawn_shields = False
                txt_surf = font1.render(f'{shield_obj.lives}', True, black)
                txtt_surf = font1.render(f'{round(shield_obj.time_limit - (elapsed_time1 - cet), 1)}', true, black)
                txtt_srect = txtt_surf.get_rect(center=(player_rect.x + 55, player_rect.y + 70))
                txt_srect = txt_surf.get_rect(center=(player_rect.x + 55, player_rect.y - 30))
                screen.blit(txt_surf, txt_srect)
                screen.blit(txtt_surf, txtt_srect)
                shield_obj.draw()
                shield_obj.update()
                the_rect = shield_obj.get_rect()
                for triangle in enemies_t:
                    if the_rect.colliderect(triangle.get_rect()):
                        enemies_t.remove(triangle)
                        shield_obj.lives -= 1
                        shield_obj.draw()
                        shield_obj.update()

                for circle in enemies_c:
                    if the_rect.colliderect(circle.get_rect()):
                        enemies_c.remove(circle)
                        shield_obj.lives -= 1
                        shield_obj.width = shield_obj.lives * 10
                        shield_obj.y = (player_rect.y - 10) + (-.5 * shield_obj.width + 30)
                        shield_obj.draw()
                        shield_obj.update()

                for square in enemies_s:
                    if the_rect.colliderect(square.get_rect()):
                        enemies_s.remove(square)
                        shield_obj.lives -= 1
                        shield_obj.width = shield_obj.lives * 10
                        shield_obj.y = (player_rect.y - 10) + (-.5 * shield_obj.width + 30)
                        shield_obj.draw()
                        shield_obj.update()

        if stage1:
            stage1_t = font4.render('Stage 1', True, 'Red')
            screen.blit(stage1_t, (435, 100))
        if stage2 and esd_key:
            enemy_spawn_delay -= 250
            esd_key = False
        if stage2:
            stage2_t = font4.render('Stage 2', True, 'Red')
            screen.blit(stage2_t, (435, 100))
        if stage3 and esd_key1:
            enemy_spawn_delay -= 80
            pygame.mixer.music.load(
                'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
            pygame.mixer.music.play()
            balance += 1
            total_balance_collected += 1
            esd_key1 = False
        if stage3:
            stage3_t = font4.render('Stage 3', True, 'Red')
            screen.blit(stage3_t, (435, 100))
        if stage4 and esd_key2:
            enemy_spawn_delay -= 40
            pygame.mixer.music.load(
                'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
            pygame.mixer.music.play(2)
            balance += 2
            total_balance_collected += 1
            esd_key2 = False
        if stage4:
            blit_stage4 = True
            if not wave_active and blit_stage4:
                stage4_t = font4.render('Stage 4', True, 'Red')
                screen.blit(stage4_t, (435, 100))
                timing_list = [9, 11, 14, 17, 21, 23, 26, 28, 30, 32, 36, 42, 45, 48]
                time_of_spawn = random.choice(timing_list)
                subtract_by = 50
                wave_spawn_s = int(truncate(elapsed_time1)) - subtract_by
                if wave_spawn_s > 26:
                    subtract_by -= 23
                    wave_spawn_s -= subtract_by
                    if subtract_by == 27:
                        def remove():
                            try:
                                timing_list.remove(9)
                                timing_list.remove(11)
                                timing_list.remove(14)
                                return timing_list
                            except ValueError:
                                return timing_list


                        timing_list = remove()
                        time_of_spawn = random.choice(timing_list)
                if wave_spawn_k:
                    crt = pygame.time.get_ticks()
                if wave_spawn_s == time_of_spawn and wave_spawn_k:
                    wave = True
                    wave_spawn_k = False
                    wave_active = True
                    progress = 0
                if wave_spawn_s - last_wave_time >= time_of_spawn:
                    last_wave_time = wave_spawn_s
                    enemy_wave_l.append(enemy_wave_1())
                if wave:
                    stage1 = False
                    stage2 = False
                    stage3 = False
                    stage4 = False
                    wave = False
        for enemy_wave in enemy_wave_l:
            enemy_wave.enemy1.move()
            enemy_wave.enemy1.draw()
            enemy_wave.enemy2.move()
            enemy_wave.enemy2.draw()
            wave_active = True
            blit_stage4 = False
            if enemy_wave.enemy1.get_rect().x > 100:
                wave_t = font4.render('Wave', True, 'Red')
                screen.blit(wave_t, (455, 100))
            stage4 = False
            if player_rect.colliderect(enemy_wave.enemy1.get_rect()):
                player_rect.bottom = 600
                velocity_y = 0
                ticks_pk = False
                game_started = False
                end_screen = True
                score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
                a_score = int(truncate(score))
                save_score(a_score)  # Save the current score
            if enemy_wave.enemy1.get_rect().x <= -100:
                enemy_allow_spawn = True
                enemy_triangle.reset()
                enemy_circle.reset()
                enemy_square.reset()
                wave_active = False
                wave_spawn_k = True
                stage4 = True
        if player_rect.bottom >= 600 or player_rect.bottom <= 0:
            player_rect.bottom = 600
            velocity_y = 0
            ticks_pk = False
            game_started = False
            end_screen = True
            wave_active = False
            score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
            a_score = int(truncate(score))
            save_score(a_score)  # Save the current score

        if design == 'outline':
            pygame.draw.rect(screen, secondary_colour, player_rect, outline_size)
        if design == 'inner circle':
            draw_circle(radius_length, (player_rect.x + 20, player_rect.y + 20))
        if design == 'rainbow':
            frame_count += 1
            if frame_count >= colour_change_interval:
                frame_count = 0  # Reset frame counter
                player_colour = next(color_cycle)  # Get the next color in the cycle
        if custom_skin == 'cn':
            screen.blit(cn, player_rect)
        if custom_skin == 'alien':
            screen.blit(alien, player_rect)
        if custom_skin == 'flower':
            screen.blit(flower, player_rect)
        if custom_skin == 'mars':
            screen.blit(mars, player_rect)
        if custom_skin == 'plane':
            screen.blit(plane, player_rect)
        if custom_skin == 'smurf':
            screen.blit(smurf, player_rect)

        score = (pygame.time.get_ticks() - ticks) / 1000 * 4.42857142 * game_speed_multiplier
        a_score = int(truncate(score))
        str_score = str(a_score)
        str_score1 = str_score.zfill(6)
        full_text = f"{s_text}{str_score1}"
        f_text = font1.render(full_text, True, 'Black')
        screen.blit(f_text, (790, 100))
        screen.blit(text1, (20, 100))
        screen.blit(e_t_text, (210, 100))
        screen.blit(cloud1, (0, 0))
        screen.blit(cloud1, (200, 0))
        screen.blit(cloud1, (400, 0))
        screen.blit(cloud1, (600, 0))
        screen.blit(cloud1, (800, 0))
        screen.blit(cloud1, (0, 513))
        screen.blit(cloud1, (200, 513))
        screen.blit(cloud1, (400, 513))
        screen.blit(cloud1, (600, 513))
        screen.blit(cloud1, (800, 513))
        screen.blit(coin, (10, 545))
        screen.blit(balance_text, (50, 542))
        if a_score % 50 == 0 and a_score != 0:
            if not pk:
                pygame.mixer.music.load(
                    'zapsplat_foley_money_british_coin_20p_set_down_on_other_coins_in_hand_change_001_90492.mp3')
                pygame.mixer.music.play()
                balance += 1
                total_balance_collected += 1
                pk = True

        # Reset pk to False immediately after the balance is updated
        if a_score % 50 == 1 and a_score != 1:
            pk = False
        pygame.display.flip()
        clock.tick(tickk)

    if end_screen:
        screen.fill((50, 100, 180))
        h_text = font1.render('(hover)', True, black)
        h_rect = h_text.get_rect(midtop=(500, 400))
        balance_text = font4.render(str(balance), True, black)
        f_text = f_text
        e_t = e_t
        minutes = round(elapsed_time1, 0) // 60  # Get the whole number of minutes
        remaining_seconds = round(elapsed_time1, 0) % 60  # Get the remaining seconds
        if minutes != 0:
            tim1 = 'You survived for: ' + str(int(minutes)) + ' minute(s) and ' + str(
                int(remaining_seconds)) + ' seconds.'
            tim_t1 = font1.render(tim1, True, 'Black')
            screen.blit(tim_t1, (20, 20))
        else:
            tim = 'You survived for: ' + e_t
            tim_t = font1.render(tim, True, 'Black')
            screen.blit(tim_t, (20, 20))
        sco = 'Score: ' + str_score
        sco_t = font1.render(sco, True, 'Black')
        y_d = font3.render('You died!', True, 'Red')
        screen.blit(sco_t, (820, 20))
        screen.blit(y_d, (310, 245))
        screen.blit(coin, (880, 540))
        screen.blit(balance_text, (920, 537))
        screen.blit(h_text, h_rect)

        # Draw restart button rectangle and text
        mp = pygame.mouse.get_pos()
        if not restart_button_rect.collidepoint(mp):
            pygame.draw.rect(screen, restart_button_color, restart_button_rect)
        if restart_button_rect.collidepoint(mp):
            pygame.draw.rect(screen, 'Gray', restart_button_rect)
        if not home_button_rect.collidepoint(mp):
            pygame.draw.rect(screen, restart_button_color, home_button_rect)
        if home_button_rect.collidepoint(mp):
            pygame.draw.rect(screen, 'Gray', home_button_rect)
        restart_text = font1.render('Restart', True, 'White')
        screen.blit(restart_text, (restart_button_rect.centerx - restart_text.get_width() // 2,
                                   restart_button_rect.centery - restart_text.get_height() // 2))
        screen.blit(home_text, (home_button_rect.centerx - home_text.get_width() // 2,
                                home_button_rect.centery - home_text.get_height() // 2))

        # Display the highest score
        highest_score = get_highest_score()
        highest_score_text = font1.render(f'High Score: {highest_score}', True, 'Black')
        screen.blit(highest_score_text, (20, 540))
        my_instance.draw()

        pygame.display.flip()
        clock.tick(600)

quit1 = False

while running is False:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit1:
            try:
                if account1:
                    os.remove('player_data.json')
                    os.remove("autosavestate.json")
                if account2:
                    os.remove('player_data1.json')
                    os.remove("autosavestate1.json")
                if account3:
                    os.remove('player_data2.json')
                    os.remove("autosavestate2.json")
                if account4:
                    os.remove('player_data3.json')
                    os.remove("autosavestate3.json")
                print('Progress successfully terminated!')
            except FileNotFoundError:
                print('File was not found.')
            except PermissionError:
                print('Access denied.')
            except Exception as e:
                print(f"An error occurred in the process: {e}")
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lax_rect.collidepoint(event.pos):
                quit1 = True

    lax = font1.render("Please click the 'x' button to finish the process, or click this text.", True, red)
    lax_rect = lax.get_rect(center=(500, 200))
    screen.blit(lax, lax_rect)
    pygame.display.flip()
    clock.tick(60)

while running is None:
    acc_change = input('Switch to: Account 1 [a], Account 2 [b], Account 3 [c] or Account 4 [d]? ')
    if acc_change == 'a':
        account1 = True
        account2 = False
        account3 = False
        account4 = False
        print('Accounts successfully switched!')
        AccountData = {
            "Account1": account1,
            "Account2": account2,
            "Account3": account3,
            "Account4": account4
        }
        with open("account_data.json", "w") as AccountDataFile:
            json.dump(AccountData, AccountDataFile, indent=2)
    if acc_change == 'b':
        account1 = False
        account2 = True
        account3 = False
        account4 = False
        print('Accounts successfully switched!')
        AccountData = {
            "Account1": account1,
            "Account2": account2,
            "Account3": account3,
            "Account4": account4
        }
        with open("account_data.json", "w") as AccountDataFile:
            json.dump(AccountData, AccountDataFile, indent=2)
    if acc_change == 'c':
        account1 = False
        account2 = False
        account3 = True
        account4 = False
        print('Accounts successfully switched!')
        AccountData = {
            "Account1": account1,
            "Account2": account2,
            "Account3": account3,
            "Account4": account4
        }
        with open("account_data.json", "w") as AccountDataFile:
            json.dump(AccountData, AccountDataFile, indent=2)
    if acc_change == 'd':
        account1 = False
        account2 = False
        account3 = False
        account4 = True
        print('Accounts successfully switched!')
        AccountData = {
            "Account1": account1,
            "Account2": account2,
            "Account3": account3,
            "Account4": account4
        }
        with open("account_data.json", "w") as AccountDataFile:
            json.dump(AccountData, AccountDataFile, indent=2)
    pygame.quit()
    sys.exit()
