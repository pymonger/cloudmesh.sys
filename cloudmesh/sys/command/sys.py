"""
The sys command to manage the cmd5 distribution
"""
from __future__ import print_function

from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.sys.manage import Command, Git, Version


class SysCommand(PluginCommand):
    """
    The system command
    """

    # noinspection PyUnusedLocal
    @command
    def do_sys(self, args, arguments):
        """
        ::

          Usage:
                sys git commit MESSAGE
                sys pypi upload
                sys command generate NAME
                sys version VERSION

          This command does some useful things.

          Arguments:
              MESSAGE   the message to commit 
              NAME      the command to generate
              VERSION  the version number

          Options:
              -f      specify the file

          Description:      
              cms sys command generate my
                This requires that you have checked out 
                
                ./cloudmesh.common
                ./cloudmesh.cmd5
                ./cloudmesh.sys
                
                When you execute in . this command
                will generate a sample directory tree for
                the command 'my'.
                
                You can than modify 
              
                cloudmesh.my/cloudmesh/my/command/my.py
                
                to define your own cmd5 add on commands.
                You install the command with 
                
                cd cloudmesh.my; pip install .
                
            cms pypi
            cms git
            
                These commands are only to be used by Gregor
                They upload the new versions to pypi
                
                The git command adds a new version and commits
                The upload command uploads the new version to pypi
        """
        print(arguments)

        if arguments.git and arguments.commit:

            msg = arguments.MESSAGE
            Git.commit(msg)

        elif arguments.pypi and arguments.upload:

            Git.upload()

        elif arguments.command and arguments.generate:

            name = arguments.NAME
            Command.generate(name)

        elif arguments.version:

            version = arguments.VERSION
            Version.set(version)
