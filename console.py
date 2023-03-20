#!/usr/bin/env python3
"""Module for the HBNB console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Class for the HBNB console"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line method"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

