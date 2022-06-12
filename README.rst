.. image:: https://github.com/timcera/tappy/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/timcera/tappy/actions/workflows/python-package.yml
    :height: 20

.. image:: https://coveralls.io/repos/timcera/tappy/badge.png?branch=master
    :target: https://coveralls.io/r/timcera/tappy?branch=master
    :height: 20

.. image:: https://img.shields.io/pypi/v/tappy.svg
    :alt: Latest release
    :target: https://pypi.python.org/pypi/tappy

.. image:: http://img.shields.io/badge/license-BSD-lightgrey.svg
    :alt: BSD-3 clause license
    :target: https://pypi.python.org/pypi/tappy/

.. image:: http://img.shields.io/pypi/dd/tappy.svg
    :alt: tappy downloads
    :target: https://pypi.python.org/pypi/tappy/

TAPPY is a tidal analysis package. It breaks down a record of water
levels into the component sine waves. It is written in Python and uses
the least squares optimization and other functions in
`SciPy <http://www.scipy.org>`__. The focus is to make the most accurate
analysis possible. TAPPY only determines the constituents that are
calculatable according to the length of the time series.

Features
--------

-  Outputs a ‘International Hydrographic Organization - Tidal and Water
   Level Working Group’ standard XML constituent file.
-  Uses the IHO standard XML constituent file to make a predicted time
   series. By far the most frequent request that I get.
-  Calculates the node factor at each water elevation measurement. Very
   important for long time-series (greater than a year).
-  Very accurate ephemeris calculations thanks to the
   `Astrolabe <http://astrolabe.sourceforge.net>`__ library.
-  Able to read in different input data sets without changing TAPPY or
   the input data set. All you have to do is create a file that defines
   the input data set. Thanks to
   `Pyparsing <http://pyparsing.wikispaces.com/>`__.
-  Added the capability to read compressed files and Internet data
   streams (actually any URL) directly into TAPPY by using
   `filelike <http://www.rfk.id.au/software/filelike/>`__.
-  The time-series does not need to have equal intervals. In fact any
   length of missing data is allowed (though too much missing will cause
   a poor analysis).
-  Can adjust the Rayleigh factor that nearby constituents are compared
   against to determine what constituents can be differentiated.
-  TAPPY chooses the main constituents based upon the length of the time
   series and infers additional constituents that are known to be
   specifically related to the main constituents.
-  Can filter the tidal energy out of the input signal using transform
   (FFT), usgs (PL33), doodson, and boxcar methods. \|
   [CompareTidalFilters]
-  Can use the tidal filters to zero the time-series before
   determination of tidal constituents.
-  Can pad the usgs, doodson, and boxcar filters with predicted data to
   minimize edge effects of the filters.
-  Convenience function to fill missing values with the time series

Requirements
------------

`Python version 3.7.1 or later <http://www.python.org>`__

`SciPy <http://www.scipy.org>`__


Install
-------

::

   # To install...
   pip install tappy


TAPPY Citations
---------------

http://meetingorganizer.copernicus.org/EGU2009/EGU2009-5154.pdf

Please forward any citation of TAPPY to tim at cerazone.net.

Contributions
-------------

Development
~~~~~~~~~~~

Any help is appreciated. If you want you could send a patch file to me,
or if you would like to make a bunch of changes I can assign you
developer privileges to the source code repository. Just contact me at
tim at cerazone.net.
