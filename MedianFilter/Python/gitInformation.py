# -*- coding: utf-8 -*-
"""
This package allows you to add information to your Ipython notebook, if you're working in a git repository.
It is usefull if you want to verify the notebook version.
This package is collecting all information by its own, so you don't need to set any repository path.
You also can check the information of other notebooks, when you set the path by your own.
Requierments: local git repository
              git python package installed
"""
import os as __os
import datetime as __datetime
import sys as __sys
from git import Repo as __Repo


def __getFileDirectory():
    fileDirectory = __os.path.dirname(__os.path.realpath('__file__')) #Set the file directoy  as directory of the currently used file
    return fileDirectory

def __findGitRepo(fileDirectory):
    if __os.path.exists(fileDirectory + '\\.git') == True:  # Check if the file path is a git repository path
        return fileDirectory + '\\.git' 
    else:
        parentPath = __os.path.abspath(__os.path.join(fileDirectory, __os.pardir))  #set the directory as parent directory
        if fileDirectory == parentPath:        # if directory is the root directory, no git repository exists
            print 'No \.git repository found'
            return None
        else:
            return __findGitRepo(parentPath)   #repeat the process until you find a git repository or the directory is the root directory
            


def printInformation( filePath = '' ):
    """Plot important information about your notebook: Date, used Python version, git directory, git commit SHA, current remote and current branch"""
    if( filePath == '' ):
        __printInformationImpl( __findGitRepo(__getFileDirectory()), 'this notebook' )
    else:
        __printInformationImpl( __findGitRepo(filePath), filePath )

def __printInformationImpl(filePath, targetString):
    mylist = []  
    today = __datetime.date.today() 
    mylist.append(today) #append the Date into a list, so it can be printed 
    repo = __Repo(filePath) #represents your git repository path
    print( 'Information about ' + targetString )
    print( '============================================================' )
    print( "Date: " +  str(mylist[0])  )
    print( 'Python Version: ' + __sys.version )
    print( 'Git directory: ' + __findGitRepo(filePath) )
    print( 'Current git SHA: ' +  repo.commit().hexsha )
    print( 'Current remote: ' + str( repo.remote() ) )
    print( 'Current branch: ' + str(repo.active_branch)  )


### with the following functions you are able to print single informations about the notebook and repository###

def printCurrentBranch(filePath = ''):
    """Plot information about the current git branch"""
    if( filePath == '' ):
        __currentBranchImpl( __findGitRepo(__getFileDirectory()) )
    else:
        __currentBranchImpl( __findGitRepo(filePath) )
        
def __currentBranchImpl(filePath):
    repo = __Repo(filePath)
    print( 'Current branch: ' + str(repo.active_branch)  ) # print the current branch
        
    
    
def printCurrentGitSHA(filePath = ''):
    """Plot information about the current git commit hash"""
    if( filePath == '' ):
        __currentGitSHAImpl( __findGitRepo(__getFileDirectory()) )
    else:
        __currentGitSHAImpl( __findGitRepo(filePath) )
    
def __currentGitSHAImpl(filePath):
     repo = __Repo(filePath)
     print( 'Current git SHA: ' +  repo.commit().hexsha ) #print the current git commit hash code


        
def printCurrentRemote(filePath = ''):
    """Plot information about the current git remote"""
    if( filePath == '' ):
        __currentRemoteImpl( __findGitRepo(__getFileDirectory()) )
    else:
        __currentRemoteImpl( __findGitRepo(filePath) )

def __currentRemoteImpl(filePath):
    repo = __Repo(filePath)
    print( 'Current remote: ' + str( repo.remote() ) ) #print the current remote of your repository
    


def printGitDirectory(filePath = ''):
    """Plot information about the current git directory"""
    if( filePath == '' ):
        __gitDirectoryImpl( __findGitRepo(__getFileDirectory()) )
    else:
        __gitDirectoryImpl( __findGitRepo(filePath) )
    
def __gitDirectoryImpl(filePath):
    print( 'Git directory: ' + __findGitRepo(filePath))  # print the directory, where the repository is saved