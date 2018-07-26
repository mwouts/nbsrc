from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='nbsrc',
    version='0.5.0',
    author='Marc Wouts',
    author_email='marc.wouts@gmail.com',
    description='Jupyter notebooks from/to python and R scripts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwouts/nbsrc',
    packages=find_packages(),
    install_requires=['nbrmd'],
    license='MIT',
    classifiers=('Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Framework :: Jupyter',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python',
                 'Topic :: Text Processing :: Markup',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6')
)
