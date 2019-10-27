import time
from time import sleep
from pydub import AudioSegment
from progress.spinner import PixelSpinner
def progress_bar(name,ext,path):
	with PixelSpinner(f'{name} Processing... ') as bar:
		sound = AudioSegment.from_mp3(name+ext)
		sound.export(f"{path}/export/{name}.ogg", format="ogg")
		for i in range(100):
			sleep(0.06)
			bar.next()