# -*- coding: utf-8 -*-
"""
This package allows you to add information to your Ipython notebook, if you're working in a git repository.
It is usefull if you want to verify the notebook version.
This package is collecting all information by its own, so you don't need to set any repository path.
You also can check the information of other notebooks, when you set the path by your own.
Requierments: *local git repository
              *git python package installed
"""
import os as _os
import datetime as _datetime
import sys as _sys
from git import Repo as _Repo


def _getFileDirectory():
    #Set the file directoy  as directory of the currently used file
    fileDirectory = _os.path.dirname(_os.path.realpath('_file_')) 
    return fileDirectory

def _findGitRepo(fileDirectory):
    #Check if the file path is a git repository path
    if _os.path.exists(fileDirectory + '\\.git') == True:  
        return fileDirectory + '\\.git' 
    else:
        #set the directory as parent directory
        parentPath = _os.path.abspath(_os.path.join(fileDirectory, _os.pardir))
        #if directory is the root directory, no git repository exists
        if fileDirectory == parentPath:        
            print 'No \.git repository found'
            return None
        else:
            #repeat the process until you find a git repository or the directory is the root directory
            return _findGitRepo(parentPath)   
            


def printInformation( filePath = '' ):
    """Plot important information about your notebook: Date, used Python version, git directory, git commit SHA, current remote and current branch"""
    if( filePath == '' ):
        _printInformationImpl( _findGitRepo(_getFileDirectory()), 'this notebook' )
    else:
        _printInformationImpl( _findGitRepo(filePath), filePath )

def _printInformationImpl(filePath, targetString):
    mylist = []  
    today = _datetime.date.today()
    #append the Date into a list, so it can be printed
    mylist.append(today) 
    #represents your git repository path
    repo = _Repo(filePath) 
    print( 'Information about ' + targetString )
    print( '============================================================' )
    print( "Date: " +  str(mylist[0])  )
    print( 'Python Version: ' + _sys.version )
    print( 'Git directory: ' + _findGitRepo(filePath) )
    print( 'Current git SHA: ' +  repo.commit().hexsha )
    print( 'Current remote: ' + str( repo.remote() ) )
    print( 'Current branch: ' + str(repo.active_branch)  )


### with the following functions you are able to print single informations about the notebook and repository###

def printCurrentBranch(filePath = ''):
    """Plot information about the current git branch"""
    if( filePath == '' ):
        _currentBranchImpl( _findGitRepo(_getFileDirectory()) )
    else:
        _currentBranchImpl( _findGitRepo(filePath) )
        
def _currentBranchImpl(filePath):
    repo = _Repo(filePath)
    #print current branch
    print( 'Current branch: ' + str(repo.active_branch)  )
        
    
    
def printCurrentGitSHA(filePath = ''):
    """Plot information about the current git commit hash"""
    if( filePath == '' ):
        _currentGitSHAImpl( _findGitRepo(_getFileDirectory()) )
    else:
        _currentGitSHAImpl( _findGitRepo(filePath) )
    
def _currentGitSHAImpl(filePath):
     repo = _Repo(filePath)
     #print current git commit hash code
     print( 'Current git SHA: ' +  repo.commit().hexsha ) 

        
def printCurrentRemote(filePath = ''):
    """Plot information about the current git remote"""
    if( filePath == '' ):
        _currentRemoteImpl( _findGitRepo(_getFileDirectory()) )
    else:
        _currentRemoteImpl( _findGitRepo(filePath) )

def _currentRemoteImpl(filePath):
    repo = _Repo(filePath)
    #print current remote of your repository
    print( 'Current remote: ' + str( repo.remote() ) ) 
    


def printGitDirectory(filePath = ''):
    """Plot information about the current git directory"""
    if( filePath == '' ):
        _gitDirectoryImpl( _findGitRepo(_getFileDirectory()) )
    else:
        _gitDirectoryImpl( _findGitRepo(filePath) )
    
def _gitDirectoryImpl(filePath):
    #print directory, where the repository is saved
    print( 'Git directory: ' + _findGitRepo(filePath))  