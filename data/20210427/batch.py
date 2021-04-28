import glob
import os

for file in glob.glob("*.png") :
    os.system("dvc add " + file)

