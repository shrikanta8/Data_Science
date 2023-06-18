import os, sys   # helps in collapsing the path
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__),'..')))




def course():
    print("this is my course details")

