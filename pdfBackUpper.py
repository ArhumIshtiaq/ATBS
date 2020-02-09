import os, sys, shutil

def searchExt(folder):
	folder = os.path.abspath(folder)
	for fileName in os.listdir(folder):
		if (fileName.endswith('.pdf')):
			fileName = os.path.abspath(fileName)
			print(fileName)
			shutil.copy(fileName, 'C:\\Users\\momo\\Desktop\\pdfBackUp')

searchExt("C:\\Users\\momo\\Desktop")