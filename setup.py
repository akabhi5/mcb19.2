
import sys
from cx_Freeze import setup, Executable

setup(
    name = "multiclipboard",
    version = "19.2",
    description = "multiclipboard by abhi",
    executables = [Executable("MainWindow.py", icon="mainlogo.ico", base = "Win32GUI")])
