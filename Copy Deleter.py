import os, shutil, sys

folder = os.path.abspath(" ".join(sys.argv[1:]))

for folder, subs, fileNames in os.walk(folder):

		for fileName in fileNames:
			if (fileName.endswith('Copy.lnk') or fileName.endswith('Copy.docx') or fileName.endswith('Copy.pdf')):
				fileName = os.path.abspath(fileName)
				print("Deleting file:", fileName)
				os.unlink(os.path.join(folder, os.path.basename(fileName)))

		for sub in subs:
			if (sub.endswith('Copy')):
				sub = os.path.abspath(sub)
				print("Deleting folder:", sub)
				shutil.rmtree(os.path.join(folder, os.path.basename(sub)))
