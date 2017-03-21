import sys
from setuptools import setup

try:
    import sympy #@UnusedImport
except ModuleNotFoundError:
    print("SymPy must be installed, download it at https://github.com/sympy/sympy/releases.")
    sys.exit(1)

setup(name="gmath",
      description="A practical mini math library/CLI",
      url="https://github.com/MegaAmoonguss/gmath",
      author="Graham Preston",
      author_email="graham.preston@gmail.com",
      packages=["gmath"],
      py_modules=["commands"],
      install_requires=["click"],
      entry_points={"console_scripts": "gmath=commands:cli"}
      )
