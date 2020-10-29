from contextlib import contextmanager
import os


# WRITING WITHOUT CONTEXT MANAGER, YOU HAVE TO REMEMBER TO CLOSE THE FILE.

# f = open('sample.txt', 'w')
# f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
# f.close()

# with open('sample.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')



@contextmanager
def change_dir(destination):
    global cwd
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('D:\PythonSda_exercises\Python_intermediate\Code_Profiling'):
    print(os.listdir())

