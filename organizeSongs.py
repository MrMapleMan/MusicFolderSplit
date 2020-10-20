import os
import sys

numArgs = len(sys.argv)
if numArgs > 0:
  mainDir = sys.argv[1]
else:
  print('Please provide directory as first argument.')
  sys.exit()

# Walk through all files (not folders)

# For every song:
  # Check metadata to find artist
  # Create artist folder if needed
  # Move song into folder
