"""Jupyter notebooks as python or R script

Use this module to read or write Jupyter notebooks as R or python scripts
(methods 'read', 'reads', 'write', 'writes')

Use the 'nbsrc' conversion script to convert Jupyter notebooks from/to
R or Python scripts
"""

from nbrmd import readf, writef, writes, reads, notebook_extensions
from .nbsrc import readme

try:
    from .srcexporter import PyNotebookExporter
    from .srcexporter import RNotebookExporter
except ImportError as e:
    PyNotebookExporter = str(e)
    RNotebookExporter = str(e)
