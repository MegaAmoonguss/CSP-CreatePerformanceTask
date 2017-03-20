from setuptools import setup

setup(name="gmath",
      description="A practical mini math library/CLI",
      url="https://github.com/MegaAmoonguss/gmath",
      author="Graham Preston",
      author_email="graham.preston@gmail.com",
      packages=["gmath"],
      install_requires=["click"],
      entry_points="""
      [console_scripts]
      gmath=commands:cli
      """
      )
