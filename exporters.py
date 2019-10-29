import time
from time import sleep
from pydub import AudioSegment
from progress.spinner import PixelSpinner

def mp3_ogg(name,ext,path,folder):
	with PixelSpinner(f'{name} Processing... ') as bar:
		for i in range(100):
			sleep(0.06)
			bar.next()
		sound = AudioSegment.from_ogg(name+ext)
		if folder == 'export':
			sound.export(f"{path}/{name}.ogg", format="ogg")
		else:
			sound.export(f"{path}/export/{name}.ogg", format="ogg")

def ogg_mp3(name,ext,path,folder):
	with PixelSpinner(f'{name} Processing... ') as bar:
		for i in range(100):
			sleep(0.06)
			bar.next()
		sound = AudioSegment.from_ogg(name+ext)
		if folder == 'export':
			sound.export(f"{path}/{name}.mp3", format="mp3")
		else:
			sound.export(f"{path}/export/{name}.mp3", format="mp3")