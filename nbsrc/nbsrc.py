"""Methods for the nbsrc package. Note that methods for notebooks are
found in the nbrmd package"""

import os


def readme():
    """Contents of README.md"""
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '..', 'README.md')
    with open(readme_path) as readme_file:
        return readme_file.read()
