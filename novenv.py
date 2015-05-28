import subprocess
import stat
import sys
import os
import fs
from termcolor import cprint

OUT_PRFX = "----"
OUT_PRFX_VERBOSE = "    "
OUT_STD_COLOR = "green"
OUT_CMD_COLOR = "blue"

NOVENV_DIR = ".novenv"
VENV_DIR = ".venv"
VENV_CMD = "pyvenv"

PYWS_DIR = fs.join(fs.home(), NOVENV_DIR)
PYWS_DIR_BIN = fs.join(PYWS_DIR, "bin")

def check_venv():
    """Check if virtualenv exists"""

    # Check if virtualenv directory exists in current directory
    if not fs.exists(VENV_DIR):
        
        cprint("%sNo virtual-envrionment detected" % (OUT_PRFX), OUT_STD_COLOR)
        
        # Create a new virtualenv
        create_venv()


def create_venv():
    """Create a virtualenv"""

    cprint("%sCreating virtual-envrionment in dir %s" % (OUT_PRFX, VENV_DIR), OUT_STD_COLOR)
    
    # Creating virtual environment
    return_code = subprocess.call("%s %s" % (VENV_CMD, VENV_DIR), shell=True) 


def clear_venv():
    """Clear the virtualenv"""

    cprint("%sRemoving virtual-envrionment from dir %s" % (OUT_PRFX, VENV_DIR), OUT_STD_COLOR)

    # Delete the directory that contains the virtual environemnt
    fs.rmdir(VENV_DIR)


def check_config():

    if not fs.exists(PYWS_DIR):
        fs.mkdir(PYWS_DIR)

    if not fs.exists(PYWS_DIR_BIN):
        fs.mkdir(PYWS_DIR_BIN)


def create_config():
    """Create executables in the project directory"""
    check_config()

    cprint("%sWriting python executable to %s" % (OUT_PRFX, PYWS_DIR_BIN), OUT_STD_COLOR)
    fs.write("%s/python" % PYWS_DIR_BIN, "#! /usr/bin/python\nimport novenv\nnovenv.python()")
    fs.chmod("%s/python" % PYWS_DIR_BIN, stat.S_IEXEC)

    cprint("%sWriting python3 executable to %s" % (OUT_PRFX, PYWS_DIR_BIN), OUT_STD_COLOR)
    fs.write("%s/python3" % PYWS_DIR_BIN, "#! /usr/bin/python\nimport novenv\nnovenv.python(version=3)")
    fs.chmod("%s/python3" % PYWS_DIR_BIN, stat.S_IEXEC)
    
    cprint("%sWriting pip executable to %s" % (OUT_PRFX, PYWS_DIR_BIN), OUT_STD_COLOR)
    fs.write("%s/pip" % PYWS_DIR_BIN, "#! /usr/bin/python\nimport novenv\nnovenv.pip()")
    fs.chmod("%s/pip" % PYWS_DIR_BIN, stat.S_IEXEC)

    cprint("%sWriting pip3 executable to %s" % (OUT_PRFX, PYWS_DIR_BIN), OUT_STD_COLOR)
    fs.write("%s/pip3" % PYWS_DIR_BIN, "#! /usr/bin/python\nimport novenv\nnovenv.pip(version=3)")
    fs.chmod("%s/pip3" % PYWS_DIR_BIN, stat.S_IEXEC)

    cprint("%sPlease add the %s directory to your path" % (OUT_PRFX, PYWS_DIR_BIN), OUT_CMD_COLOR)
    cprint("%sexport PATH=/home/ckoerner/%s/bin:$PATH" % (OUT_PRFX_VERBOSE, VENV_DIR), OUT_CMD_COLOR)

    cprint("%sCheck current python executable with" % (OUT_PRFX), OUT_CMD_COLOR)
    cprint("%swhich python" % (OUT_PRFX_VERBOSE), OUT_CMD_COLOR)


def clear_config():
    """Truncate the bin dir containing the executables"""
    check_config()
    fs.truncate(PYWS_DIR_BIN)

def run():
    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--init', help='Create python virtualenv', action="store_true")
    parser.add_argument('--clear', help='Remove python virtualenv', action="store_true")
    parser.add_argument('--install', help='Initialize python executables', action="store_true")
    parser.add_argument('--uninstall', help='Remove python executables', action="store_true")
    
    args = parser.parse_args()

    if args.install:
        create_config()
    elif args.uninstall:
        clear_workspace()
    elif args.clear:
        clear_venv()
    else:
        create_venv()


def python(version=""):
    """run the python interpreter"""
    args = " ".join(sys.argv[1:])
    cmd = "/usr/bin/python%s" % (version)
    
    if fs.exists(VENV_DIR):
        cmd = "%s/bin/python%s" % (VENV_DIR, version)
        cprint("%sUsing interpreter %s" % (OUT_PRFX, cmd), OUT_STD_COLOR)
    
    return_code = subprocess.call( "%s %s" % (cmd, args), shell=True) 


def pip(version=""):
    """run pip exectuable"""
    args = " ".join(sys.argv[1:])
    cmd = "/usr/bin/pip%s" % (version)

    if fs.exists(VENV_DIR):
        cmd = "%s/bin/pip%s" % (VENV_DIR, version)
        cprint("%sUsing exectuable %s" % (OUT_PRFX, cmd), OUT_STD_COLOR)
    
    return_code = subprocess.call("%s %s" % (cmd, args), shell=True) 