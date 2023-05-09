import cx_Freeze
import sys
from cx_Freeze import setup, Executable
import os
base = None


build_exe_options = {"packages": ["os"]}
if sys.platform == 'win32':
    base = "Win32GUI"



setup(
    name ="Hindaco",
    version = "0.1",
    description = "An example wxPython script",
    options = {"build_exe":build_exe_options},
    executables = [Executable("main.py")]
    )