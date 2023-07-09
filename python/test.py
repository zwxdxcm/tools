import os
from utils import io,misc

def test_io():
    io.create_dirs(os.path.join('.','demo'), clear=False)

if __name__ == "__main__":
    test_io()