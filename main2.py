# English and Portugues expressions (300 expressions)

import sys, random, time, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
from kivy.uix.image import Image
from kivy.core.window import Window   ##############
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

# Platform importation
from kivy.utils import platform

# Check if Platform is Android and import necessary modules
if platform == "android":
	from jnius import cast
	from jnius import autoclass
	
# global count
number = NumericProperty()
	
# Home page class 
class Expressions(Screen):
    def __init__(self, *args, **kwargs):
        super(Expressions, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.on_touch_up,0.1)
		
    def on_touch_up(self, touch):
        self.tilesource =random.choice(expTest)

# Drop down class
class CustomDropDown(DropDown):
    pass
	
# Game class 	
class GameScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(GameScreen, self).__init__(*args, **kwargs)
        self.principalsound = SoundLoader.load('gameSound.ogg')
		Clock.schedule_interval(self.up,0.3)
		
		# invoking drop down class OOP
		self.drop_down = CustomDropDown()
     
	# Play sound method 
    def toplaysound(self,*args):
        if self.principalsound:
            self.principalsound.play()
			
	# Stop sound method
    def tostopplaysound(self,*args):
        if self.principalsound:
            self.principalsound.stop()
			
	# Calling the app class OOP. This method control the music from the app class 		
    def startmusicstop(self,*args):
        self.ap =XPRESSIONZzz()
        return self.ap.stopsound()
		
	# Up random selection	
    def up(self, *args):
        self.tilesource3 =random.choice(exp)
		
        self.characterlabel =("button/b1.png")
        self.image =('background/b4.jpg')
        self.bubblelabel =('bub/j1.png')
       
		# Loud sounds
        self.s1 = SoundLoader.load('claps3.mp3')
        self.s2 = SoundLoader.load("boo3.mp3")

        self.ingles5 =("[b]Hyper[/b]")
        self.portugues5 =("[b]Muito animado[/b]")
		
	# clear sons and daughters when they aren't needed 
    def out_butts(self, widget):
        self.layout.clear_widgets(children=None)
        self.layout26.clear_widgets(children=None)
		
	# count and start
    def count_start(self,*args):
        self.mylabel =self.ids["label"]
        self.nl +=1
        self.mylabel.text ="[b][i]ARE YOU READY??[/b][/i]"
        
	# Automation function. Don't stop untill I ask you to stop 
    def nextAutomation(self, *args): 
        Clock.schedule_interval(partial(self.for_out_butts), self.t)
        Clock.schedule_interval(partial(self.to_play_to_pause),self.t) 
        return self.gameButtons()#,self.texts()
		
	# Play and pause function
    def to_play_to_pause(self, *args):
        if self.principalsound:
            self.principalsound.play()
        Clock.schedule_once(self.gameButtons,0)
        Clock.schedule_once(self.texts, 0)
        Clock.unschedule(self.lab1ontext)
        Clock.unschedule(self.flab2)
        self.layout201.clear_widgets(children=None)
    
	# Calls no children function
    def for_out_butts(self, *args):
        Clock.schedule_once(self.out_butts,0)
		
	# Movement property function 1
    def formove_1(self,*args):
        Clock.schedule_once(self.move2,0)
		
	# Movement property function 1
    def formove_2(self,*args):
        Clock.schedule_once(self.move,0)
		
	# Record touches property function	
    def on_touch_up(self, *args):
        pass
           
   # Let the player know that he is doing well function 
    def cheer(self, *args):########
        self.mylabel.text =random.choice(self.praise)+"\n"+ random.choice(self.jokepraise)
		
    # approval sound 1 function 
    def sound_1(self, *args):		
        if self.s1:
            self.s1.play()
	
    def boo(self, *args):########
        self.mylabel.text =random.choice(self.wrong)+"\n"+ random.choice(self.bootext) 
		
    def sound_2(self,*args):
        if self.s2:
            self.s2.play()
			
    def start(self): ## start timing
        Clock.schedule_interval(self.increment_time, 1)
			
    def increment_time(self, *args):  ## Timing
        if (self.number ==209) and (self.numba1  <=39): 
            Clock.schedule_once(self.timeup4level1,0) 
        elif (self.number ==415) and (self.numba1  <=79): 
            Clock.schedule_once(self.timeup4level1,0)
        elif (self.number ==620) and (self.numba1  <=119): 
            Clock.schedule_once(self.timeup4level1,0)
        self.number +=1
		
    def stop (self, *args):
        Clock.unschedule(self.increment_time)
	
    def score(self, interval):
        self.number4 +=5
		
    def scoreminus(self, interval):
        self.number4 -=1
		
	# Levels intelligence partial schedule
    def f_l2(self, *args):
        Clock.schedule_interval(self.level_2,self.t)
    def f_l3(self, *args):
        Clock.schedule_interval(self.level_3,self.t)
		
    def numba(self, *args):
        self.numba1 +=1
		
    def lab1_on_text(self, *args):
        self.layout201 = self.ids["grid_layout201"]
        self.load2 = Label(text='')# Just to position the widget
        self.load2.size_hint= None,None
        self.load2.size=(self.width/3, self.height/3)
        self.load2.pos_hint={'center_x': .50, 'center_y': .90}
        self.layout201.add_widget(self.load2)#
        self.load2.font_size = 100
        
        self.indexlab1 +=1
        self.load2.text = str(self.indexlab1)
	
        self.load3 = Label(text='')# Just to position the widget
        self.load3.size_hint= None,None
        self.load3.size=(self.width/3, self.height/3)
        self.layout201.add_widget(self.load3)#

        if self.indexlab1 ==9:
            self.mylabel.text="[b][i]LET'S GO...!![/b][/i]"
        
    def flab1(self, *args):
        Clock.schedule_interval(self.flab2,1)
    def flab2(self, *args):
        Clock.schedule_once(self.lab1ontext,0)
		
    # Animation method 
    def gameButtons(self, *args): # Dynamic buttons and labels starts heres
        self.anim3 = Animation(x=200, y=0) + Animation(size=(self.width/2.7, self.height/3), duration=1.5)
        self.anim3.repeat = True
        self.anim3.start(self.btn3)
		
        self.anim4 = Animation(x=30, y=0) + Animation(size=(self.width/2.7, self.height/3), duration=1.5)
        self.anim4.repeat = True
        self.anim4.start(self.btn4)
        return
		
		#Animation properties 1
    def move(self,*args):
        self.btn1.pos_hint={'x':.6, 'y':.40}
        self.btn2.pos_hint={'x':.02, 'y':.40}
       
	   #Animation properties 2
    def move2(self,*args):
        if self.move2:
            self.btn1.pos_hint={'x':.11, 'y':.52}
            self.btn2.pos_hint={'x':.52, 'y':.52}
			
        #Animation properties 3  
    def moveimage(self,*args):
        if self.moveimage:
            self.btn3.pos_hint={'center_y': .20}
            self.btn4.pos_hint={'center_y': .20}
		
		#Text method
    def texts(self, *args):
        if self.index1 >=21:
            return True
        self.mylabel.text =self.ingles1[self.index1] 
        self.mylabel.texture_update()
        self.index1 += 1
        return 
	
    # Level 2 method	
    def level_2(self, *args):########
        if self.index2 >=21:
            return True
        self.mylabel.text =self.ingles2[self.index2]
        self.mylabel.texture_update()
        self.index2 += 1
        return
			
	# Level 3 method
    def level_3(self, *args):########
        if self.index3 >=21:
            return True
        self.mylabel.text =self.ingles3[self.index3]
        self.mylabel.texture_update()
        self.index3 += 1
        return
		
	# Level 4 method
    def level_4(self, *args):########
        if self.index4 >=21:
            return True
        self.mylabel.text =self.ingles4[self.index4]
        self.mylabel.texture_update()
        self.index4 += 1
        return

	# Time control method
    def timeup4level1(self, *args): # Instructions Popup function
        content = BoxLayout(orientation="vertical", spacing =10)
        content.add_widget(Label(text="TIME UP!",text_size=(150, None),line_height=1, markup=True, font_size=14))
        mybuttonl1 = Button(text="[b]Try\nAgain[/b]",font_size =15, size_hint=(None,None)
		,markup=True,size=(60,55), pos_hint={'center_x': 0.5}, height=40)
        content.add_widget(mybuttonl1)
        show_popup = Popup(content = content,              
            title = "      TIME UP!! ",     
            auto_dismiss = False,         
            size_hint = (.9, .8))
        mybuttonl1.bind(on_release=show_popup.dismiss)
        mybuttonl1.bind(on_release=self.notime)
        show_popup.open()
		
# Screens control class
class ToMangeScreen(ScreenManager):
    def __init__(self, *args, **kwargs):
        super(ToMangeScreen, self).__init__(*args, **kwargs)

class XPRESSIONZzz(App):
    number = NumericProperty()
    sound = SoundLoader.load('gameSound/game_game.ogg')
	
	# Play instructions method
    def instructions(self, *args): 
        infotext="""[b]PLAY INSTRUCTIONS!\n
                 2. XPRESSIONZ e muito simples
				 de usar[/b]"""
        
    # High score method
    def highScore(self, args): 
        pass 
		
     # about xpressionz
    def about(self, *args):
       pass
        
	# sound control from the app level
    def stopsound(self,*args):
        if self.sound:
            self.sound.stop()

    def build(self):
        if self.sound:
            self.sound.play() ######
        return ToMangeScreen()

    def on_pause(self):
        return True

    def on_resume(self):
        pass	
		
if __name__ =="__main__":
    XPRESSIONZzz().run()
