import pygame
import time

class SwitchDenGo():
    ACCEL_KNOTCH_NUM = 5
    BRAKE_KNOTCH_NUM = 9
    
    def __init__(self):
        pygame.init()
        self.joy = pygame.joystick.Joystick(0)
        self.ctrl_nums = (self.joy.get_numaxes(), self.joy.get_numballs(), self.joy.get_numbuttons(), self.joy.get_numhats())
        if self.ctrl_nums not in [(6, 0, 16, 0), (4, 0, 14, 1)]:
            raise Exception("サポートされていないコントローラです")
        self.joy.init()

    def loadStatus(self):
        self.brake_knotch = 0
        self.accel_knotch = 0
        self.buttons = []
        pygame.event.get()
        
        # ロンチ版
        if self.ctrl_nums == (6, 0, 16, 0):
            # Xボタン
            if self.joy.get_button(2):
                self.buttons.append("SW_X")
            # Yボタン
            if self.joy.get_button(3):
                self.buttons.append("SW_Y")
            # Aボタン
            if self.joy.get_button(0):
                self.buttons.append("SW_A")
            # Bボタン
            if self.joy.get_button(1):
                self.buttons.append("SW_B")
            # ○ボタン
            if self.joy.get_button(15):
                self.buttons.append("SW_CIRCLE")
            # HOMEボタン
            if self.joy.get_button(5):
                self.buttons.append("SW_HOME")
            
            knotch_level = self.joy.get_axis(1)
        elif self.ctrl_nums == (4, 0, 14, 1):
            # Xボタン
            if self.joy.get_button(3):
                self.buttons.append("SW_X")
            # Yボタン
            if self.joy.get_button(0):
                self.buttons.append("SW_Y")
            # Aボタン
            if self.joy.get_button(2):
                self.buttons.append("SW_A")
            # Bボタン
            if self.joy.get_button(1):
                self.buttons.append("SW_B")
            # ○ボタン
            if self.joy.get_button(13):
                self.buttons.append("SW_CIRCLE")
            # HOMEボタン
            if self.joy.get_button(12):
                self.buttons.append("SW_HOME")
            
            knotch_level = self.joy.get_axis(1)
        else:
            raise Exception("サポートされていないコントローラです")
        
        if knotch_level > 0.95:
            self.accel_knotch = 5
        elif knotch_level > 0.75:
            self.accel_knotch = 4
        elif knotch_level > 0.55:
            self.accel_knotch = 3
        elif knotch_level > 0.3:
            self.accel_knotch = 2
        elif knotch_level > 0.1:
            self.accel_knotch = 1
        elif knotch_level > -0.05:
            self.accel_knotch = 0
            self.brake_knotch = 0
        elif knotch_level > -0.25:
            self.brake_knotch = 1
        elif knotch_level > -0.35:
            self.brake_knotch = 2
        elif knotch_level > -0.45:
            self.brake_knotch = 3
        elif knotch_level > -0.55:
            self.brake_knotch = 4
        elif knotch_level > -0.7:
            self.brake_knotch = 5
        elif knotch_level > -0.8:
            self.brake_knotch = 6
        elif knotch_level > -0.9:
            self.brake_knotch = 7
        elif knotch_level > -1.0:
            self.brake_knotch = 8
        else:
            self.brake_knotch = 9
            
        if self.brake_knotch > 0:
            self.accel_knotch = 0
