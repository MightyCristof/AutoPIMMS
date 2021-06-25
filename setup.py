import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "autopimms",
    version = "1.0.0",
    author = "Elizabeth G. Lincoln, Rosa W. Everson, Christopher M. Carroll",
    author_email = "lincoln@astro.gsu.edu, rosa@ucsc.edu, c.m.carroll715@gmail.com",
    description = ("Upload tool for WebPIMMS designed for multiple queries."),
    license = "MIT",
    keywords = "AutoPIMMS documentation tutorial",
    url = "https://pypi.org/project/AutoPIMMS/",
    packages = find_packages(),
    long_description =read('README.md'),
    classifiers=[
        "Programming Language :: Python :: 3", 
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)