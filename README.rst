=========
LSV-Panel
=========

A linear strength vortex panel method from Katz & Plotkin, implemented in 
Rust with a Python API.

Installation
============

To install on any operating system from PyPi, the recommended method is pip.
First, create a virtual environment and activate. On macOS/Linux,

.. code-block:: shell

    uv venv
    source .venv/bin/activate

On Windows,

.. code-block:: shell

    uv venv
    .venv\Scripts\activate

Then, install the library using ``pip``:

.. code-block:: shell

    uv pip install lsv-panel

Usage
=====

The following Python script can be executed assuming you have a Selig-format
airfoil coordinate file called ``"n0012-il.txt"`` located in the same 
directory.

.. code-block:: python

    import lsv_panel
    import numpy as np
    import os
    file_name = os.path.join("n0012-il.txt")
    coords = np.loadtxt(file_name, skiprows=1)
    co, cp, cl = lsv_panel.solve(coords, -3.0)

The airfoil coordinate file should look something like the following. Of
course, the line of code that loads the coordinates could be modified
to accomodate different coordinate formats.

.. code-block:: text

    NACA 0012
    1.000000  0.001260
    0.999416  0.001342
    ...       ...
    0.999416 -0.001342
    1.000000 -0.001260

The outputs of the ``solve`` function have the following meanings:

#. ``co``: The collocation points of the panel method (the midpoint of
   each airfoil coordinate panel). The data type is a list of lists.
#. ``cp``: The pressure coefficient at each collocation point.
   The data type is a list.
#. ``cl``: The lift coefficient. The data type is a float.
