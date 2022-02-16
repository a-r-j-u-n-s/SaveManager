from setuptools import setup

setup(
    name='savegame-manager',
    version='1.0.1',
    scripts=['./scripts/savegame.cmd'],
    author='Arjun Srivastava',
    description='Save folder manager for PC games.',
    packages=['src.savegame'],
    install_requires=[
        'setuptools',
        'argparse',
        'psutil>=5.7.0'
    ],
    python_requires='>=3.8'
)
