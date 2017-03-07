from setuptools import setup, Extension

setup(name="gmath-py",
      version="0.0.1",
      description="A Python implementation of the depricated GMath Java library",
      long_description="Useful calculation functions in Python, such as quadratic factoring, repeating decimal notation, decimal to fraction, and more.",
      url="https://github.com/MegaAmoonguss/GMath-py",
      author="Graham Preston",
      author_email="graham.preston@gmail.com",
      packages=["gmath"],
      ext_modules=[Extension("gmath.factoring_c", sources=["./gmath/extension/factoring_c.c"])],
      include_package_data=True)
