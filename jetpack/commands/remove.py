from ..jetfile import Jetfile

def main(project):
    '''Removes indicated project from Jetpack'''
    jetfile = Jetfile()
    if jetfile.remove(project):
        print("Removed {} from Jetpack.".format(project))
    else:
        print("No project named {} found.".format(project))
