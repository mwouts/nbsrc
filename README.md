# Jupyter notebooks from/to Python or R scripts

[![Pypi](https://img.shields.io/pypi/v/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)
[![Pypi](https://img.shields.io/pypi/l/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)
[![Build Status](https://travis-ci.com/mwouts/nbsrc.svg?branch=master)](https://travis-ci.com/mwouts/nbsrc)
[![codecov.io](https://codecov.io/github/mwouts/nbsrc/coverage.svg?branch=master)](https://codecov.io/github/mwouts/nbsrc?branch=master)
![pylint Score](https://mperlet.github.io/pybadge/badges/9.6.svg)
[![pyversions](https://img.shields.io/pypi/pyversions/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mwouts/nbrmd/master?filepath=demo)

Jupyter notebooks are complex files, that contain source code, metadata, and
rich outputs. Here we offer a simple and complementary format for Jupyter
notebooks, as pure python (or R) companion scripts.

The resulting python scripts are perfect candidates for
keeping notebooks under *version control*. They can be
*edited* outside of Jupyter, using
your favorite text editor, or even standard merge tools if you wish to merge
*multiple contributions* to a notebook.

With the `nbsrc` package, any python or R script can be loaded as a notebook
in Jupyter. If a classical `ipynb` notebook with a matching name exists,
outputs for matching inputs are reconstructed. And, if you associate python
and jupyter files as recommended below, when a `ipynb` notebook opens, the
corresponding inputs are taken from the `py` file, which you may have updated
outside of Jupyter.

## Can I have a demo?

Sure. Try our package on [binder](https://mybinder.org/v2/gh/mwouts/nbrmd/master?filepath=demo)!

There, you will be able
- to open and execute arbitrary python files as notebooks (give a try to
the matplotlib demo named `filled_step.py`, for instance)
- to open a notebook, then edit the companion python script, and reload the notebook,
to find up-to-date inputs in Jupyter.

## How does the python version look like?

Below is an example of a Jupyter notebook, together with its python representation.

We have a battery of tests that ensure that
- Round trip conversion: python to notebook to python, is *identity*
- Round trip conversion, starting from a Jupyter notebook, preserve *source*
and *metadata*, not outputs. In some occasions (consecutive blank lines in
code cells), cells may be splitted into smaller ones.

Python [notebook](https://mybinder.org/v2/gh/mwouts/nbrmd/master?filepath=tests/python_notebook_sample.py) in Jupyter  | Python [script](https://github.com/mwouts/nbrmd/blob/master/tests/python_notebook_sample.py)
:--------------------------:|:-----------------------:
![](https://raw.githubusercontent.com/mwouts/nbsrc/master/img/python_notebook.png)   | ![](https://raw.githubusercontent.com/mwouts/nbsrc/master/img/python_source.png)

The representation of notebooks as R scripts follows the [standard](https://rmarkdown.rstudio.com/articles_report_from_r_script.html) for that language.

## How do I activate the companion script?

- generate a jupyter config, if you don't have one yet, with `jupyter notebook --generate-config`
- edit the config and include the below:
```python
c.NotebookApp.contents_manager_class = 'nbrmd.RmdFileContentsManager'
c.ContentsManager.default_nbrmd_formats = 'ipynb,py'
```

Then, make sure you have the `nbrmd` package up-to-date, and re-start jupyter, i.e. run
```bash
pip install nbrmd --upgrade
jupyter notebook
```

## Per notebook configuration

With the above configuration, every notebook will have a companion `.py` file.

If you prefer that the companion script be generated only for a few notebooks,
then remove the `c.ContentsManager.default_nbrmd_formats` line from Jupyter's
configuration, and instead edit the notebook metadata as follows:
```
{
  "kernelspec": {
    "name": "python3",
    (...)
  },
  "language_info": {
    (...)
  },
  "nbrmd_formats": "ipynb,py"
}
```

Accepted formats are: `.ipynb`, `.Rmd`, `.py` and `.R`.

In case you want both `.py` and `.Rmd`, please note that the
order matters: the first non-`.ipynb` extension
is the one used as the reference source for notebook inputs.

## What is the difference between `nbsrc` and `nbrmd`?

`nbrmd` is a python package that represents Jupyter notebooks as R markdown
files. It is also where notebooks as python scripts are implemented. But
I felt notebooks as scripts deserved a standalone documentation, and
that's the main reason for having the `nbsrc` package.

You don't actually need the `nbsrc` package unless you want the command line
conversion tools.

## Command line conversion

The `nbsrc` package provides a `nbsrc` script that converts Jupyter notebooks
 to R or python scripts, and vice-versa.
 
Install it with 
```
pip install nbsrc --upgrade
```

and then use it as:
```bash
nbsrc jupyter.ipynb         # this prints the `.py` or `.R` alternative
nbsrc jupyter.ipynb -i      # this creates a jupyter.py or jupyter.R file
nbsrc jupyter.py    -i      # and this, a jupyter.ipynb file
nbsrc jupyter.py    -i -p   # update the jupyter.ipynb file and preserve outputs that correspond to unchanged inputs
```

Alternatively, the `nbsrc` package provides two `nbconvert` exporters that you can use with
```bash
nbconvert jupyter.ipynb --to pynotebook
nbconvert jupyter.ipynb --to rnotebook
```

