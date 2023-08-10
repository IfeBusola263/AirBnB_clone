#!/usr/bin/env python3
"""A program that contains the entry point of
the command line interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Creates a class that handles the cmd console"""
    prompt = "(hbnb) "
    __models = ["BaseModel", "Place", "User",
                "State", "City", "Amenity", "Review"]

    def do_create(self, line):
        """ Creates a new instance of a basemodel and saves it to the
        json file """

        if not line:
            print("** class name missing **")
        elif line in self.__models:
            if line == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)
            elif line == "User":
                obj = User()
                obj.save()
                print(obj.id)
            elif line == "State":
                obj = State()
                obj.save()
                print(obj.id)
            elif line == "City":
                obj = City()
                obj.save()
                print(obj.id)
            elif line == "Amenity":
                obj = User()
                obj.save()
                print(obj.id)
            else:
                obj = Review()
                obj.save()
                print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ The show method displays the string representation of
        a basemodel based on class name and id """

        # Argument in args is a tuple, taking all argument
        # as a string, this is why you have to split it
        # by the delimiter used to enter the arguments
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()

        for key, value in inst_dict.items():
            if obj_id == value.id:
                print(value)
                return

        print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes the instance of a base model in the storage and
        updates the value in the json file."""
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()
        to_del = ""

        for key, value in inst_dict.items():
            if obj_id == value.id:
                to_del = key

        if to_del != "":
            del inst_dict[to_del]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints are the BaseModel instances in the storage
        as a list."""

        args = args.split()

        if args and args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        storage.reload()
        inst_dict = storage.all()
        rep_list = []
        for key, value in inst_dict.items():
            rep_list.append(str(value))

        print(rep_list)

    def do_update(self, args):
        """ Updates the attributes of an instance in the json file."""
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        # confirm if the id exists
        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()
        id_check = ""

        for key, value in inst_dict.items():
            if obj_id == value.id:

                # id_check will hold the key to the
                # basemodel object with the given id, if it exists
                id_check = key

        if id_check == "":
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        # retrieve the value of the key from the id_check
        # implement the update
        bm_obj = inst_dict[id_check]

        if args[2] in bm_obj.to_dict():
            bm_obj.__dict__[args[2]] = str(args[3])
        else:
            bm_obj.__dict__[args[2]] = str(args[3])

        bm_obj.save()

    def emptyline(self):
        """ The emptyline method called when an empty line
        is entered """
        return ""

    def do_quit(self, command):
        """Functionality for quitting the console"""
        return True

    def do_EOF(self, command):
        """Exit gracefully when end of file is signaled """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
