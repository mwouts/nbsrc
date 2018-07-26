"""Jupyter notebooks as python or R script

Use the 'nbsrc' conversion script to convert Jupyter notebooks from/to
R or Python scripts

NB: read, write methods, as well as ContentsManager, are to be found in the
nbrmd package
"""

from .nbsrc import readme

try:
    from .srcexporter import PyNotebookExporter
    from .srcexporter import RNotebookExporter
except ImportError as error:
    PyNotebookExporter = str(error)
    RNotebookExporter = str(error)
