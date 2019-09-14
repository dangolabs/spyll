#!/usr/bin/env python
from .spyll import *
import logging
logging.getLogger(__name__).info("Made using Spyll")
__author__="Tinos Psomadakis"
__copyright__="Copyright (c) 2019 Tinos Psomadakis"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Tinos Psomadakis"
__email__ = "me@hellotinos.com"
__status__ = "Release"

def help():
    print(
    """

    Commands:

    spyll.write(file, text, split)

    file - A string that defines the location of your text file
    text - What you would like to write into the text file. Accepts list, tuple and string format.
    split - Only available for list and tuple. This will determine how each element from the list/tuple will be written.

    Example:

    spyll.write(file="Hello.txt", text=["Hello","World",":)"], split="\n")
    spyll.write(file="Hello.txt", text="Hello World :)")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.read(file, split)

    file - A string that defines the location of your text file
    split - Will split the read text file into whatever string is provided

    Example:

    spyll.read(file="Hello.txt")
    spyll.read(file="Hello.txt", split=" ")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.search(file, text)

    file - A string that defines the location of your text file
    text - The value that you'd like to search for in a text file

    Returns:

    Boolean

    Example:

    spyll.search(file="Hello.txt", "example")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.count(file, text)

    file - A string that defines the location of your text file
    text - The value that you'd like to count in a text file

    Returns:

    Integer

    Example:

    spyll.count(file="Hello.txt", " ")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.rename(file, name)

    file - A string that defines the location of your text file
    name - A string that will define the new name of your text file

    Returns:

    Nothing

    Example:

    spyll.rename(file="Hello.txt", "World")
    spyll.rename(file="Hello.txt", "World.ini")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.searchdir(directory, filetype)

    directory - A string that defines the location of your directory
    filetype - A string that will define the type of file ending to search for in that directory

    Returns:

    List

    Example:

    spyll.searchdir(directory="C:/Users/HelloWorld/Desktop")
    spyll.searchdir(directory="C:/Users/HelloWorld/Desktop/text_files", "txt")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.size(file, total)

    file - A string, tuple or list that defines the location of the file you're checking
    total - An optional boolean that can only be used if you use a list or tuple in the file variable

    Returns:

    List or Integer

    Example:

    spyll.size(file="C:/Users/HelloWorld/Desktop/dogs.txt")
    spyll.size(file=['world.txt','mars.ini','./animals/cows.txt'], total=True)

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.copy(file, directory, extension)

    file - A string that defines the location of the file you're copying
    directory - A string that defines the location you're copying to
    extension - An optional value that will be added to the copied file

    Returns:

    Nothing

    Example:

    spyll.copy("test.txt", "./completed_tests", "_complete")
    spyll.copy("dog.txt", "./favourites")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    spyll.cut(file, directory, extension)

    file - A string that defines the location of the file you're cutting
    directory - A string that defines the location you're cutting to
    extension - An optional value that will be added to the copied file

    Returns:

    Nothing

    Example:

    spyll.cut("test.txt", "./completed_tests", "_complete")
    spyll.cut("dog.txt", "./favourites")

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



    """




    )

def changelog():
    print(
    '''
    Currently running spyll Version 1.0
    Changelog:

    Version 1.0

    - Major update to README to include comaprisons + github link
    - Improved if statements, courtesy of salt rock lamp#0679 over at the Python Discord
    - Added searchdir feature
    - Added rename feature
    - Added size feature
    - Added copy feature
    - Added paste feature

    Version 0.12

    - README formatting errors

    Version 0.11

    - Improved README
    - Made the file opening as + to avoid errors

    Version 0.1

    - Hello World
    - Added core features
    - Added search feature
    - Added count feature
    - Added read feature
    - Added write feature
    - Added help feature
    - Added changelog feature







    '''
    )
