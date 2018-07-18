from setuptools import setup, find_packages
from nbsrc.nbsrc import readme

setup(
    name='nbsrc',
    version='0.4.0',
    author='Marc Wouts',
    author_email='marc.wouts@gmail.com',
    description='Jupyter notebooks from/to python and R scripts',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/mwouts/nbsrc',
    packages=find_packages(),
    entry_points={'console_scripts': ['nbsrc = nbsrc.cli:main'],
                  'nbconvert.exporters': [
                      'pynotebook = nbsrc:PyNotebookExporter',
                      'rnotebook = nbsrc:RNotebookExporter'
                  ]},
    tests_require=['pytest', 'testfixtures'],
    install_requires=['nbformat>=4.0.0', 'mock', 'pyyaml'],
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
