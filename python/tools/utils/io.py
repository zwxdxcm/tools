import os
import shutil
import warnings


def create_dirs(dirs, clear=False):
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    elif clear is True:
        clear_dirs(dirs)
        os.makedirs(dirs)

    else:
        warnings.warn(f"dirs: {dirs} has already existed and you select to not clear")


def clear_dirs(dirs):
    if os.path.exists(dirs):
        shutil.rmtree(dirs)