Description
------------
List of collections similar to JAVA style collection for Python

Installation
============

::

    $ pip install collection-pipelines


Usage
=====

.. code-block:: python

    from collection import *

    l = List()
    l.add(1)
    l.is_empty()

    vec = Vector()
    vec.add(1)


Build Project
=============
python setup.py sdist
python setup.py bdist_wheel


Distribute
==========
twine upload --repository-url https://test.pypi.org/legacy/ dist/*