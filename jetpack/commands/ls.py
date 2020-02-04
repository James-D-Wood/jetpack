from ..jetfile import Jetfile

def main():
    '''Prints all projects known by Jetpack'''
    jetfile = Jetfile()
    projects = jetfile.all()
    if projects:
        print("Projects known to Jetpack")
        print("-------------------------")
        for project in projects:
            print(project)
    else:
        print("No projects have been added to Jetpack. Add a project by running `jetpack launch -n [project name]`.")