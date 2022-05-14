import pathlib
from setuptools import setup
from skbuild import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='jjshoots_test_hanabi',
    version='0.0.1',
    description='Learning environment for the game of hanabi.',
    author='taijunjet@hotmail.com',
    packages=['hanabi_learning_environment', 'hanabi_learning_environment.agents'],
    install_requires=['cffi']
    license="MIT",
    install_requires=["cffi"],
)
