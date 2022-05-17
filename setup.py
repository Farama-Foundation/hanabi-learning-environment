import pathlib
from setuptools import setup
from skbuild import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='hanabi_learning_environment',
    version='0.0.4',
    description='Learning environment for the game of hanabi.',
    long_description_content_type="text/markdown",
    long_description="Learning environment for the game of hanabi.",
    author='deepmind/hanabi-learning-environment',
    packages=['hanabi_learning_environment', 'hanabi_learning_environment.agents'],
    license="MIT",
    install_requires=["cffi"],
)
