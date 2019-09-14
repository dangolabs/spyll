import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spyll",
    version="1.0",
    author="Tinos Psomadakis",
    author_email="me@hellotinos.com",
    description="Spyll is an Open-Source Python package that is aimed at making txt file management easier. It was made in python 3.7 and should work on all versions higher than 3.0.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hellotinos.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
            ],
)
