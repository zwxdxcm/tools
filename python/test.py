import os
import utils

def test_io():
   utils.io.create_dirs(os.path.join('.','demo'), clear=False)

if __name__ == "__main__":
    test_io()