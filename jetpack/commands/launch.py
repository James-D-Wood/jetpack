import os
import re
from ..jetfile import Jetfile
from ..exceptions import InputNotWhitelisted


def main(new, project):
    try:
        jetfile = Jetfile()
        if not re.match('\w', project):
            # whitelist param name to disallow any unexpected errors
            raise InputNotWhitelisted("Project names can only contain alphanumeric characters and the underscore character.")
        if new:
            try:
                os.mkdir(project)
                cwd = os.path.abspath(os.getcwd())
                project_path = cwd + "/" + project
                jetfile.add(project_path)
                os.system("code {}".format(project))
            except FileExistsError:
                print("A project with the name {} already exists in this directory".format(project))
            except OSError as e:
                if str(e)[:10] == "[Errno 30]":
                    print("Writing is not allowed in this directory. Failed to create project.")
                else:
                    print(e)
        else:
            result = jetfile.find(project)
            if result:
                # TODO: what to do about missing projects
                os.system("code {}".format(result))
            else:
                print("Entry not in jetfile")
    except InputNotWhitelisted as e:
        print(e)


       
    # else
        # search for project
        # if found
            # open code editor
        # else
            # display error message
    