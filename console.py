#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = '(hbnb) '
    __my_classes = {"BaseModel",
                    "User"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits Console"""
        return True

    def emptyline(self):
        """Overwrites the emptyline command"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
 and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id Usage: `$ show <class name> <id>
         """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + "." + tokens[1]) not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[tokens[0] + "." + tokens[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name is missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[tokens[0] + '.' + tokens[1]]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name
        Usage: '$ all <class name>'
        """
        obj_dict = models.storage.all()
        selected = []
        if len(arg) != 0:
            if arg not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            else:
                for each in obj_dict.values():
                    if arg == each.__class__.__name__:
                        selected.append(each.__str__())
                print(selected)
        else:
            for each in obj_dict.values():
                selected.append(each.__str__())
            print(selected.__str__())

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change to the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                obj = obj_dict[tokens[0] + '.' + tokens[1]]
                if tokens[2] in obj.__class__.__dict__.keys():
                    v_type = type(obj.__class__.__dict__[tokens[2]])
                    obj.__dict__[tokens[2]] = (v_type(tokens[3]))
                else:
                    obj.__dict__[tokens[2]] = tokens[3]
                models.storage.save()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
