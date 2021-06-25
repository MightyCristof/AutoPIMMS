from setuptools import setup, find_packages
import os, re

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# auto-updating version
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(project + '/__init__.py').read())
    return result.group(1)

# parse requirements.txt file for dependency install
def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

setup(
    name = "autopimms",
    version = get_property('__version__', 'autopimms'),
    description = ("Upload tool for WebPIMMS designed for multiple queries."),
    long_description =read('README.md'),
    url = "https://pypi.org/project/AutoPIMMS/",
    keywords = 'X-ray Astronomy WebPIMMS',
    author = "Elizabeth G. Lincoln, Rosa W. Everson, Christopher M. Carroll",
    author_email = "lincoln@astro.gsu.edu, rosa@ucsc.edu, c.m.carroll715@gmail.com",
    license = "MIT",    
    packages = find_packages(),
    include_package_data = True,
    install_requires=get_requires(),
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3', 
    ],
)