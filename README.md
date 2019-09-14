<h1>Spyll 1.0</h1>

<h2>Welcome</h2>
<p>Spyll is an Open-Source Python package that is aimed at making txt file management easier. It was made in python 3.7 and should work on all versions higher than 3.0.</p>

<h2>Help commands</h2>
<ul>
<li>spyll.help()</li>
<li>spyll.changelog()</li>
</ul>

<h1>Features</h1>

<h2>spyll.write(file, text, split)</h2>

<p>Writes to a specified text file with optional split which is only available for tuples and lists.</p>
<h3> Example </h3>

```python
import spyll

spyll.write(file="./folder/Hello_World.txt",text="This is a new text file!")
spyll.write(file="./folder/Goodbye_World.txt", text=["First Line", "Second Line", "Third Line"], split="\n")
```

<h2>spyll.read(file)</h2>

<p>Simply reads text file to string</p>
<h3> Example </h3>

```python
import spyll

text = spyll.read(file="./folder/Hello_World.txt")
print(text)
```

<h2>spyll.search(file, text)</h2>

<p>Checks to see if the file contains the specified value</p>
<h3> Example </h3>

```python
import spyll

if spyll.search(file="./folder/Hello_World.txt", "username"):
  print("Contains Username!")
```

<h1>Why use Spyll?</h1>

<h2>Spyll was created to make managing python text files much easier to work with. It's purpose is to turn multi-line code snippets into a single function.<h2>

<h2> Comparisons </h2>

<h3> Normal Python </h3>

```python

sentence = ["Wow, ","I","Love","Python"]
text=""
with open("directory_to_file", "w") as file:
  for i in sentence:
    text+=f"{i} "
  file.write(text)

with open("directory_to_file", "r") as file:
  value = file.read()

with open("directory_to_file", "r") as file:
  value = file.read()
  if "username" in file:
    print("Username spotted!")

with open("directory_to_file", "r") as file:
  text = file.read()
  number = text.count("username")
```

<h3> Using Spyll </h3>

```python
import spyll

sentence = ["Wow, ","I","Love","Python"]
spyll.write("directory_to_file", sentence, " ")

value = spyll.read("directory_to_file")

if spyll.search("directory_to_file", "username"):
  print("Username spotted!")

number = spyll.count("directory_to_file","username")

```

<h1> Contribute! </h1>

[GitHub Page](https://github.com/pTinosq/spyll)
