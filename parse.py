from sys import argv, stdin, stdout
import numpy as np 

class Parser:
    """Parse command line arguments."""
    def __init__(self):
       self._option = {}
       
    def read_args(self, args):
        
        if args[0].startswith('-'):
            if args[0] == '-s' or args[0] == 'step':
                self._option['epoch'] = int(args[1])
                self._option['size']  = int(args[2])
                self._option['path']  = str(args[3])
                return self._option
            elif args[0] == '-n' or args[0] == '-none':
                self._option['epoch'] = int(args[1])
                self._option['size'] = int(args[2])
                self._option['path'] = False
                return self._option
        return None
    
    def read_args_validation(self,args):
        if args[0].startswith('-'):
            if args[0] == '-v':
                print("passou -v")
                self._option['image_path'] = str(args[1])
                self._option['size'] = int(args[2]) 
                return self._option
            return None
