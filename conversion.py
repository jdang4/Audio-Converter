#!/usr/bin/python3.6

import os, shutil, glob
import getpass
import subprocess

def check_for_existing_file(basename, dest) :
	file_exists = 0
	for file in os.listdir(dest) :
		if basename == file :
			file_exists += 0
		else :
			file_exists += 1

	return file_exists


def transferFiles(filetype, src, dest) :
	files = glob.iglob(os.path.join(src, "*." + str(filetype)))
	for file in files :
		if os.path.isfile(file) :
			baseFile = os.path.basename(file)
			baseFolder = os.path.basename(dest)

			path, dirs, files3 = next(os.walk(dest))
			file_count = len(files3)

			result = check_for_existing_file(baseFile, dest)

			if (result == file_count) :
				shutil.move(file, dest)
				print (baseFile + " has been transferred to " + baseFolder)

			else :
				print ("File already exists")
				print (baseFile + " will be deleted")
				os.remove(file)


def convert(original, new, src, dest) :
	files = glob.iglob(os.path.join(src, "*." + str(original)));

	for file in files :
		if os.path.isfile(file) :
			original_base = os.path.basename(file)
			print("Converting " + original_base)
			newFile = file[:-3] + str(new)
			new_base = os.path.basename(newFile)
			#print(new_base)

			for filename in src :
				if "'" in filename :
					os.rename(filename, filename.replace("'", ""))

			
			file_string = str(file).replace(' ', '\ ').replace('(', '\(').replace(')', '\)').replace("'", "\\'" )
			newFile_string = str(newFile).replace(' ', '\ ').replace('(', '\(').replace(')', '\)').replace("'", "\\'")

			command = "ffmpeg -i " + str(file_string) + ' ' + str(newFile_string)
			result = os.system(command)

			if (result != 0) :
				shutil.move(file, '/home/jonathan/Music/Missed')

			if (os.path.isfile(newFile)):
				print(original_base + " has successfully been converted to " + new_base)
				transferFiles("mp3", src, dest)
			else :
				print("Something went wrong with moving the file")


def main() :
	usr_name = getpass.getuser()
	path = '/home/' + usr_name + '/Music'
	audio_file_types = ["mp3", "wma", "m4a", "wav", "ogg", "aac", "ac3"]

	print(", ".join(['{0}'.format(audio) for audio in audio_file_types]));

	
	while True :
		original_audioFile = str(input("Enter the audio file type you want to change: "))

		if original_audioFile not in audio_file_types :
			print ("Invalid audio file type")
			continue
		else :
			custom_directory = os.path.dirname(path + '/' + original_audioFile + '/')
			path2 = path + '/' + original_audioFile
			if not os.path.exists(custom_directory) : 
				os.makedirs(custom_directory)
				print("Created a directory to hold all the " + original_audioFile + " files")

			break

	while True :
		new_audioFile = input("Enter the aduio file type you want to change to: ")
		if new_audioFile not in audio_file_types :
			print ("Invalid audio file type")
			continue
		else :
			custom_directory_2 = os.path.dirname(path + '/' + new_audioFile + '/')
			path3 = path + '/' + new_audioFile

			if not os.path.exists(custom_directory_2) : 
				os.makedirs(custom_directory_2)
				print("Created a directory to hold all the new " + new_audioFile + " files")

			break

	missed_directory = os.path.dirname(path + '/Missed/')
	
	if not os.path.exists(missed_directory) :
		os.makedirs(missed_directory)
		print("Created a directory to hold all the files that weren't converted")

	transferFiles(original_audioFile, path, path2)

	convert(original_audioFile, new_audioFile, path2, path3)

	paths, dirs, missed_files = next(os.walk(missed_directory))
	missed_file_count = len(missed_files)

	paths, dirs, wma_files = next(os.walk(path2))
	wma_file_count = len(wma_files)

	successful_conversions = int(wma_file_count) - int(missed_file_count)

	print("\nSuccess Rate: " + str(successful_conversions) + "/" + str(wma_file_count))

#convert('wma', 'mp3', '/home/jonathan/Music/wma', '/home/jonathan/Music/mp3')

#transferFiles("wma", '/home/jonathan/Music', '/home/jonathan/Music/wma')

main()
