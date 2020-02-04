from ..jetfile import Jetfile
import os 

def main():
    jetfile = Jetfile()
    cwd = os.path.abspath(os.getcwd())
    jetfile.add(cwd)