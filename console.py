"""Entry point of the command interpreter."""
from models.base_model import BaseModel
from models import storage
import cmd
import shlex
import json
class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone."""
    prompt = '(hbnb)' 
    valid_classes = ["BaseModel"]

    def do_create(self, model):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        input_cmd = shlex.split(model)
        if len(input_cmd) == 0:
            print("** class name missing **")
           
            
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
            
    def do_show(self, str_rep):
        """Print the string representation of an instance based on the class name and id."""
        input_cmd = shlex.split(str_rep)
        if len(input_cmd) == 0:
            print("** class name missing **")
            
        elif len(input_cmd) == 1:
            print("** instance id missing **")
        
        elif input_cmd[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        else:
            class_name = input_cmd[0]
            instance_id = input_cmd[1]
            with open('file.json', 'r') as file:
                data = json.load(file)
                instance_key = "{}.{}".format(class_name, instance_id)
                
                if instance_key in data:
                    instance_data = data[instance_key]
                    print(f"[{class_name}] ({instance_id}) {instance_data}")
                     
    def do_EOF(self, line):
        """Implement EOF."""
        return True
    
    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()