#coding=utf-8
from distutils.core import setup
import sys
sys.path.append('./')
import py2exe
import requests.certs

#this allows to run it with a simple double click.
# sys.argv.append('py2exe')
build_exe_options = {"include_files":[(requests.certs.where(),'cacert.pem')]}
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll"],
        "compressed": 0,
        "optimize": 2,
        "ascii": 0,
        "packages": ["requests","urllib2"]
        }
 
setup(
      name = 'Translate',
      version = '1.1.8',
      windows = [{"script":'WinMain.py'}], 
      # zipfile = None,
      options = {'py2exe': py2exe_options,"build_exe":build_exe_options}
      )