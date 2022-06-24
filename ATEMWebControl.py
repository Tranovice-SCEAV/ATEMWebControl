# -*- coding: utf-8 -*-
# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from importlib.resources import path
from remi.gui import *
from remi import start, App
import PyATEMMax
import time
from Config import *

# ─── API CONFIG AND SETUP ───────────────────────────────────────────────────────
#PyATEMMax config and setup
switcher = PyATEMMax.ATEMMax()

switcher.connect(SWITCHERIP)
switcher.waitForConnection()

class SwitcherWeb(App):
    #Initiation
    def __init__(self, *args, **kwargs):
        self.tallySOURCE = 0
        super(SwitcherWeb, self).__init__(*args)

    #Auto update
    def idle(self):
        #Update detection

        tally_1 = str(switcher.tally.bySource.flags[1])

        if tally_1 == "[PGM]":
            self.src1.css_background_color = "rgb(220,69,69)"
            self.tally1.css_background_color = "rgb(220,69,69)"
        elif tally_1 == "[PVW]":
            self.src1.css_background_color = "rgb(165,240,120)"
            self.tally1.css_background_color = "rgb(165,240,120)"
        elif tally_1 == "[]":
            self.src1.css_background_color = "rgb(170,170,170)"
            self.tally1.css_background_color = "rgb(170,170,170)"
        elif tally_1 == "[PGM][PVW]":
            self.src1.css_background_color = "rgb(220,69,69)"
            self.tally1.css_background_color = "rgb(220,69,69)"
        
        tally_2 = str(switcher.tally.bySource.flags[2])

        if tally_2 == "[PGM]":
            self.src2.css_background_color = "rgb(220,69,69)"
            self.tally2.css_background_color = "rgb(220,69,69)"
        elif tally_2 == "[PVW]":
            self.src2.css_background_color = "rgb(165,240,120)"
            self.tally2.css_background_color = "rgb(165,240,120)"
        elif tally_2 == "[]":
            self.src2.css_background_color = "rgb(170,170,170)"
            self.tally2.css_background_color = "rgb(170,170,170)"
        elif tally_2 == "[PGM][PVW]":
            self.src2.css_background_color = "rgb(220,69,69)"
            self.tally2.css_background_color = "rgb(220,69,69)"
        
        tally_3 = str(switcher.tally.bySource.flags[3])

        if tally_3 == "[PGM]":
            self.src3.css_background_color = "rgb(220,69,69)"
            self.tally3.css_background_color = "rgb(220,69,69)"
        elif tally_3 == "[PVW]":
            self.src3.css_background_color = "rgb(165,240,120)"
            self.tally3.css_background_color = "rgb(165,240,120)"
        elif tally_3 == "[]":
            self.src3.css_background_color = "rgb(170,170,170)"
            self.tally3.css_background_color = "rgb(170,170,170)"
        elif tally_3 == "[PGM][PVW]":
            self.src3.css_background_color = "rgb(220,69,69)"
            self.tally3.css_background_color = "rgb(220,69,69)"

        tally_4 = str(switcher.tally.bySource.flags[4])

        if tally_4 == "[PGM]":
            self.src4.css_background_color = "rgb(220,69,69)"
            self.tally4.css_background_color = "rgb(220,69,69)"
        elif tally_4 == "[PVW]":
            self.src4.css_background_color = "rgb(165,240,120)"
            self.tally4.css_background_color = "rgb(165,240,120)"
        elif tally_4 == "[]":
            self.src4.css_background_color = "rgb(170,170,170)"
            self.tally4.css_background_color = "rgb(170,170,170)"
        elif tally_4 == "[PGM][PVW]":
            self.src4.css_background_color = "rgb(220,69,69)"
            self.tally4.css_background_color = "rgb(220,69,69)"
        #tally background update
        if self.tallySOURCE == 0:
            self.Tally.css_background_color = "rgb(239,156,47)"
        else: 
            tally_bck = str(switcher.tally.bySource.flags[self.tallySOURCE])

            if tally_bck == "[PGM]":
                self.Tally.css_background_color = "rgb(220,69,69)"
            elif tally_bck == "[PVW]":
                self.Tally.css_background_color = "rgb(165,240,120)"
            elif tally_bck == "[]":
                self.Tally.css_background_color = "rgb(170,170,170)"
            elif tally_bck == "[PGM][PVW]":
                self.Tally.css_background_color = "rgb(220,69,69)"
        pass
    
    def main(self):
        #returns design
        return SwitcherWeb.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #Design
        self.tabbox0 = TabBox()
        self.tabbox0.attr_class = "TabBox"
        self.tabbox0.attr_editor_newclass = False
        self.tabbox0.css_border_radius = "22px"
        self.tabbox0.css_height = "95%"
        self.tabbox0.css_left = "0.0px"
        self.tabbox0.css_position = "absolute"
        self.tabbox0.css_top = "0.0px"
        self.tabbox0.css_width = "100%"
        self.tabbox0.variable_name = "tabbox0"
        self.Switcher = Container()
        self.Switcher.attr_class = "Container"
        self.Switcher.attr_editor_newclass = False
        self.Switcher.css_background_color = "rgb(239,156,47)"
        self.Switcher.css_border_radius = "22px"
        self.Switcher.css_display = "block"
        self.Switcher.css_height = "88%"
        self.Switcher.css_left = "0%"
        self.Switcher.css_position = "absolute"
        self.Switcher.css_top = "12%"
        self.Switcher.css_width = "100%"
        self.Switcher.variable_name = "Switcher"
        self.src1 = Button()
        self.src1.attr_class = "Button"
        self.src1.attr_editor_newclass = False
        self.src1.css_background_color = "rgb(170,170,170)"
        self.src1.css_border_radius = "22px"
        self.src1.css_font_size = "250%"
        self.src1.css_height = "14.5%"
        self.src1.css_left = "2%"
        self.src1.css_position = "absolute"
        self.src1.css_top = "85%"
        self.src1.css_width = "12%"
        self.src1.text = "1"
        self.src1.variable_name = "src1"
        self.Switcher.append(self.src1,'src1')
        self.src2 = Button()
        self.src2.attr_class = "Button"
        self.src2.attr_editor_newclass = False
        self.src2.css_background_color = "rgb(170,170,170)"
        self.src2.css_border_radius = "22px"
        self.src2.css_font_size = "250%"
        self.src2.css_height = "14.5%"
        self.src2.css_left = "15%"
        self.src2.css_position = "absolute"
        self.src2.css_top = "85%"
        self.src2.css_width = "12%"
        self.src2.text = "2"
        self.src2.variable_name = "src2"
        self.Switcher.append(self.src2,'src2')
        self.src3 = Button()
        self.src3.attr_class = "Button"
        self.src3.attr_editor_newclass = False
        self.src3.css_background_color = "rgb(170,170,170)"
        self.src3.css_border_radius = "22px"
        self.src3.css_font_size = "250%"
        self.src3.css_height = "14.5%"
        self.src3.css_left = "28%"
        self.src3.css_position = "absolute"
        self.src3.css_top = "85%"
        self.src3.css_width = "12%"
        self.src3.text = "3"
        self.src3.variable_name = "src3"
        self.Switcher.append(self.src3,'src3')
        self.src4 = Button()
        self.src4.attr_class = "Button"
        self.src4.attr_editor_newclass = False
        self.src4.css_background_color = "rgb(170,170,170)"
        self.src4.css_border_radius = "22px"
        self.src4.css_font_size = "250%"
        self.src4.css_height = "14.5%"
        self.src4.css_left = "41%"
        self.src4.css_position = "absolute"
        self.src4.css_top = "85%"
        self.src4.css_width = "12%"
        self.src4.text = "4"
        self.src4.variable_name = "src4"
        self.Switcher.append(self.src4,'src4')
        self.cut = Button()
        self.cut.attr_class = "Button"
        self.cut.attr_editor_newclass = False
        self.cut.css_background_color = "rgb(170,170,170)"
        self.cut.css_border_radius = "22px"
        self.cut.css_font_size = "250%"
        self.cut.css_height = "14%"
        self.cut.css_left = "68%"
        self.cut.css_position = "absolute"
        self.cut.css_top = "85%"
        self.cut.css_width = "12%"
        self.cut.text = "CUT"
        self.cut.variable_name = "cut"
        self.Switcher.append(self.cut,'cut')
        self.auto = Button()
        self.auto.attr_class = "Button"
        self.auto.attr_editor_newclass = False
        self.auto.css_background_color = "rgb(170,170,170)"
        self.auto.css_border_radius = "22px"
        self.auto.css_font_size = "250%"
        self.auto.css_height = "14%"
        self.auto.css_left = "81%"
        self.auto.css_position = "absolute"
        self.auto.css_top = "85%"
        self.auto.css_width = "12%"
        self.auto.text = "AUTO"
        self.auto.variable_name = "auto"
        self.Switcher.append(self.auto,'auto')
        self.tabbox0.append(self.Switcher,'Switcher')
        self.Tally = Container()
        self.Tally.attr_class = "Tally"
        self.Tally.attr_editor_newclass = False
        self.Tally.css_border_radius = "22px"
        self.Tally.css_display = "none"
        self.Tally.css_height = "89%"
        self.Tally.css_left = "0px"
        self.Tally.css_position = "absolute"
        self.Tally.css_top = "11%"
        self.Tally.css_width = "100%"
        self.Tally.variable_name = "Tally"
        self.tally1 = Button()
        self.tally1.attr_class = "Button"
        self.tally1.attr_editor_newclass = False
        self.tally1.css_background_color = "rgb(170,170,170)"
        self.tally1.css_border_radius = "22px"
        self.tally1.css_font_size = "300%"
        self.tally1.css_height = "35%"
        self.tally1.css_left = "15.0px"
        self.tally1.css_position = "absolute"
        self.tally1.css_top = "30.0px"
        self.tally1.css_width = "45%"
        self.tally1.text = "1"
        self.tally1.variable_name = "tally1"
        self.Tally.append(self.tally1,'tally1')
        self.tally3 = Button()
        self.tally3.attr_class = "Button"
        self.tally3.attr_editor_newclass = False
        self.tally3.css_background_color = "rgb(170,170,170)"
        self.tally3.css_border_radius = "22px"
        self.tally3.css_font_size = "300%"
        self.tally3.css_height = "35%"
        self.tally3.css_left = "15.0px"
        self.tally3.css_position = "absolute"
        self.tally3.css_top = "50%"
        self.tally3.css_width = "45%"
        self.tally3.text = "3"
        self.tally3.variable_name = "tally3"
        self.Tally.append(self.tally3,'tally3')
        self.tally2 = Button()
        self.tally2.attr_class = "Button"
        self.tally2.attr_editor_newclass = False
        self.tally2.css_background_color = "rgb(170,170,170)"
        self.tally2.css_border_radius = "22px"
        self.tally2.css_font_size = "300%"
        self.tally2.css_height = "35%"
        self.tally2.css_left = "53.5%"
        self.tally2.css_position = "absolute"
        self.tally2.css_top = "30.0px"
        self.tally2.css_width = "45%"
        self.tally2.text = "2"
        self.tally2.variable_name = "tally2"
        self.Tally.append(self.tally2,'tally2')
        self.tally4 = Button()
        self.tally4.attr_class = "Button"
        self.tally4.attr_editor_newclass = False
        self.tally4.css_background_color = "rgb(170,170,170)"
        self.tally4.css_border_radius = "22px"
        self.tally4.css_font_size = "300%"
        self.tally4.css_height = "35%"
        self.tally4.css_left = "53.5%"
        self.tally4.css_position = "absolute"
        self.tally4.css_top = "50%"
        self.tally4.css_width = "45%"
        self.tally4.text = "4"
        self.tally4.variable_name = "tally4"
        self.Tally.append(self.tally4,'tally4')
        self.tabbox0.append(self.Tally,'Tally')
        #Button detection
        self.cut.onclick.do(self.on_button_pressed_cut)
        self.auto.onclick.do(self.on_button_pressed_auto)

        self.src1.onclick.do(self.on_button_pressed_1)
        self.src2.onclick.do(self.on_button_pressed_2)
        self.src3.onclick.do(self.on_button_pressed_3)
        self.src4.onclick.do(self.on_button_pressed_4)

        self.tally1.onclick.do(self.on_tally_pressed_1)
        self.tally2.onclick.do(self.on_tally_pressed_2)
        self.tally3.onclick.do(self.on_tally_pressed_3)
        self.tally4.onclick.do(self.on_tally_pressed_4)

        return self.tabbox0
    # ─── BUTTON FUNCTIONS ───────────────────────────────────────────────────────────
    def on_button_pressed_cut(self, widget):
        switcher.execCutME(0)
    def on_button_pressed_auto(self, widget):
        switcher.execAutoME(0)
    def on_button_pressed_1(self, widget):
        switcher.setPreviewInputVideoSource(0,1)
    def on_button_pressed_2(self, widget):
        switcher.setPreviewInputVideoSource(0,2)
    def on_button_pressed_3(self, widget):
        switcher.setPreviewInputVideoSource(0,3)
    def on_button_pressed_4(self, widget):
        switcher.setPreviewInputVideoSource(0,4)
    def on_tally_pressed_1(self, widget):
        self.tallySOURCE = 1
        self.tally1.css_color = "rgb(0,0,0)"
        self.tally2.css_color = "rgb(255,255,255)"
        self.tally3.css_color = "rgb(255,255,255)"
        self.tally4.css_color = "rgb(255,255,255)"
    def on_tally_pressed_2(self, widget):
        self.tallySOURCE = 2
        self.tally2.css_color = "rgb(0,0,0)"
        self.tally1.css_color = "rgb(255,255,255)"
        self.tally3.css_color = "rgb(255,255,255)"
        self.tally4.css_color = "rgb(255,255,255)"
    def on_tally_pressed_3(self, widget):
        self.tally3.css_color = "rgb(0,0,0)"
        self.tally1.css_color = "rgb(255,255,255)"
        self.tally2.css_color = "rgb(255,255,255)"
        self.tally4.css_color = "rgb(255,255,255)"
        self.tallySOURCE = 3
    def on_tally_pressed_4(self, widget):
        self.tallySOURCE = 4
        self.tally4.css_color = "rgb(0,0,0)"
        self.tally1.css_color = "rgb(255,255,255)"
        self.tally2.css_color = "rgb(255,255,255)"
        self.tally3.css_color = "rgb(255,255,255)"

# ─── WEB STARTUP ────────────────────────────────────────────────────────────────
start(SwitcherWeb, address='0.0.0.0', port=8080, multiple_instance=True, enable_file_cache=True, update_interval=0.08, start_browser=True)