from moviepy.editor import *
import providad
import providad.asset
import numpy as np
from moviepy import editor

class LetterBase:
    def moveLetters(self, letters):
        return [ letter[0].set_pos(self.move(letter[1],i,len(letters))) for i,letter in enumerate(letters)]

    def move(self, screenpos,i,nletters):
        pass

class LetterMove(LetterBase):
    def __init__(self, duration, percentageFromLeft=20, percentageFromTop=50, fontSize=60, txtcolor='red', bgcolor='transparent', font='Amiri-Bold'):
        self.duration = duration
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        self.top= percentageFromTop
        self.left= percentageFromLeft

    def apply(self, clip, startTime, asset):
        w,h = clip.size
        screensize = clip.size
        letters= []
        sumwidth=0
        for a in range(0, len(asset.value)):
            tmp = []
            tmp.append( TextClip(asset.value[a], color=self.txtcolor, bg_color=self.bgcolor, font=self.font, fontsize=self.fontSize) )
            tmp.append( (self.left * (w/100) + sumwidth , self.top * (h/100) ) )
            sumwidth += tmp[0].w +5
            letters.append(tmp)

        newVideos= CompositeVideoClip( (self.moveLetters(letters)), size = screensize)
        newVideos = newVideos.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, newVideos])