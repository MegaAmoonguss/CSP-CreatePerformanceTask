from distutils.core import setup

setup(name="GMath",
      version="0.0.1",
      description="A Python implementation of the depricated GMath Java library",
      long_description="Useful calculation functions in Python, such as quadratic factoring, repeating decimal notation, decimal to fraction, and more.",
      url="https://github.com/MegaAmoonguss/GMath-py",
      author="Graham Preston",
      author_email="graham.preston@gmail.com",
      packages=["gmath"],
      install_requires=["click"],
      entry_points="""
          [console_scripts]
          gmath=commands:cli
      """)
