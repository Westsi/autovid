from moviepy.editor import *
import random
import os

# dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# def GetDaySuffix(day):
#     if day == 1 or day == 21 or day == 31:
#         return "st"
#     elif day == 2 or day == 22:
#         return "nd"
#     elif day == 3 or day == 23:
#         return "rd"
#     else:
#         return "th"

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
music_path = os.path.join(dir_path, "Music/")


class CreateMovie():

    @classmethod
    def CreateMP4(cls, lines, moral, users, json, clip_path_list, bgv_color = (0,0,0)):


        # ColorClip((1920,1080), color=bgv_color, duration=(len(clip_path_list)*3)+6).write_videofile("bgv.mp4", fps=24)

        clips = []
        for file in clip_path_list:
            # if file == "40":
            #     continue
            fpath = f"genned_images/{file}.png"
            clip = ImageSequenceClip(
                [fpath], durations=[3])
            clips.append(clip)

        # After we have out clip.
        clip = concatenate_videoclips(clips, "compose", bg_color=None, padding=0)

        # Hack to fix getting extra frame errors??
        #clip = clip.subclip(t_end=(clip.duration - 1.0))

        boom_sound_lines = []
        for s in json['sounds']:
            boom_sound_lines.append(s)

        color = 'WhiteSmoke'
        text_clips = []
        notification_sounds = []
        ixThree = 0
        for i, line in enumerate(lines):
            ixThree = i*3
            if str(line['lineNum']) in boom_sound_lines:
                boom = AudioFileClip(os.path.join(music_path, f"boom.mp3"))
                boom = boom.set_start((0, (i*3)))
                boom = boom.set_duration(1)
                boom = boom.volumex(.4)
                notification_sounds.append(boom)
            else:
                notification = AudioFileClip(
                    os.path.join(music_path, f"notification.mp3"))
                notification = notification.set_start((0, (i*3)))
                notification_sounds.append(notification)

        txt = TextClip("MORAL", font='Verdana', fontsize=100, color=color)
        txt = txt.on_color(col_opacity=.3)
        txt = txt.set_position(("center", "center"))
        txt = txt.set_start((0, ixThree + 3))  # (min, s)
        txt = txt.set_duration(3)
        txt = txt.crossfadeout(0.5)
        text_clips.append(txt)

        txt = TextClip(moral.strip(), font='Verdana', fontsize=60, color=color)
        txt = txt.on_color(col_opacity=.3)
        txt = txt.set_position(("center", "center"))
        txt = txt.set_start((0, ixThree + 6))  # (min, s)
        txt = txt.set_duration(3)
        txt = txt.crossfadein(0.5)
        txt = txt.crossfadeout(0.5)
        text_clips.append(txt)

        music_file = os.path.join(
            music_path, f"music{random.randint(0,4)}.mp3")
        music = AudioFileClip(music_file)
        music = music.set_start((0, 0))
        music = music.volumex(.4)
        mus_duration = ixThree + 7
        if mus_duration > music.duration:
            music_file = os.path.join(
            music_path, f"music{random.randint(0,4)}.mp3")
            music2 = AudioFileClip(music_file)
            music2 = music2.set_start((0, mus_duration))
            music2 = music2.volumex(.4)
            music2.set_duration(mus_duration - music.duration)
        else:
            music = music.set_duration(mus_duration)

        new_audioclip = CompositeAudioClip([music]+notification_sounds)
        clip.write_videofile("video_clips.mp4", fps=24)

        clip = VideoFileClip("video_clips.mp4", audio=False)
        clip = clip.set_position(("center", "center"))
        clip = clip.resize(2)
        bgc = VideoFileClip("bgv.mp4", audio=False)
        clip = CompositeVideoClip([bgc] + [clip] + text_clips, use_bgclip=True)
        clip.audio = new_audioclip
        clip.write_videofile("video.mp4", fps=24)

        # if os.path.exists(os.path.join(dir_path, "video_clips.mp4")):
        #     os.remove(os.path.join(dir_path, "video_clips.mp4"))
        # else:
        #     print(os.path.join(dir_path, "video_clips.mp4"))


if __name__ == '__main__':
    print(TextClip.list('color'))
