'''
This file should handle the main control flow of the logic for this program.
'''

# 3rd party libraries
import click

# Standard libraries
import sys

# Our modules
from .commands import launch

# this is the base group for our utility, all commands will be attached to @cli
@click.group()
def cli():
    pass

# jetpack launch -p project_name 
@cli.command('launch') 
@click.option('-p', required = True, help = 'project_name')
def run_launch(p):
    launch.main(project_name = p)  # offload complex logic to module    