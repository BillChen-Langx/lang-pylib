========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/lang-pylib/badge/?style=flat
    :target: https://lang-pylib.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/BillChen-Langx/lang-pylib/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/BillChen-Langx/lang-pylib/actions

.. |version| image:: https://img.shields.io/pypi/v/lang-pylib.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/lang-pylib

.. |wheel| image:: https://img.shields.io/pypi/wheel/lang-pylib.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/lang-pylib

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/lang-pylib.svg
    :alt: Supported versions
    :target: https://pypi.org/project/lang-pylib

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/lang-pylib.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/lang-pylib

.. |commits-since| image:: https://img.shields.io/github/commits-since/BillChen-Langx/lang-pylib/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/BillChen-Langx/lang-pylib/compare/v0.0.1...main



.. end-badges

LangX Python Library

* Free software: BSD 2-Clause License

Installation
============

::

    pip install lang-pylib

You can also install the in-development version with::

    pip install https://github.com/BillChen-Langx/lang-pylib/archive/main.zip


Documentation
=============


https://lang-pylib.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
