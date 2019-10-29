from pydub import AudioSegment
import sys,os,glob
from exporters import *
from progress.spinner import Spinner

def mp3_to_ogg(path):
	mp3list = os.chdir(path) 
	folder = os.getcwd()[-6:] # Getting the last 6 characters 
	if os.path.isdir('./export'):
		pass
	if folder == 'export': # If the last 6 characters are export it will skip 
		pass
	else:
		os.mkdir('export')
	if glob.glob('*.mp3'): # Checking if there's any mp3 file
		pass
	else:
		raise FileNotFoundError('Mp3 file not found') # If not, it will show an error message and exit the program
		exit(1)
	for i in os.listdir():
		if os.path.isdir(i):
			print("Skipping directories...")
		else:			
			name, ext = os.path.splitext(i)
			if ext ==".mp3":
				print(f'{name} is already exported as mp3 file, skipping...')
			elif ext !='.ogg':
				print("Skipping not ogg files...")
			else:
				mp3_ogg(name,ext,path,folder)

def ogg_to_mp3(path):
	ogglsit = os.chdir(path) 
	folder = os.getcwd()[-6:] # Getting the last 6 characters 
	if os.path.isdir('./export'):
		pass
	if folder == 'export': # If the last 6 characters are export it will skip 
		pass
	else:
		os.mkdir('export')
	if glob.glob('*.ogg'):
		pass
	else:
		raise FileNotFoundError('OGG file not found')
		exit(1)
	for i in os.listdir():
		if os.path.isdir(i):
			print("Skipping directories...")
		else:			
			name, ext = os.path.splitext(i)
			if ext ==".mp3":
				print(f'{name} is already exported as mp3 file, skipping...')
			elif ext !='.ogg':
				print("Skipping not ogg files...")
			else:
				ogg_mp3(name,ext,path,folder)

		    	
try:
	while True:
		print('===============')
		print('Audio converter')
		print('===============')
		print('[1] Mp3 to Ogg')
		print('[2] Ogg to Mp3')
		print('[3] Exit')
		print('===============')
		op = int(input('Select an option -> '))
		print('===============')
		if op==1:
			print("Write the path where the mp3 files are for export them as ogg")
			path = input('MP3 Path -> ')
			mp3_to_ogg(path)
		elif op==2:
			print("Write the path where the ogg files are for export them as mp3")
			path = input('OGG Path -> ')
			ogg_to_mp3(path)
		elif op==3:
			break

	
except FileNotFoundError as NoMP3File:
	print(NoMP3File)	
else:
	print("Program finalized")
		
		
		