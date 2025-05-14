import sys, os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller sets sys._MEIPASS to the temp directory where files are unpacked
        base_path = sys._MEIPASS
    except AttributeError:
        # We’re probably running in “dev” mode
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
