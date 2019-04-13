import providad
import moviepy
import numpy as np
from moviepy import editor

class TextPosition:
    def __init__(self, duration, horizontal="center", vertical="center", fontSize=60, txtcolor='blue', bgcolor='transparent', font='Courier'):
        self.duration = duration
        self.horizontal = horizontal
        self.vertical = vertical
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        text_clip = moviepy.video.VideoClip.TextClip(asset.value, fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
        text_clip = text_clip.set_pos((self.horizontal, self.vertical))
        text_clip = text_clip.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, text_clip])

    def name(self):
        return "TextPosition"

class TextMoveLeftTest:
    def __init__(self, duration, fontSize=60, txtcolor='blue', bgcolor='transparent', font='Courier'):
        self.duration = duration
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        w,h = moviesize = clip.size
        text = moviepy.video.VideoClip.TextClip(asset.value, fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
        text_clip = text.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)), max(5*h/6,int(100*t))) )
        text_clip = text_clip.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, text_clip])

    def name(self):
        return "TextMoveLeftTest"


class TextsShowWords:
    def __init__(self, duration, horizontal="center", vertical="center", fontSize=60, txtcolor='white', bgcolor='black', font='Courier'):
        self.duration = duration
        self.fontSize = fontSize
        self.horizontal = horizontal
        self.vertical = vertical
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        w,h = moviesize = clip.size
        words= asset.value.split(" ");
        text_clips= []
        itemDur= self.duration / len(words)
        newclip = clip
        for i in range(0, len(words)):
            text_clip = moviepy.video.VideoClip.TextClip(words[i], fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
            text_clip = text_clip.set_pos((self.horizontal, self.vertical))
            text_clip= text_clip.set_start(startTime + i *itemDur ).set_duration(itemDur-0.1)
            newclip= editor.CompositeVideoClip([newclip, text_clip])
        return newclip

    def name(self):
        return "TextsShowWords"

class TextMove_From_LU_To_RD:
    def __init__(self, duration, horizontal_speed, vertical_speed, fontSize=60, txtcolor='blue', bgcolor='transparent', font='Courier'):
        self.vspeed = vertical_speed
        self.hspeed = horizontal_speed
        self.duration = duration
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        rightmost, bottommost = clip.size
        leftmost = 0
        topmost = 0
        text = moviepy.video.VideoClip.TextClip(asset.value, fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
        text_clip = text.set_pos( lambda t: (leftmost+(t*self.hspeed), topmost+(t*self.vspeed)) )
        text_clip = text_clip.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, text_clip])

    def name(self):
        return "TextMove_From_LU_To_RD"

class TextMove_From_RD_To_LU:
    def __init__(self, duration, horizontal_speed, vertical_speed, fontSize=60, txtcolor='blue', bgcolor='transparent', font='Courier'):
        self.vspeed = vertical_speed
        self.hspeed = horizontal_speed
        self.duration = duration
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        leftmost, topmost = clip.size
        rightmost = 0
        bottommost = 0
        text = moviepy.video.VideoClip.TextClip(asset.value, fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
        tw,th= text.size
        leftmost -= tw /2
        topmost -= th /2
        text_clip = text.set_pos( lambda t: (leftmost-(t*self.hspeed), topmost-(t*self.vspeed)) )
        text_clip = text_clip.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, text_clip])

    def name(self):
        return "TextMove_From_RD_To_LU"

class TextMove_From_LD_To_RU:
    def __init__(self, duration, horizontal_speed, vertical_speed, fontSize=60, txtcolor='blue', bgcolor='transparent', font='Courier'):
        self.vspeed = vertical_speed
        self.hspeed = horizontal_speed
        self.duration = duration
        self.fontSize = fontSize
        self.txtcolor= txtcolor
        self.bgcolor= bgcolor
        self.font=  font
        
    def apply(self, clip, startTime, asset):
        rightmost, topmost = clip.size
        leftmost = 0
        bottommost = 0
        text = moviepy.video.VideoClip.TextClip(asset.value, fontsize=self.fontSize, color=self.txtcolor, bg_color=self.bgcolor, font=self.font )
        tw,th= text.size
        leftmost += tw /2
        topmost -= th /2
        text_clip = text.set_pos( lambda t: (leftmost+(t*self.hspeed), topmost-(t*self.vspeed)) )
        text_clip = text_clip.set_start(startTime).set_duration(self.duration)
        return editor.CompositeVideoClip([clip, text_clip])

    def name(self):
        return "TextMove_From_LD_To_RU"