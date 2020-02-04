'''
This file should handle the main control flow of the logic for this program.
'''

# 3rd party libraries
import click

# Standard libraries
import sys
import os

# Our modules
from .commands import launch, ls, remove

# this is the base group for our utility, all commands will be attached to @cli
@click.group()
def cli():
    '''Jetpack, a utility for getting started quicker.'''
    os.environ['JETFILE_PATH'] = '/Users/james/Documents/james/jetpack/jetpack/jetfile'

#jetpack launch [-n] project
@cli.command('launch') 
@click.option('-n', is_flag=True, help = 'Skip search and create a new project in current directory.')
@click.argument('project')
def run_launch(n, project):
    '''Finds or creates new project and launches VSCode editor'''
    print()
    launch.main(new=n, project=project)  # offload complex logic to module 
    print()

#jetpack list
@cli.command('ls')
def run_ls():
    '''Lists all projects known by Jetpack'''
    print()
    ls.main()
    print() 

#jetpack remove project
@cli.command('remove') 
@click.argument('project')
def run_remove(project):
    '''Removes a project from Jetpack'''
    print()
    remove.main(project)
    print()

