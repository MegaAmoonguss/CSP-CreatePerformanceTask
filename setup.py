import sys
import importlib
from setuptools import setup

sympy_spec = importlib.util.find_spec("sympy")
if sympy_spec is None:
    sys.exit("SymPy must be installed, download it at https://github.com/sympy/sympy/releases.")

if sys.version_info < (3, 6):
    sys.exit("Python < 3.6 is not supported.")

setup(name="gmath",
      description="A practical mini math library/CLI",
      url="https://github.com/MegaAmoonguss/gmath",
      author="Graham Preston",
      author_email="graham.preston@gmail.com",
      packages=["gmath"],
      py_modules=["commands"],
      install_requires=["click", "sympy"],
      entry_points={"console_scripts": "gmath=commands:cli"}
      )
