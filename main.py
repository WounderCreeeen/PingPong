from play import *
from random import *
from keyboard import *
plr1 = new_box(color = 'blue', x=350, y=0, height=100, width=5)
plr2 = new_box(color = 'red', x=-350, y=-0, height=100, width=5)
ball = new_box(color='white', border_color='black', border_width=1, x=0, y=0, height=25, width=25)


plr1.hide()
plr2.hide()
ball.hide()

playButton1=new_text(words='PLAY(solo)', y=25)
playButton2=new_text(words='PLAY(duo)', y=-25)
exitButton=new_text(words='EXIT', y=-75)


status=0

@repeat_forever
def game():
    plr1ScoreInt = 0
    plr2ScoreInt = 0
    plr1ScoreStr = str(plr1ScoreInt)
    plr2ScoreStr = str(plr2ScoreInt)
    plr1Score = new_text(words=plr1ScoreStr, color='blue', x=25, y=250)
    stick = new_text(words='|', y=250)
    plr2Score = new_text(words=plr2ScoreStr, color='red', x=-25, y=250)
    global status
    if status == 0:
        plr1Score.hide()
        plr2Score.hide()
        stick.hide()
        if write('cheat'):
            status=100
            print(status)
        if playButton1.is_clicked:
            playButton1.hide()
            playButton2.hide()
            exitButton.hide()
            status=1
        if playButton2.is_clicked:
            playButton1.hide()
            playButton2.hide()
            exitButton.hide()
            status = 2
        if exitButton.is_clicked:
            exit()
    if status == 1:
        ball.show()
        plr1.show()
        plr2.show()
        plr1Score.show()
        plr2Score.show()
        stick.show()
        ball.start_physics(can_move=True, obeys_gravity=False, x_speed=randint(-50, 50), y_speed=randint(-50, 50))
        plr1.start_physics(can_move=False)
        plr2.start_physics(can_move=False)

        plr1.physics.x_speed=0
        plr2.physics.x_speed=0
        plr1.x=350
        plr2.x=-350
        if ball.x < plr2.x:
            ball.x = 0
            ball.y = 0
            ball.physics.x_speed = randint(-50, 50)
            ball.physics.y_speed = randint(-50, 50)
            plr1ScoreInt+=1
            plr1ScoreStr = str(plr1ScoreInt)
        if ball.x > plr1.x:
            ball.x = 0
            ball.y = 0
            ball.physics.x_speed = randint(-50, 50)
            ball.physics.y_speed = randint(-50, 50)
            plr2ScoreInt+=1
            plr2ScoreStr = str(plr2ScoreInt)
        if key_is_pressed('w'):
            plr1.y += 15
        if key_is_pressed('s'):
            plr1.y -= 15
        if plr2.y != ball.y:
            plr2.y = ball.y
        if key_is_pressed('r'):
            plr1.y=0
            plr2.y=0
            ball.x=0
            ball.y=0
            ball.physics.x_speed=randint(-50, 50)
            ball.physics.y_speed=randint(-50, 50)
    if status == 2:
        ball.show()
        plr1.show()
        plr2.show()
        plr1Score.show()
        plr2Score.show()
        stick.show()
        ball.start_physics(can_move=True, obeys_gravity=False, x_speed=randint(-50, 50), y_speed=randint(-50, 50))
        plr1.start_physics(can_move=False)
        plr2.start_physics(can_move=False)

        plr1.physics.x_speed=0
        plr2.physics.x_speed=0
        plr1.x=350
        plr2.x=-350

        if key_is_pressed('w'):
            plr1.y += 15
        if key_is_pressed('s'):
            plr1.y -= 15
        if key_is_pressed('y'):
            plr2.y += 15
        if key_is_pressed('h'):
            plr2.y -= 15
        if key_is_pressed('r'):
            plr1.y=0
            plr2.y=0
            ball.x=0
            ball.y=0
            ball.physics.x_speed=randint(-50, 50)
            ball.physics.y_speed=randint(-50, 50)












































start_program()