#!/usr/bin/python3
"""Console module."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances."""
        objects = storage.all()

        if arg:
            args = shlex.split(arg)
            class_name = args[0]

            if class_name != "BaseModel":
                print("** class doesn't exist **")
                return

            print([str(obj) for obj in objects.values()
                   if obj.__class__.__name__ == class_name])
            return

        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Update an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attribute = args[2]
        value = args[3]

        if hasattr(obj, attribute):
            current_value = getattr(obj, attribute)

            if isinstance(current_value, int):
                value = int(value)
            elif isinstance(current_value, float):
                value = float(value)

        setattr(obj, attribute, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
