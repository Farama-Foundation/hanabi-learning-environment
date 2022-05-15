from skbuild import setup

setup(
    name='hanabi_learning_environment',
    version='0.0.3',
    description='Learning environment for the game of hanabi.',
    long_description_content_type="text/markdown",
    long_description="Learning environment for the game of hanabi.",
    author='deepmind/hanabi-learning-environment',
    packages=['hanabi_learning_environment', 'hanabi_learning_environment.agents'],
    install_requires=['cffi']
)
