import moviepy.editor as mpe
import operator
import providad
import providad.asset_effects_Text
import providad.asset_effects_img


########################################
# Transforms jozocode into movie file
# params:
#      code:       input jozocode
########################################
def create_video(header, declarations, effects, output, music="music_1.mp3"):
    # header = ((800, 600), 10.0)
    # declaration = ("pizdec", asset.Image("img/02.jpg"))
    # effect = (0.5, 1, "pizdec", asset_effects.Fade(0.5, False))

    clip = mpe.ColorClip(header[0], color=(0, 0, 0), duration=header[1])
    clip.fps = header[2]

    all_assets = dict()
    for decl in declarations:
        if(decl[0] in all_assets):
            raise Exception("Asset IDs must be unique!")
        else:
            all_assets[decl[0]] = decl[1]

    effects.sort(key=operator.itemgetter(1, 0))

    for effect in effects:
        clip = effect[3].apply(clip, effect[0], all_assets[effect[2]])

    audio = mpe.AudioFileClip(music)
    audio = audio.set_duration(clip.duration + 0.5)
    clip = clip.set_audio(audio)
    clip.write_videofile(output)


