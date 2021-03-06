from setuptools import setup
from setuptools import find_packages
import sys

__version__ = ""
args = sys.argv
try:
    with open('motherbrain/version.py') as f:
        exec(f.read())
except:
    __version__ = "?"


requires = [
    'numpy >= 1.18.1, <2',
]

test_requirements = [
    'pytest >= 4.6.3, <5',
    'tensorflow >= 2.4.0, < 3',
]

setup(
    name='motherbrain',
    version=__version__,
    author="Joseph Daws",
    author_email="daws.joseph@gmail.com",
    description="Card games, agents to play them, and algorithms to train the agents.",
    python_requires=">=3.7.*",
    install_requires=requires,
    url="https://github.com/joedaws/aicard.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",''
        "Operating System :: OS Independent",
    ],
)
