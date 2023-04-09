import pygame as pg
pg.init()
class mus():
    def __init__(self, file):
        self.file = file
    def start(file, num_of_times):
        global filedata
        filedata = pg.mixer.Sound(file).play(num_of_times)
    def pause():
        global filedata
        filedata.pause()
    def unpause():
        global filedata
        filedata.unpause()
    def stop():
        global filedata
        filedata.stop()
