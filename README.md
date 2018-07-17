# Python and R scripts as Jupyter notebooks

[![Pypi](https://img.shields.io/pypi/v/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)
[![Pypi](https://img.shields.io/pypi/l/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)
[![Build Status](https://travis-ci.com/mwouts/nbsrc.svg?branch=master)](https://travis-ci.com/mwouts/nbsrc)
[![codecov.io](https://codecov.io/github/mwouts/nbsrc/coverage.svg?branch=master)](https://codecov.io/github/mwouts/nbsrc?branch=master)
[![pyversions](https://img.shields.io/pypi/pyversions/nbsrc.svg)](https://pypi.python.org/pypi/nbsrc)

This package provides companion scripts (`.py` or `.R` extension)
to your Jupyter notebooks, that are always *synchronized*
with the notebook.

With this you will be able to
- set the `.py` or `.R` script under version control
- modify the script outside of Jupyter, and easily merge multiple contributions
to the notebook using standard, text merge tools
- reload the latest version of the notebook from the `.py` or `.R` script. Outputs
for the cells with unchanged input are taken from the `.ipynb` file.

## How do I activate the companion script?

- generate a jupyter config, if you don't have one yet, with `jupyter notebook --generate-config`
- edit the config and include the below:
```python
c.NotebookApp.contents_manager_class = 'nbrmd.RmdFileContentsManager'
c.ContentsManager.default_nbrmd_formats = ['.ipynb', '.py']
```

Then, make sure you have the `nbsrc` and `nbrmd` packages installed, and re-start jupyter, i.e. run
```bash
pip install nbrmd nbsrc --upgrade
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
  "nbrmd_formats": [".ipynb", ".py"]
}
```

Accepted formats are: `.ipynb`, `.Rmd`, `.py` and `.R`.

In case you want both `.py` and `.Rmd`, please note that the
order matters: the first non-`.ipynb` extension
is the one used as the reference source for notebook inputs.

## Command line conversion

The package also provides a `nbsrc` script that converts Jupyter notebooks
 to R or python scripts, and vice-versa.

Use it as:
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

## And if I convert twice?

Round trip conversion of scripts is identity.
Round trip conversion of Jupyter notebooks preserves the source, not outputs.

