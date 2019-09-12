<h1>Spyll 0.11</h1>

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

<h2>spyll.count(file, text)</h2>

<p>Counts the amount of time a value appears in a text file</p>
<h3> Example </h3>
```python
import spyll

value = spyll.count(file="./folder/romeo_and_juliet.txt", "?")
print(f"There are {value} questions in Romeo and Juliet!")
```

<h1>To do</h1>
<ul>
<li>Appending files</li>
<li>Creating files</li>
<li>Deleting files</li>
<li>Renaming files</li>
<li>Add to website</li>
<li>Get file information</li>
<li>Copy/Paste file</li>
</ul>
