# Example effect
import moviepy
import providad
import providad.asset
import moviepy.editor as mpe
import scipy

from moviepy import editor


class imgFadeInOut:
    def __init__(self, duration, solid_duration):
        self.duration = duration
        self.solid_duration = solid_duration

    def name(self):
        return "imgFadeInOut"

    def apply(self, clip, startTime, asset):
        image_clip = moviepy.video.VideoClip.ImageClip(asset.url, duration=self.duration)

        mask = mpe.ColorClip(image_clip.size, color=1, ismask=True, duration=image_clip.duration)
        mask = moviepy.video.fx.all.fadein(mask, (self.duration-self.solid_duration)/2, initial_color=0)
        mask = moviepy.video.fx.all.fadeout(mask, (self.duration - self.solid_duration) / 2, final_color=0)

        image_clip = image_clip.set_mask(mask)

        image_clip = image_clip.set_pos(('center', 'center'))
        image_clip = image_clip.set_start(startTime)
        return editor.CompositeVideoClip([clip, image_clip])


class imgBaseTransform:
    def __init__(self, duration):
        self.duration = duration

    def zoom_function(self, t):
        return 0.5

    def name(self):
        return "imgBaseTransform"

    def translate_function(self, t):
        return 0.5, 0.5

    def apply(self, clip, startTime, asset):
        image_clip = moviepy.video.VideoClip.ImageClip(asset.url, duration=self.duration)

        leftmost = -image_clip.size[0]
        rightmost = clip.size[0]
        topmost = -image_clip.size[1]
        bottommost = clip.size[1]

        image_clip = moviepy.video.fx.all.resize(image_clip, newsize=lambda t: self.zoom_function(t))

        def unnormalize(pos):
            if isinstance(pos[0], str):
                return pos
            else:
                return leftmost+(rightmost - leftmost) * pos[0], topmost+(bottommost - topmost) * pos[1]

        image_clip = image_clip.set_start(startTime)
        ret = editor.CompositeVideoClip([clip, image_clip.set_pos(lambda t: unnormalize(self.translate_function(t)))])
        overtime = startTime + image_clip.duration
        return ret.set_duration(clip.duration if clip.duration > overtime else overtime)


class imgZoom(imgBaseTransform):
    def __init__(self, duration, solid_duration):
        self.duration = duration
        self.solid_duration = solid_duration

    def name(self):
        return "imgZoom"

    def zoom_function(self, t):
        half = (self.duration - self.solid_duration) / 2
        ret = 1
        if t == 0:
            return 1

        if t < half:
            ret = t / half
        elif t > self.duration - half:
            ret = 1 - ((t - (self.duration - half)) / half)
        else:
            ret = 1.0

        return ret + 0.01

    def translate_function(self, t):
        return 'center', 'center'


class imgSpiral(imgBaseTransform):
    def __init__(self, duration, loops):
        self.duration = duration
        self.loops = loops

    def name(self):
        return "imgSpiral"

    def zoom_function(self, t):
        return ((t/self.duration)) + 0.01

    def translate_function(self, t):
        normal_time = (t/self.duration)
        radius = 0.5*normal_time
        x = scipy.sin(normal_time*self.loops)*radius
        y = scipy.cos(normal_time*self.loops)*radius
        x += 0.5
        y += 0.5
        return x, y

class imgSlide(imgBaseTransform):
    def __init__(self, horizontal, vertical):
        self.horizontal_speed = horizontal
        self.vertical_speed = vertical

    def zoom_function(self, t):
        return 1.0

    def name(self):
        return "imgSlide"

    def translate_function(self, t):
        ratio = self.horizontal_speed/self.vertical_speed
        x = t/self.duration

        if(ratio <= 1):
            return x, x*ratio
        else:
            return x*(1/ratio), x

    def apply(self, clip, startTime, asset):
        hor_dur = clip.size[0] / self.horizontal_speed
        ver_dur = clip.size[1] / self.vertical_speed

        if hor_dur > ver_dur:
            self.duration = hor_dur
        else:
            self.duration = ver_dur

        return super(imgSlide, self).apply(clip, startTime, asset)


class imgBackground:
    def name(self):
        return "imgBackground"

    def apply(self, clip, startTime, asset):
        image_clip = moviepy.video.VideoClip.ImageClip(asset.url, duration=clip.duration-startTime)

        image_clip = moviepy.video.fx.all.resize(image_clip, newsize=clip.size)

        image_clip = image_clip.set_start(startTime)
        return editor.CompositeVideoClip([clip, image_clip])
