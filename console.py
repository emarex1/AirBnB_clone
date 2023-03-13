#!/usr/bin/python3
"""This module defines a command interpreter"""
import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line + ENTER is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and saves it to JSON file"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_inst = classes[arg]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        objs = storage.all()
        if not arg:
            print([str(objs[k]) for k in objs])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(objs[k]) for k in objs if args[0] in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_val = args[3]
                setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_val))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
