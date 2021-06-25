
Overview
--------

A Python package for automating calls to WebPIMMS.

AutoPIMMS was created by 
`Elizabeth Lincoln <https://github.com/ellielinc>`__, 
`Rosa Everson <https://github.com/rosawe>`__, and 
`Christopher Carroll <https://github.com/MightyCristof>`__ 
during the Code/Astro: Software Engineering Workshop for Astronomy 
in June 2021.

Installation
------------

|Latest Version| |Supported Versions|

Download and install the latest version from `PyPI <https://pypi.org/project/autopimms/>`__::

  pip install autopimms

Download and install the development version from `GitHub <https://github.com/MechanicalSoup/MechanicalSoup>`__::

  pip install git+https://github.com/MechanicalSoup/MechanicalSoup

Installing from source (into the current working directory)::

  python setup.py install

(In all cases, add ``--user`` to the ``install`` command to
install in the current user's home directory.)


Documentation
-------------

The full documentation is available on
https://mechanicalsoup.readthedocs.io/. You may want to jump directly to
the `automatically generated API
documentation <https://mechanicalsoup.readthedocs.io/en/stable/mechanicalsoup.html>`__.

Example
-------

From `<examples/expl_qwant.py>`__, code to get the results from
a Qwant search:

.. code:: python

    """Example usage of AutoPIMMS to get the results from WebPIMMS
    web form.
    """
    
    import autopimms
    autopimms.main()
    

Development
-----------

|Build Status| |Coverage Status|
|Requirements Status| |Documentation Status|
|CII Best Practices|
|LGTM Alerts|
|LGTM Grade|

Instructions for building, testing and contributing to MechanicalSoup:
see `<CONTRIBUTING.rst>`__.

Common problems
---------------

Read the `FAQ
<https://mechanicalsoup.readthedocs.io/en/stable/faq.html>`__.


.. |Latest Version| image:: https://img.shields.io/pypi/v/autopimms.svg
   :target: https://pypi.python.org/pypi/autopimms/
.. |Supported Versions| image:: https://img.shields.io/pypi/pyversions/autopimms.svg
   :target: https://pypi.python.org/pypi/autopimms/