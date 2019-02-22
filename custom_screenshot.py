import tempfile
import os


def custom_screenshot():
    f = tempfile.NamedTemporaryFile()
    name = f.name
    os.system("screencapture -R 0,0,1920,1080 %s" % name)
    with open(name, 'rb') as fp:
        new_file = fp.read()
    f.close()
    return new_file
