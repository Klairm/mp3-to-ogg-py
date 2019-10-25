from pydub import AudioSegment
import sys,os,glob

def mp3_to_ogg(path):

	mp3list = os.chdir(path)
	if os.path.isdir('./export'):
		pass
	else:
		os.mkdir("export")
	if glob.glob("*.mp3"):
		pass
	else:
		raise FileNotFoundError("MP3 file not found")
		exit(1)
	for i in os.listdir():
	    name, ext = os.path.splitext(i)
	    if ext == ".mp3":
	    	if os.path.isfile(f'./export/{name}.ogg'):
	    		print(f'{name} is already exported as ogg file, skipping...')
	    	else:	
		    	print(f"Exporting {name} ...")
		    	sound = AudioSegment.from_mp3(name+ext)
		    	sound.export(f"{path}/export/{name}.ogg", format="ogg")

print("Write the path where the mp3 files are for export them as ogg")
path = input('MP3 Path -> ')		    	
try:
	mp3_to_ogg(path)
except FileNotFoundError as NoMP3File:
	print(NoMP3File)	
else:
	print("Program finalized")
		
		
		