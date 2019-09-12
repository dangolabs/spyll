import os

def read(file=None, split=None):

    os.chdir(os.getcwd())

    if file == None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.read(file=\"directory_to_file\")")
        return

    file = str(file)
    with open(file,"r+") as file:
        text = file.read()
        if split == None or split == False:
            pass

        else:
            text = text.split(str(split))


    return text

def search(file=None, text=None):

    os.chdir(os.getcwd())

    if file == None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.search(file=\"directory_to_file\")")
        return

    if text == None:
        raise ValueError("You haven't specified any text to search for. Usage:\n spyll.search(file='directory_to_file', text='Hello World')")
        return

    file = str(file)
    with open(file,"r+") as file:
        read_text = file.read()
        if text in read_text:
            return True
        else:
            return False

def count(file=None, text=None):

    os.chdir(os.getcwd())

    if file == None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.count(file=\"directory_to_file\")")
        return

    if text == None:
        raise ValueError("You haven't specified any text to count. Usage:\n spyll.count(file='directory_to_file', text=' ')")
        return

    file = str(file)
    with open(file,"r+") as file:
        read_text = file.read()
        return read_text.count(text)


def write(file=None, text=None, split=None):

    os.chdir(os.getcwd())

    file = str(file)

    if file == None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.write(file=\"directory_to_file\")")
        return

    if text == None:
        raise ValueError("You haven't specified any text. Usage:\n spyll.write(file='directory_to_file', text='Hello World')")
        return

    is_list=False

    if type(text) == list or type(text) == tuple:
        is_list=True

    if split != None and is_list != True:
        raise ValueError("You can only split inputs of type list. Usage: spyll.write(file='directory.txt', text=['hello','world'], split='\\n')")
        return

    if split != None and is_list:
        newtext = ""
        for i in text:
            if len(text) - (text.index(i)) == 1:
                newtext+=f"{i}"
            else:
                newtext+=f"{i}{split}"
        text=newtext

    if split == None and is_list:
        newtext = ""
        for i in text:
            if len(text) - (text.index(i)) == 1:
                newtext+=f"{i}"
            else:
                newtext+=f"{i} "
        text=newtext



    with open(file,"w+") as file:
        file.write(text)
