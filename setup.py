#!/usr/bin/env python

"""
setup.py file for SWIG Wrapper for MCFSimplex
"""

from setuptools import setup, Extension
import numpy as np  # for numpy array conversion

with open("README.md", "r") as file:
    long_desc = file.read()

pyMCFSimplex_module = Extension('_pyMCFSimplex',
                                sources=['pyMCFSimplex_wrap.cxx', 'MCFSimplex.cpp'],
                                include_dirs=[np.get_include()], extra_compile_args=["-w"])

setup(name='pyMCFSimplex',
      version='0.9.4',
      author="G#.Blog - Johannes Sommer",
      author_email="info@sommer-forst.de",
      url="http://www.sommer-forst.de/blog",
      description="pyMCFSimplex is a Python Wrapper for MCFSimplex",
      long_description=long_desc,
      long_description_content_type='text/markdown',
      include_dirs=[np.get_include()],  # Header for numpy
      ext_modules=[pyMCFSimplex_module],
      license="LGPL 2.1",
      platforms=["win32", "manylinux1_x86_64"],
      py_modules=["pyMCFSimplex"],
      install_requires=["numpy"],
      )
