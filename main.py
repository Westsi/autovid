"""
Main run for ADV
"""
import json
from utils.VideoInstance import Video
from utils.CreateMovie import CreateMovie
from utils.ParseScript import parse_script
from utils.upload_video import upload_video
from utils.messages.CreateMessage import discordMsg
import PIL
from PIL import Image
import random

movie = CreateMovie()

def load_script(script_path):
    script = open(script_path)
    lines = script.readlines()
    script.close()
    return lines

def load_script_json(json_path):
    script_json = open(json_path)
    data = json.load(script_json)
    script_json.close()
    return data

def make_link_truths(s, sj):
    for lineObj in s:
        try:
            tf = sj["links"][lineObj["lineNum"]]
        except KeyError as e:
            sj["links"][lineObj["lineNum"]] = False
        except Exception as e:
            print(f"There was an unhandled exception. Program will crash soon. {e}")
    
    return sj

def make_message_images(s, sj):
    fltr = []
    for lineObj in s:
        uname = lineObj["userSpeaking"]
        pfppath = sj["users"][uname]["pfp"]
        pfp = Image.open(f"pfp/{pfppath}")
        pfp = pfp.resize([128, 128])
        image = discordMsg(pfp, lineObj["content"].strip(), lineObj["userSpeaking"], isLink=sj["links"][lineObj["lineNum"]], color=sj["users"][uname]["rolecolour"])
        lineno = str(lineObj["lineNum"])
        image.save(f"genned_images/{lineno}.png")
        fltr.append(lineno)
    return fltr

script = load_script("template_script.txt")
script_json = load_script_json("template_script_metadata.json")

script_parsed, moral, users = parse_script(script)

script_json = make_link_truths(script_parsed, script_json)

file_list = make_message_images(script_parsed, script_json)

movie.CreateMP4(script_parsed, moral, users, script_json, file_list)

video_data = {
            "file": "video.mp4",
            "title": f"{moral} - Discord Storytime!",
            "description": "Discord Video with funny morals and plots\nby CHANNEL NAME",
            "keywords":"posts,discord,compilation,memes,morals,soyousee",
            "privacyStatus":"public"
    }
upload_video(video_data)
