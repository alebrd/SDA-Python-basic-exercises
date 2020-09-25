# Introduction

Welcome to the **Python Fundamentals** module!

During this module you will learn the core concepts of Python programming language. <br>
Many of the covered topics are applicable to other languages like C, C++, C# or Java.

Every part of the theory will be followed by the live coding session
and exercises that should be done individually, with an assistance of the trainer.

Some of the topics that are going to be explained during this module are:
- introduction to the language
- basic data structures
- language elements
- object-oriented programming
- text formatting
- operations on files

## Presentation
Presentation is available under [link.](https://gitlab.com/sda-international/program/python/python-fundamentals/-/wikis/uploads/c8a7e5746b1721a6eed076968539440e/Python_Fundamentals.pdf)

## Materials for Individual Workshop

We prepared exercises in PyCharm with Edu Tool. 

Exercises are available under [this link.](SDA_Python_EN.zip)

Here we prepared instruction, how to install Edu tool in IntelliJ [link.](How_to_add_Edu_tool_to_IntelliJ_PyCharm.pdf)


## Requirements

Before you start make sure that you have downloaded and installed required software:
1. [Python 3.7](https://www.python.org/downloads/)
2. [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)
3. [GIT](https://git-scm.com/downloads)

> Note: If you have trouble installing one of thos packages please consult the guide below or ask your trainer to help you.

> Note: Pycharm Community is not required during first two modules. You can edit files in any text editor you know and like.
 
## Installing Python

### Linux

1. Your best option is to install latest package provided by your distribution. Most popular distributions provide `python3.7` packages in their repositories.
2. For example for Ubuntu: `apt update && apt install python3.7`
3. If your distribution does not package Python 3.7 yet, you’ll have to download from https://www.python.org/downloads/source/ and compile it yourself.
4. Package dependencies vary from distribution to distribution. For Ubuntu `build-essential` `zlib1g-dev` `libncurses5-dev` `libgdbm-dev` `libnss3-dev` `libssl-dev` `libreadline-dev` `libffi-dev` `make` `gcc` `tar` `libsqlite3-dev` `uuid-dev` `curl`
5. General compilation steps are:
    1. Install dependencies
    2. Download `Python-3.7.x.tar.xz`
    3. Unpack it `tar -xf Python-3.7.x`
    4. Enter the newly created directory and run `./configure`
    5. `make`
    6. `make test`
    7. If you already have `python3` on your machine, run `make altinstall`
    8. Else run `make install`
    9. Ensure `pip` has been installed by running `python3.7 -m ensurepip`
6. Ensure installation has gone well by checking version `python3.7` `--``version`

### Windows

1. Download executable installer from https://www.python.org/downloads/windows/
2. Important: check Add to PATH checkbox
3. Run the installer by clicking Install Now
4. Verify installation by running `python3.7` `--``version` in PowerShell

 
# First Steps

1. Prepare **one** place on your computer where you will store all of the files and projects related to the Python course. (HINT: desktop is not a good place for that)
2. Download the project as a zip package (or if you are already familiar with GIT you can use it as well)
3. Unpack project to the prepared directory.
4. Using PyCharm create new project using "Create project from existing sources" - point to the recently unpacked directory.
5. Use default setting during the whole creational process.
6. Wait for a couple of seconds as PyCharm has to refresh the directory structure and all of the dependencies.
7. You are ready to go!

> Note: You can run doctests on all files by executing python -m doctest -v path/to/file.py
> You can run tests on all files using run-test.py

# Further reading

## Books

1. Python Crash Course
2. Head-First Python, 2nd edition
3. Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)

## Links

1.  https://www.guru99.com/python-tutorials.html
2.  https://www.tutorialspoint.com/java/index.htm
3.  https://www.learnpython.org/en/
4. https://realpython.com/list-comprehension-python/

# Useful links

1. https://www.onlinegdb.com/online_python_compiler
2. https://regex101.com/