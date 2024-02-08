import pygame
from pygame import mixer
import random
import math

pygame.init()

# 游戏画面
width = 800
height = 600
screen = pygame.display.set_mode((width , height))

# 游戏标题
pygame.display.set_caption("SlapFace")

# 游戏图案
icon = pygame.image.load('privacy (1).png')
pygame.display.set_icon(icon)

# 游戏背景
background = pygame.image.load('brown-wooden-flooring.png')

# 玩家
hand = pygame.image.load('privacy (1).png')
slap = pygame.image.load('hello.png')
# 玩家处于画面的位置
hand_x = 380
hand_y = 80
# 玩家的移动
hand_xmove = 0
hand_ymove = 0

# 水果
zijet = pygame.image.load('zijet.png')
# 水果处于画面的位置
zijet_x = random.randint(0, 800)
zijet_y = random.randint(600, 700)
# 水果的移动
zijet_xmove = 0
zijet_ymove = 0.5

# 炸弹
teacher = pygame.image.load('teacher.png')
# 炸弹处于画面的位置
teacher_x = random.randint(0,800)
teacher_y = random.randint(1600,1700)
# 炸弹的移动
teacher_xmove = 0
teacher_ymove = 0.5

# 分数
score = 0
font = pygame.font.Font('freesansbold.ttf', 20)
# 分数处于画面的位置
text_x = 700
text_y = 580

rule_font = pygame.font.Font('freesansbold.ttf', 30)
ruletext_x = 180
ruletext_y = 250

# 游戏结束字样
gameover_font = pygame.font.Font('freesansbold.ttf', 64)
# 游戏结束字样处于画面的位置
gotext_x = 219
gotext_y = 259

# Function
def player():
    # 画出手以及其位置
    screen.blit(hand,(hand_x, hand_y))

def zijetface():
    # 画出子杰以及其位置
    screen.blit(zijet,(zijet_x, zijet_y))

def teacherface():
    # 画出老师以及其位置
    screen.blit(teacher,(teacher_x, teacher_y))

def collide_zijet():
    # 距离公式（测试水果和手之间的距离，靠近的话就视为撞击）
    distance_zijet = math.sqrt(math.pow(zijet_x - hand_x, 2) + (math.pow(zijet_y - hand_y, 2)))
    if distance_zijet < 60:
        return True

def collide_teacher():
    # 距离公式（测试老师和手之间的距离，靠近的话就视为撞击）
    distance_teacher = math.sqrt(math.pow(teacher_x - hand_x, 2) + (math.pow(teacher_y - hand_y, 2)))
    if distance_teacher < 60:
        return True

def scores():
    # 分数显示
    s = font.render("Score : " + str(score), True, (0, 0, 0))
    screen.blit(s,(text_x,text_y))

def rule():
    r = rule_font.render("Slap Zijet, Don't Slap Teacher!", True, (255, 255, 255))
    screen.blit(r, (ruletext_x, ruletext_y))

def gameover():
    # 游戏结束字样显示
    g = gameover_font.render("Game Over ", True, (255, 255, 255))
    screen.blit(g, (gotext_x, gotext_y))

# Loop
running = True
while running:

    # 画出背景
    screen.blit(background,(0,0))

    # 游戏里行动的loop
    for event in pygame.event.get():
        # 关闭游戏
        if event.type == pygame.QUIT:
            running = False

        # 按按键
        if event.type == pygame.KEYDOWN:
            # 左键
            if event.key == pygame.K_LEFT:
                hand_xmove = -2.75
            # 右键
            elif event.key == pygame.K_RIGHT:
                hand_xmove = 2.75
            # 上键
            elif event.key == pygame.K_UP:
                hand_ymove = -2.75
            # 下键
            elif event.key == pygame.K_DOWN:
                hand_ymove = 2.75
        # 不按按键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                hand_xmove = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                hand_ymove = 0

    # 玩家处于的X轴会随着按按键移动而改变
    hand_x += hand_xmove
    # 玩家处于的Y轴会随着按按键移动而改变
    hand_y += hand_ymove

    # 限制玩家在画面的框架里
    if hand_x <= 0:
        hand_x = 0
    if hand_x >= 736:
        hand_x = 736
    if hand_y <= 0:
        hand_y = 0
    if hand_y >= 500:
        hand_y = 500

    # 子杰处于的Y轴会随着自身移动而改变
    zijet_y += zijet_ymove
    # 子杰在游戏画面下出现（有突然出来的感觉）
    if zijet_y >= height:
        zijet_ymove = -2.50
        zijet_x = random.randint(0, 736)
        # 当子杰飞出画面，将会在X轴上不同的位置上回来
    if zijet_y <= -500:
        zijet_y = random.randint(600, 700)
        zijet_x = random.randint(0, 736)
        # 并且发出声音
        noslap = mixer.Sound("noobshit.wav")
        noslap.play()

    # 老师处于的Y轴会随着自身移动而改变
    teacher_y += teacher_ymove
    # 老师在游戏画面下出现（有突然上来的感觉）
    if teacher_y >= height:
        teacher_ymove = -2.50
        # 当老师飞出画面，将会在X轴上不同的位置上回来
        teacher_x = random.randint(0, 736)
    if teacher_y <= -1500: # -1500是为了让老师飛久一点就不会像子杰那么频繁的出现
        teacher_y = random.randint(600, 700)

    # 当子杰和手撞击
    collision_zijet = collide_zijet()
    if collision_zijet:
        # 播放音乐
        slap = mixer.Sound("slap.wav")
        slap.play()
        # 分数递增
        score += 1
        # 子杰在新的地方出现
        zijet_x = random.randint(0, 736)
        zijet_y = random.randint(600, 700)

    # 当老师和手撞击
    collision_teacher = collide_teacher()
    if collision_teacher:
        # 播放音乐
        explode = mixer.Sound("aiya.wav")
        explode.play()
        # 分数归零
        score = 0
        # 老师在新的地方出现
        teacher_x = random.randint(0, 736)
        teacher_y = random.randint(1700, 1800)

    if score == 0:
         rule()

    # 结束游戏
    if score >= 15:
        gameover()
        # 子杰和老师被限制在游戏画面外
        zijet_y = random.randint(1700, 1800)
        teacher_y = random.randint(1700, 1800)
        # 玩家不能移动
        hand_xmove = 0
        hand_ymove = 0

    # 把Function带进loop里
    player()
    zijetface()
    teacherface()
    scores()
    pygame.display.update()
