"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""
#CONSTANTS- 
LOG = False
# Imports

# import requests
# x = requests.get('https://jayd719.github.io/sources/file1.txt')

# print(x.text)

class Process:
    
    def checkContains(self, val):
        import psutil
        processes = psutil.process_iter()
        for process in processes:
            if process.name().upper() == val:
                return process
        return None
        

    
    def __init__(self,val):
        self.process = self.checkContains(val.upper())
        val= val.upper()
        
        
                
        
    
    




print(Process('safari').process)