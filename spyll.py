import os
import shutil

def read(file=None, split=None):

    os.chdir(os.getcwd())

    if file is None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.read(file=\"directory_to_file\")")
        return

    file = str(file)
    with open(file,"r+") as file:
        text = file.read()
        if split is None or split is False:
            pass

        else:
            text = text.split(str(split))


    return text

def search(file=None, text=None):

    os.chdir(os.getcwd())

    if file is None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.search(file=\"directory_to_file\")")
        return

    if text is None:
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

    if file is None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.count(file=\"directory_to_file\")")
        return

    if text is None:
        raise ValueError("You haven't specified any text to count. Usage:\n spyll.count(file='directory_to_file', text=' ')")
        return

    file = str(file)
    with open(file,"r+") as file:
        read_text = file.read()
        return read_text.count(text)

def write(file=None, text=None, split=None):

    os.chdir(os.getcwd())

    file = str(file)

    if file is None:
        raise FileNotFoundError("You haven't specified a file. Usage:\n spyll.write(file=\"directory_to_file\")")
        return

    if text is None:
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

    if split is None and is_list:
        newtext = ""
        for i in text:
            if len(text) - (text.index(i)) == 1:
                newtext+=f"{i}"
            else:
                newtext+=f"{i} "
        text=newtext



    with open(file,"w+") as file:
        file.write(text)

def rename(file=None, name=None):
    SplitFile=file.split(".")
    print(f"{len(SplitFile)} file")
    if len(SplitFile) > 1:
        pass
    else:
        raise ValueError("The file you entered isn't valid. You must include the file. For example, dir/hello/scripts/world.txt")
        return
    SplitName = name.split(".")
    print(f"{len(SplitName)} name")
    if len(SplitName) > 1:
        fileEnding = SplitName[-1]
    else:
        fileEnding = SplitFile[-1]

    if len(name.split(".")) > 1:
        name = name.split(".")[:-1]
        fullname=""
        for i in name:
            if len(name) - (name.index(i)) == 1:
                fullname+=f"{i}"
            else:
                fullname+=f"{i}."
        name=fullname

    newName = f"{name}.{fileEnding}"

    os.rename(file, newName)

def searchdir(directory=None, filetype=None):

    if directory is None:
        raise ValueError("You haven't specified a directory to search in. Usage: spyll.list(directory='directory_here', filetype=None)")
        return


    directoryList = os.listdir(directory)

    if filetype is None:
        new_directoryList = directoryList
    else:
        new_directoryList=[]
        for i in directoryList:
            filename = i.split(".")
            if filename[-1] == filetype:
                new_directoryList.append(i)

    return new_directoryList

def size(file=None, total=None):
    os.chdir(os.getcwd())
    if type(file) == str:
        return os.path.getsize(file)


    if type(file) == list or type(file) == tuple:
        if total is None or total is False:
            sizes=[]
            for i in file:

                sizes.append(os.path.getsize(i))

            return sizes

        elif total is True:
            total_size=0
            for i in file:
                total_size+=os.path.getsize(i)
            return total_size

def copy(file=None, directory=None, extension=None):
    if file is None:
        raise ValueError("You haven't specified a file to copy over. Usage: spyll.copy(file = 'file_directory', directory='directory_here', extension=None)")
        return

    if directory is None:
        raise ValueError("You haven't specified a directory to copy to. Usage: spyll.copy(file = 'file_directory', directory='directory_here', extension=None)")
        return

    if directory[-1] != "/":
        directory+="/"

    if extension is None:
        shutil.copyfile(file, directory)
    else:
        filename = file.split("/")[-1]
        filetype = filename.split(".")[-1]
        filename = filename.split(".")[0:-1]
        newname = ""
        for i in filename:
            if len(filename) - (filename.index(i)) == 1:
                newname+=f"{i}"
            else:
                newname+=f"{i}."
        directory = f"{directory}{newname}{extension}.{filetype}"

        shutil.copyfile(file, directory)

def cut(file=None, directory=None, extension=None):
    if file is None:
        raise ValueError("You haven't specified a file to copy over. Usage: spyll.cut(file = 'file_directory', directory='directory_here', extension=None)")
        return

    if directory is None:
        raise ValueError("You haven't specified a directory to copy to. Usage: spyll.cut(file = 'file_directory', directory='directory_here', extension=None)")
        return

    if directory[-1] != "/":
        directory+="/"

    if extension is None:
        shutil.move (file, directory)
    else:
        filename = file.split("/")[-1]
        filetype = filename.split(".")[-1]
        filename = filename.split(".")[0:-1]
        newname = ""
        for i in filename:
            if len(filename) - (filename.index(i)) == 1:
                newname+=f"{i}"
            else:
                newname+=f"{i}."
        directory = f"{directory}{newname}{extension}.{filetype}"

        shutil.move(file, directory)
