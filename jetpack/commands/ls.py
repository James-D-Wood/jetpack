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
        print('''No projects have been added to Jetpack.\n
Add an existing directory by running `jetpack add` or create a new project by running `jetpack launch -n [project name]`.
''')