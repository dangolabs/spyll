import os


def read(file=None, split=None):
    """Reads text file

    Parameters
    ----------
    file : str
        The file location
    split : str, optional
        The character to split the file contents. Default is None.

    Returns
    -------
    str
        The file contents

    OR
    list of str (Only if split is not None)
        The file contents split by the split parameter
    """
    os.chdir(os.getcwd())
    if file is None:
        raise FileNotFoundError("File not specified.")

    with open(str(file), "r+") as file:
        content = file.read()
        if split is None or split is False:
            pass

        else:
            content = content.split(str(split))

    return content


def contains(haystack=None, needle=None):
    """Checks if a file (haystack) contains a specified string (needle). It's like looking for a needle in a haystack!

    Parameters
    ----------
    haystack : str
        The file location
    text : str
        The text to search for in the file.

    Returns
    -------
    bool
        True if the file contains the text, otherwise False.
    """
    os.chdir(os.getcwd())

    if haystack is None:
        raise FileNotFoundError("File not specified.")

    if needle is None:
        raise ValueError("No needle specified.")

    with open(str(haystack), "r+") as haystack:
        read_text = haystack.read()
        if needle in read_text:
            return True
        else:
            return False


def count(file=None, text=None):
    """Counts occurances of a string in a file.

    Parameters
    ----------
    file : str
        The file location
    text : str, optional
        The text to search for in the file. If None, it will return the amount of characters in the file.

    Returns
    -------
    int
        The number of times the text occurs in the file.
    """
    os.chdir(os.getcwd())

    if file is None:
        raise FileNotFoundError("File not specified.")

    with open(str(file), "r+") as file:
        if text is None:
            return len(file.read())
        else:
            return file.read().count(text)


def write(file=None, content=None, split=""):
    """Writes content to a text file.

    Parameters
    ----------
    file : str
        The file location
    content : str, list, or tuple, optional
        The text to write to the file. If None, an empty file will be created.
    split : str, optional
        The character to split the file contents. Default is "".

    Returns
    -------
    bool
        True if the file was created, otherwise False.
    """
    os.chdir(os.getcwd())

    if file is None:
        raise FileNotFoundError("File not specified.")

    if content is None:
        with open(file, "w+") as file:
            file.write("")
            return True

    if type(content) is str:
        with open(file, "w+") as file:
            file.write(content)
            return True

    if type(content) is list or type(content) is tuple:
        with open(file, "w+") as file:
            for i in content:
                file.write(f"{i}{split}")
            return True

    return False


def rename(file=None, name=None):
    """Renames a text file.

    Parameters
    ----------
    file : str
        The file location
    name : str
        The new name for the file.

    Returns
    -------
    str
        The new file location.
    """
    if "." not in file:
        raise ValueError("Invalid file - no file type found.")

    if "/" in name:
        raise ValueError("Invalid name (Includes /)")

    if "/" in file:
        file_path = file.split("/")[:-1]
        file_path = "/".join(file_path)

    else:
        file_path = os.getcwd().replace("\\", "/")

    file_type = file.split(".")[-1]
    os.rename(file, f"{file_path}/{name}.{file_type}")


def searchdir(directory=None, file=None):
    """Searches a directory for a file.

    Parameters
    ----------
    file : str
        The file name to search for.
    directory : str
        The directory to search.

    Returns
    -------
    bool
        True if the file is found. False if it is not.
    """
    if directory is None:
        raise ValueError("Directory not specified.")

    if file is None:
        raise ValueError("File not specified.")

    directoryList = os.listdir(directory)

    return file in directoryList
