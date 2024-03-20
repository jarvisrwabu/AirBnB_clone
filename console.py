"""Entry point of the command interpreter."""
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone."""
    prompt = '(hbnb)'

    def do_create(self, model):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if model == 'BaseModel':
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
            
        
        elif not model:
            print("** class name missing **")
        
        else:
            print("** class doesn't exist **")
            
         
        
    def do_EOF(self, line):
        """Implement EOF."""
        return True
    
    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
