import nbsrc
import nbrmd
import pytest
from .utils import list_all_notebooks
import subprocess
import os


@pytest.mark.skipif(isinstance(nbsrc.PyNotebookExporter, str),
                    reason=nbsrc.PyNotebookExporter)
@pytest.mark.parametrize('nb_file', list_all_notebooks('.ipynb'))
def test_nbconvert_and_read_py(nb_file):
    # Load notebook
    nb = nbrmd.readf(nb_file)

    # Export to py using nbsrc package
    py1 = nbrmd.writes(nb, ext='.py')

    # Export to py using nbconvert exporter
    py_exporter = nbsrc.PyNotebookExporter()
    (py2, resources) = py_exporter.from_notebook_node(nb)

    assert py1 == py2


pytest.importorskip('jupyter')


@pytest.mark.skipif(isinstance(nbsrc.PyNotebookExporter, str),
                    reason=nbsrc.PyNotebookExporter)
@pytest.mark.parametrize('nb_file', list_all_notebooks('.ipynb'))
def test_nbconvert_cmd_line_py(nb_file, tmpdir):
    py_file = str(tmpdir.join('notebook.py'))

    subprocess.call(['jupyter', 'nbconvert', '--to', 'pynotebook',
                     nb_file, '--output', py_file])

    assert os.path.isfile(py_file)

    nb = nbrmd.readf(nb_file)
    py1 = nbrmd.writes(nb, ext='.py')
    with open(py_file) as fp:
        py2 = fp.read()

    assert py1 == py2


@pytest.mark.skipif(isinstance(nbsrc.RNotebookExporter, str),
                    reason=nbsrc.RNotebookExporter)
@pytest.mark.parametrize('nb_file', list_all_notebooks('.ipynb'))
def test_nbconvert_cmd_line_R(nb_file, tmpdir):
    r_file = str(tmpdir.join('notebook.R'))

    subprocess.call(['jupyter', 'nbconvert', '--to', 'rnotebook',
                     nb_file, '--output', r_file])

    assert os.path.isfile(r_file)

    nb = nbrmd.readf(nb_file)
    r = nbrmd.writes(nb, ext='.R')
    with open(r_file) as fp:
        r2 = fp.read()

    assert r == r2
