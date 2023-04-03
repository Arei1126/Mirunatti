from microbit import *
from micropython import const
import machine


############################################################
# 全般の設定
PERIOD = const(1000)  # フレームレート (ms) 逆数がfps
SAVE_PERIOD = const(600)  # 10min

#############################################################
# 制限時間の設定,smallが1回ごとの開け時間の制限、中と大は累計の制限

LIMIT_SMALL = const(900)  # (s)15分,以下同様
ALERT_SMALL = const(600)  # 10min

PERIDO_MEDUIM = const(3600)  #1hour
LIMIT_MEDUIM = const(1800)  #30min 
ALERT_MEDUIM = const(1500)  #25min

PERIDO_LARGE = const(28800)  # 6hour
LIMIT_LARGE = const(5400)  #1h30m
ALERT_LARGE = const(5100)  #1h25min

#################################################
# 成長にかかる時間

BIRTH_TIME = const(3600)  # 30min
ADULT_TIME = const(14400)  # 4h 
###########################################
#イメージ定義

IMAGE_DEATH = Image("00900:"
                    "09990:"
                    "00900:"
                    "00900:"
                    "99999:")

IMAGE_EGG_NORMAL_0 = Image("00000:"
                           "09990:"
                           "09090:"
                           "09990:"
                           "00000:")

IMAGE_EGG_NORMAL_1 = Image("00000:"
                           "00999:"
                           "00909:"
                           "00999:"
                           "00000:")

IMAGE_EGG_ALERT_0 = Image("00000:"
                          "00900:"
                          "09090:"
                          "09900:"
                          "00000:")

IMAGE_EGG_ALERT_1 = Image("00000:"
                          "00090:"
                          "00909:"
                          "00990:"
                          "00000:")

IMAGE_CHILD_NORMAL_0 = Image("00090:"
                             "09000:"
                             "00000:"
                             "09090:"
                             "00900:")

IMAGE_CHILD_NORMAL_1 = Image("09000:"
                             "00090:"
                             "00000:"
                             "09090:"
                             "00900:")

IMAGE_CHILD_ALERT_0 = Image("00090:"
                            "09000:"
                            "00000:"
                            "00900:"
                            "09090:")

IMAGE_CHILD_ALERT_1 = Image("09000:"
                            "00090:"
                            "00000:"
                            "00900:"
                            "09090:")

IMAGE_ADULT_NORMAL_0 = Image("00000:"
                             "09009:"
                             "00000:"
                             "90009:"
                             "09990:")

IMAGE_ADULT_NORMAL_1 = Image("00000:"
                             "90090:"
                             "00000:"
                             "90009:"
                             "09990:")

IMAGE_ADULT_ALERT_0 = Image("00000:"
                            "09009:"
                            "00000:"
                            "09990:"
                            "90009:")

IMAGE_ADULT_ALERT_1 = Image("00000:"
                            "90090:"
                            "00000:"
                            "09990:"
                            "90009:")

#IMAGE_SAD_0 = Image.UMBRELLA

#IMAGE_SAD_SMALL_1 = Image("09999:"
#                         "90000:"
#                         "09999:"
#                         "00009:"
#                         "99990:")

#IMAGE_SAD_MEDUIM_1 = Image("09090:"
#                          "90909:"
#                          "90909:"
#                          "90909:"
#                         "90900:")

#IMAGE_SAD_LARGE_1 = Image("90000:"
#                         "90000:"
#                         "90000:"
#                         "90000:"
#                         "99999:")

###################################
#アニメーション定義

IMAGE_EGG_NORMAL = [IMAGE_EGG_NORMAL_0, IMAGE_EGG_NORMAL_1]
IMAGE_EGG_ALERT = [IMAGE_EGG_ALERT_0, IMAGE_EGG_ALERT_1]

IMAGE_CHILD_NORMAL = [IMAGE_CHILD_NORMAL_0, IMAGE_CHILD_NORMAL_1]
IMAGE_CHILD_ALERT = [IMAGE_CHILD_ALERT_0, IMAGE_CHILD_ALERT_1]

IMAGE_ADULT_NORMAL = [IMAGE_ADULT_NORMAL_0, IMAGE_ADULT_NORMAL_1]
IMAGE_ADULT_ALERT = [IMAGE_ADULT_ALERT_0, IMAGE_ADULT_ALERT_1]

IMAGE_LOVE = [Image.HEART_SMALL, Image.HEART]

#IMAGE_SAD_SMALL = [IMAGE_SAD_0, IMAGE_SAD_SMALL_1]
#IMAGE_SAD_MEDUIM = [IMAGE_SAD_0, IMAGE_SAD_MEDUIM_1]
#IMAGE_SAD_LARGE= [IMAGE_SAD_0, IMAGE_SAD_LARGE_1]


##################################
#Initialization
######################################
#関数定義

# ボタンのラッパーさえ削らなければならなかった
#def chk_used():
#    return not pin0.read_digital()

#def chk_button_reset():
#    return (button_a.is_pressed() and button_b.is_pressed())

#def chk_button_emotion():
#    return button_a.is_pressed()

#def chk_button_status():
#    return button_b.is_pressed()

# どの顔を表示するか決める
def determine_face(age, alert,death):
    if death == True:
        return 0
    if age == 0 :
        if alert == True:
            return 2
        else:
            return 1
    
    if age == 1 :
        if alert == True:
            return 4
        else:
            return 3

    if age == 2 :
        if alert == True:
            return 6
        else:
            return 5

# 指定した顔を表示する
def draw_face(face):
    if face == 0:
        display.show(IMAGE_DEATH)
    elif face == 1:
        display.show(IMAGE_EGG_NORMAL,delay=500,loop=True,wait=False)
    elif face == 2:
        display.show(IMAGE_EGG_ALERT,delay=500,loop=True,wait=False)
    elif face == 3:
        display.show(IMAGE_CHILD_NORMAL,delay=500,loop=True,wait=False)
    elif face == 4:
        display.show(IMAGE_CHILD_ALERT,delay=500,loop=True,wait=False)
    elif face == 5:
        display.show(IMAGE_ADULT_NORMAL,delay=500,loop=True,wait=False)
    elif face == 6:
        display.show(IMAGE_ADULT_ALERT,delay=500,loop=True,wait=False)

# 時間を表示するだけ
def draw_status(timer):
    display.scroll(timer,wait=True)

# 感情の表示（全機能版）、S/M/Lどの種類でやばいか表示できた
#def draw_emotion(al_s,al_m,al_l):
#    if al_s == True:
#        display.show(IMAGE_SAD_SMALL,delay=500,loop=True,wait=False)
#    elif al_m == True:
#        display.show(IMAGE_SAD_MEDUIM,delay=500,loop=True,wait=False)
#    elif al_l == True:
#        display.show(IMAGE_SAD_LARGE,delay=500,loop=True,wait=False)
#    else:
#        display.show(IMAGE_LOVE,delay=500,loop=True,wait=False)
#    utime.sleep_ms(4*PERIOD)

# 感情の表示・機能制限版、やばいかやばくないかだけ表示。
def draw_emotion(alert):
    if alert:
        display.show(Image.UMBRELLA,wait=False)
    else:
        #display.show(Image.HEART,wait=False)
        display.show(IMAGE_LOVE,delay=500,loop=True,wait=False)
        sleep(3*PERIOD)

# メモリ削減用の関数群
def chk_time(timer,time):
            return timer >= time

def chk_time_period(timer,period):
            return timer % period ==0

##
# セーブ用関数

def save(data):
    with open("save","w") as f:
        f.write(str(data))

def load():
    with open("save","r") as f:
        return int(f.read())

# 以下、本来のフル機能のセーブ・ロード関数
#def save(GT,ST,MT,LT,):
#    with open("saveGT","w") as sGT:
#        sGT.write(str(GT))#
#
#    with open("saveST","w") as sST:
#        sST.write(str(ST))
#    
#    with open("saveMT","w") as sMT:
#        sMT.write(str(MT))##
#
#    with open("saveLT","w") as sLT:
#        sLT.write(str(LT))   
    
#def load():
##    data = []
#    with open("saveGT","r") as sGT:
#        data[0] = int(sGT.read())
#
##    with open("saveST","r") as sST:
#        data[1] = int(sST.read())
#
#    with open("saveMT","r") as sMT:
#        data[2] = int(sMT.read())
#
#    with open("saveLT","r") as sLT:
#       data[3] = int(sLT.read())
#
#    return data

###############################################################################
# main function
################################################################################


def main():

    #変数定義
    
    Global_Timer = 0
    Small_Timer = 0
    Medium_Timer = 0
    Large_Timer = 0
    
    Alert = False
    Alert_Small = False
    Alert_Medium = False
    Alert_Large = False
    
    Age = 0  # 0卵 1子供 2大人 3死 
    Death = False

    Face = 0 # 表示する顔、0death 1EggNormal 2EggAlert 3ChildNormal 4ChileAlert 5AdultNormal 6AdultAlert

    #####
    # セーブ　初期化
    save(Global_Timer)
    
    
    #################################
    # main loop
    
    while True:

        # タイマー加算
        Global_Timer += 1      
        Small_Timer += 1
        Medium_Timer += 1
        Large_Timer += 1
        
        if (Global_Timer % SAVE_PERIOD )== 0:  # オートセーブ
            save(Global_Timer)
        
        if Death:
            Global_Timer -= 1

        ##########################################    
        # 閉じているときのルーチン
        if  pin0.read_digital():             
            display.clear()

            Alert_Small = False  # 一度に開く時間を測るスモールタイマーはリセット
            Small_Timer = 0

            if button_a.is_pressed() and button_b.is_pressed():  # 3つのボタンでロードする・中・大タイマーはリセット
                Global_Timer = load()
                Medium_Timer = 0
                Large_Timer = 0
            
            sleep(PERIOD)
            continue
        ############################################

        #ab同時押しでリセット
        if button_a.is_pressed() and button_b.is_pressed():
            machine.reset()
       
        # bで生存時間確認
        if button_b.is_pressed():
            draw_status(Global_Timer)

        # aでアラート（感情）確認
        if button_a.is_pressed():
           draw_emotion(Alert)
      
    
         # スモールタイマー系チェック
        Alert_Small = chk_time(Small_Timer,ALERT_SMALL)
        Death = chk_time(Small_Timer,LIMIT_SMALL)
    
        # 中・大タイマーアラートチェック
        Alert_Medium = chk_time(Medium_Timer,ALERT_MEDUIM)
        Alert_Large = chk_time(Large_Timer,ALERT_LARGE)

   
        #中・大タイマー初期化,死亡判定
        if chk_time_period(Global_Timer,PERIDO_MEDUIM):
            if chk_time(Global_Timer,LIMIT_MEDUIM):
                Death = True
            else:
                Medium_Timer = 0
                Alert_Medium = False
        
            
        if chk_time_period(Global_Timer,PERIDO_LARGE):
            if chk_time(Global_Timer,LIMIT_LARGE):
                Death= True
            else:
                Medium_Timer = 0
                Alert_Large = False

        # 成長度チェック
        if 0 <= Global_Timer < BIRTH_TIME:
            Age = 0
    
        if BIRTH_TIME <= Global_Timer < ADULT_TIME:
            Age = 1
        if ADULT_TIME <= Global_Timer:
            Age = 2
            
        Alert = Alert_Small or Alert_Medium or Alert_Large  # 簡易表示用のアラートフラグ
        
        Face = determine_face(Age,Alert,Death)
        
        draw_face(Face)

        sleep(PERIOD)

##############################################################################################


main()
    
        

    
        




