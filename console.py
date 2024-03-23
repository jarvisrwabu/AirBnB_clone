#!/usr/bin/python3

"""Entry point of the command interpreter.

Assumptions: You can assume arguments are always in the right order
             Each arguments are separated by a space
             A string argument with a space must be between double quote
             The error management starts from the first argument to the last one

"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone."""
    prompt = '(hbnb)' 
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_create(self, model):
        """
        Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: $create <BaseModel>
        
        """
        input_cmd = shlex.split(model)
        if len(input_cmd) == 0:
            print("** class name missing **")
           
            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        else:
            new_model = eval(f"{input_cmd[0]}()")
            storage.save()
            print(new_model.id)
            
    def do_show(self, str_rep):
        """
        Print the string representation of an instance based on the class name and id.
        Usage: $show <class_name> <id>
        
        """
        input_cmd = shlex.split(str_rep)
        if len(input_cmd) == 0:
            print("** class name missing **")
            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")    
            
        elif len(input_cmd) < 2:
            print("** instance id missing **")
          
        else:
            class_name = input_cmd[0]
            instance_id = input_cmd[1]
            with open('file.json', 'r') as file:
                data = json.load(file)
                instance_key = "{}.{}".format(class_name, instance_id)
                
                if instance_key in data:
                    instance_data = data[instance_key]
                    print(f"[{class_name}] ({instance_id}) {instance_data}")
                     
                else:
                    print("** no instance found **")
                     
    def do_destroy(self, dest_arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: $destroy <class_name> <id>
        
        """
        input_cmd = shlex.split(dest_arg)
        
        if len(input_cmd) == 0:
            print("** class name missing **")
            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")    
            
        elif len(input_cmd) < 2:
            print("** instance id missing **")
          
        else:
            objects = storage.all()
            instance_key = "{}.{}".format(input_cmd[0], input_cmd[1]) # Class name and id
            
            if instance_key in objects:
                del objects[instance_key]
                storage.save()
            
            else:
                print("** no instance found **")
            
         
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name. 
        Usage: $all <class_name> or $all 
        
        """
        objects = storage.all()
        input_cmd = shlex.split(arg)
        
        if len(input_cmd) == 0:
            for key, value in objects.items():
                print(str(value)) # The output must be in string representation
                            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")
            
        else:
            for key, value in objects.items():
                if key.split('.')[0] == input_cmd[0]:
                    print(str(value))
                    
                    
    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        usage:  $update <class name> <id> <attribute name> "<attribute value>"
        
        """
        input_cmd = shlex.split(arg)
        
        if len(input_cmd) == 0:
            print("** class name missing **")
            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")
            
        elif len(input_cmd) < 2:
            print("** instance id missing **")
            
        else:
            objects = storage.all()
            instance_key = "{}.{}".format(input_cmd[0], input_cmd[1]) # Class name and id
            
            if instance_key not in objects:
                print("** no instance found **")
                
            elif len(input_cmd) < 3:
                print("** attribute name missing **")
                
            elif len(input_cmd) < 4:
                print("** value missing **")
                
            else:
                my_obj = objects[instance_key]
                
                attribute_name = input_cmd[2]
                attribute_value = input_cmd[3]
                
                try:
                    attribute_value = eval(attribute_value)
                    
                except:
                    pass
                
                setattr(my_obj, attribute_name, attribute_value)
                
                my_obj.save()
                        
                            
    def do_EOF(self, line):
        """Implement EOF."""
        return True
    
    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()