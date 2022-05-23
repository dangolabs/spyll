# -*- coding: utf-8 -*-       /

"""
Spyll Library
~~~~~~~~~~~~~~~~~~~~~

Spyll is a file management library built for python that focuses on providing simple, understandable and easy to use functionality.
Example usage:

   >>> import spyll
   >>> file_written = spyll.write("Example.txt", "Hello World!")
   >>> spyll.read("Example.txt") if file_written else None
   'Hello World!'

"""
from .spyll import *
__author__ = "Dango Labs"
__copyright__ = "Copyright (c) 2019 pTinosq"
__credits__ = [""]
__version__ = "1.2.3"
__maintainer__ = "pTinosq"
__email__ = "info@dangolabs.com"
__status__ = "Release"
__license__ = "GNU General Public License v3.0"
__description__ = "A Python libary for fast, simple and effective file handling."
__download_url__ = "https://pypi.org/project/spyll/"
__keywords__ = ["file", "management", "rename", "search", "directory"]
__install_requires__ = [""]
__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]
