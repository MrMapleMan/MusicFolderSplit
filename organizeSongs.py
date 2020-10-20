import os
import sys
import eyed3

numArgs = len(sys.argv)
if numArgs > 0:
  mainDir = sys.argv[1]
else:
  print('Please provide directory as first argument.')
  sys.exit()

dirPath, dirNames, fileNames = os.walk(mainDir)

# Walk through all files (not folders)
for i in fileNames:
# For every song:
  
  fullPath = os.path.join(mainDir, i)
  
  # Check metadata to find artist  
  audiofile = eyed3.load(fullPath)
  newPath = os.path.join(mainDir, audiofile.tag.artist)
  
  # Create artist folder if needed
  try:
    os.mkdir(newPath)
  except:
    pass
  
  # Move song into folder
  os.rename(fullPath, os.path.join(newPath, i))
