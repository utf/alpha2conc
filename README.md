README
======

Introduction
------------

This repository provides a simple function to estimate carrier
carrier concentrations, resulting from a material being subjected to the AM1.5G
solar spectrum. Only the absorption spectra of the material is required as input.

A full explanation of the code is provided in a [jupyter notebook](https://github.com/utf/alpha2conc/blob/master/tutorial_notebook.ipynb)

Usage
-----

The `abs2conc.py` contains the python code required to calculate the carrier
concentration based on the absorption spectra of material.

A jupyter notebook has been provided, which gives a tutorial on how the script
should be used.

Requirements
------------

This script is currently compatible with Python 3.5.
Numpy is required for matrix operations and pvpy is required for
obtaining the AM1.5G spectrum in units of photon flux.

License
-------

This script is made available under the MIT License.
