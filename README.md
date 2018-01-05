README
======

Introduction
------------

This repository provides a simple function to calculate photoexcited
carrier concentrations due to the AM1.5G solar spectrum, based on a
materials optical absorption. The carrier concentrations are calculated
for a specific thickness of material (considering generation will decay
exponentially into the material) and carrier lifetime (tau).

A full explanation of the code is provided in a [jupyter notebook](https://github.com/utf/alpha2conc/blob/master/tutorial_notebook.ipynb)

Usage
-----

The `abs2conc.py` contains the python code required to calculate the carrier
concentration based on the absorption spectra of material.

A jupyter notebook has been provided, which gives a tutorial on how the script
should be used.

Requirements
------------

This script is currently compatible with Python 2.7 and Python 3+.
Numpy is required for matrix operations.

License
-------

This script is made available under the MIT License.
