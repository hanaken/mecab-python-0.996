#!/usr/bin/env python

from distutils.core import setup,Extension
from commands import getoutput

def cmd1(cmd):
    return getoutput(cmd)

def cmd2(cmd):
    return cmd1(cmd).split()

setup(name = "mecab-python",
	version = cmd1("mecab-config --version"),
	py_modules=["MeCab"],
	ext_modules = [
			Extension("_MeCab", ["MeCab_wrap.cxx",],
				include_dirs=cmd2("mecab-config --inc-dir"),
				library_dirs=cmd2("mecab-config --libs-only-L"),
				libraries=cmd2("mecab-config --libs-only-l"))
			]
)
