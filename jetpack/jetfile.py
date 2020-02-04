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

    def all(self):
        '''prints all projects in Jetfile'''
        projects = []
        f = open(self.path)
        for line in f:
            line = line.rstrip()
            entry = line.split("/")
            project = entry[-1]
            projects.append(project)
        f.close()
        return projects

    def remove(self, project):
        removed = False
        with open(self.path) as f:
            lines = f.readlines()
        with open(self.path, 'w') as f:
            for line in lines:
                line = line.rstrip()
                entry = line.split("/")
                filename = entry[-1]
                if filename.lower() != project.lower():
                    f.write(line)
                else:
                    removed = True
        return removed