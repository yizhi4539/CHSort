from distutils.core import setup
from Cython.Build import cythonize
 
setup(
  name = 'tools',
  ext_modules = cythonize("tools.py"),
)
