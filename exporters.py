import time
from time import sleep
from pydub import AudioSegment
from progress.spinner import PixelSpinner

def converter(name,ext,path,form):
	with PixelSpinner(f'{name} Processing... ') as bar:
		for i in range(100):
			sleep(0.03)
			bar.next()
		sound = AudioSegment.from_mp3(name+ext)
		sound.export(f"{path}/export/{name}.{form}", format=form)
