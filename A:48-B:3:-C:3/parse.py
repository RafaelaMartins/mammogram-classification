from sys import argv, stdin, stdout
import numpy as np 

class Parser:
    """Parse command line arguments."""
    def __init__(self):
       self.option = {}
       
    def read_args(self, args):
        
        if args[0].startswith('-'):
            if args[0] == '-s' or args[0] == 'step':
                self.option['epoch'] = int(args[1])
                #self.option['size']  = int(args[2])
                self.option['path']  = str(args[2])
                return self.option
            elif args[0] == '-n' or args[0] == '-none':
                self.option['epoch'] = int(args[1])
                #self.option['size'] = int(args[2])
                self.option['path'] = False
                return self.option
        return None
    
    def read_args_validation(self,args):
        if args[0].startswith('-'):
            if args[0] == '-v':
                print("passou -v")
                self.option['image_path'] = str(args[1])
                #self.option['size'] = int(args[2]) 
                return self.option
            return None
