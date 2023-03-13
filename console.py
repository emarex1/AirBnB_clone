#!/usr/bin/python3
"""
Command interpreter module
"""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        object_key = class_name + "." + instance_id
        if object_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[object_key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        object_key = class_name + "." + instance_id
        if object_key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[object_key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = shlex.split(arg)
        all_objects = storage.all()

        if not args:
            print([str(all_objects[obj]) for obj in all_objects])
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        objects_list = [str(all_objects[obj]) for obj in all_objects
                        if class_name in obj]
        print(objects_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist)

