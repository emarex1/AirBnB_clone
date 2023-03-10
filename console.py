#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line should not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

