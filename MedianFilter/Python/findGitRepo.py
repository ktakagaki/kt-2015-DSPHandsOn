# -*- coding: utf-8 -*-
"""
Spyder Editor

Finding the Git repository path.
"""
import os 

def findGitRepo(path):
    if os.path.exists(path + '\\.git') == True:   #Check if \\.git path exists
        return path + '\\.git'
    elif path == 'C:\\':                          # if directory = root directory, print that no .git repository was found
        print 'No \.git repository found'
        
    else:
        return findGitRepo(os.path.abspath(os.path.join(path, os.pardir))) # call the function findGitRepo and set the path to the parent directory
         