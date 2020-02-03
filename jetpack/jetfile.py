import os

class Jetfile:

    def __init__(self):
        self.path = os.environ['JETFILE_PATH'] 

    def find(self, project):
        f = open(self.path)
        for line in f:
            line = line.rstrip()
            entry = line.split("/")
            filename = entry[-1]
            if filename.lower() == project.lower():
                return line
        f.close()

    def add(self, project_path):
        f = open(self.path, 'a')
        f.write(project_path)
        f.write('\n')
        f.close()
    