import shutil,os,sys#,send2trash

if __name__ == '__main__':
	os.chdir("./test folder")
	# Create a copy of file1 named file2. If file already exist, nothing happens
	shutil.copy('eggs.txt','eggs2.txt')
	shutil.copy('eggs.txt','eggs3.txt')

	os.chdir('../')
	#Copy entire folder and subfiles
	#shutil.copytree('./test folder','./copied test folder')

	# move file from folder to another folder
	try:
		shutil.move('./test folder/eggs3.txt', './move folder')
	except:
		print("The file already exist in the folder")

	#Move file and rename
	shutil.move('./test folder/eggs2.txt','./move folder/eggs2_moved.txt')

	shutil.copytree('./test folder','./delete this folder')
	# Delete a single file in a folder
	os.unlink('./delete this folder/eggs.txt')
	os.unlink('./delete this folder/eggs3.txt')
	# Delete the empty folder
	os.rmdir('./delete this folder')

	shutil.copytree('./test folder','./delete this folder and its content')
	# Delete the folder and the content
	shutil.rmtree('./delete this folder and its content')

	# When deleting files, be sure to run it with prints the first time
	# to see which files that would be deleted
	os.chdir('./test folder')
	for filename in os.listdir():
		if filename.endswith('.txt'):
			#os.unlink(filename)
			print(filename+' will be deleted')

	# -------------send2trash-------------
	# baconFile = open('bacon.txt', 'a') # creates the file
	# baconFile.write('Bacon is not a vegetable.')
	# baconFile.close()
	# send2trash.send2trash('bacon.txt')

	# ------------os.walk()----------------
	# Does a three walk of all folders and files in os.walk(PATH)
	for folderName, subfolders, filenames in os.walk('../'):
		print('The current folder is ' + folderName)

		for subfolder in subfolders:
			print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
		for filename in filenames:
			print('FILE INSIDE ' + folderName + ': '+ filename)

		print('')


	# --------------zipfile------------------------
	# exampleZip = zipfile.ZipFile('example.zip')
	# exampleZip.namelist()

	# spamInfo = exampleZip.getinfo('spam.txt')
	# print(spamInfo.file_size())
	# print(spamInfo.compress_size())
	# print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
 #   .compress_size, 2)))

 	# exampleZip.extractall() # Extracts all files to the current directory
 	# exampleZip.extractall('./Extracted folder') # Extracts all files to a folder
 	
 	# compress file to a zip file
 	# newZip = zipfile.ZipFile('new.zip', 'w')
	# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
	
	# exampleZip.close()

	
	sys.exit()
