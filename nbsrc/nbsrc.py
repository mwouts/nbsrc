import os


def readme():
    """
    Contents of README.md
    :return:
    """
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '..', 'README.md')
    with open(readme_path) as fh:
        return fh.read()
