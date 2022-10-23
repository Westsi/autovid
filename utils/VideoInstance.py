import os

class Video:
    def __init__(self, users, output_path = os.getcwd()):
        self.users = users
        self.out_video_path = output_path