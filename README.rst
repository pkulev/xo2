|PyPI| |Build Status| |codecov.io|

===
xo2
===

Python framework for creating 3D applications.

Requirements
============

* >=python-3.7
* >=eaf-0.2

Installation
============

.. code-block:: console

	$ pip install xo2


Development
===========

Installation
------------

.. code-block:: console

   $ poetry install

Testing
-------

.. code-block:: console

   $ poetry run pytest -s -v tests/  # run all tests
   $ poetry run pytest --cov=xo2 -s -v tests/  # run all tests with coverage
   $ poetry run black xo2/ tests/  # autoformat code
   $ # run type checking
   $ poetry run pytest --mypy --mypy-ignore-missing-imports -s -v xo2/ tests/
   $ # run code linting
   $ poetry run pytest --pylint -s -v xo2/ tests/

Documentation
-------------

* **To be added**

.. |PyPI| image:: https://badge.fury.io/py/xo2.svg
   :target: https://badge.fury.io/py/xo2
.. |Build Status| image:: https://github.com/pkulev/xo2/workflows/CI/badge.svg
.. |codecov.io| image:: http://codecov.io/github/pkulev/xo2/coverage.svg?branch=master
   :target: http://codecov.io/github/pkulev/xo2?branch=master
