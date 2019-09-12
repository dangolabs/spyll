#!/usr/bin/env python
from .spyll import *
import logging
logging.getLogger(__name__).info("Made using Spyll")
__author__="Tinos Psomadakis"
__copyright__="Copyright (c) 2019 Tinos Psomadakis"
__credits__ = [""]
__version__ = "0.11"
__maintainer__ = "Tinos Psomadakis"
__email__ = "me@hellotinos.com"
__status__ = "Alpha"

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



    """




    )

def changelog():
    print(
    '''
    Currently running spyll Version 0.11
    Changelog:

    - Hello World
    - Added core features
    - Added search feature
    - Added count feature
    - Added read feature
    - Added write feature
    - Added help command
    - Added changelog command

    Version 0.11

    - Improved README
    - Made the file opening as + to avoid errors

    '''
    )
