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
calculable according to the length of the time series.

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
-  Convenience function to fill missing values with the predicted time series

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
Barbosa, S. M., 2009. Analysis of trends in North Atlantic tidal amplitudes
University of Porto, Portugal (susana.barbosa@fc.up.pt)
http://meetingorganizer.copernicus.org/EGU2009/EGU2009-5154.pdf

Bechet, V., Verstraeten, E., Hanert, E. and Deleersnijder, E., 2018.
Multiple-year marine connectivity modeling in the Florida Coral Reef Tract to
assess Acropora Cervicornis recovery. (Unpublished master’s thesis). Ecole
polytechnique de Louvain, Université catholique de Louvain.

Becker, K., Davis, E.E. and Villinger, H., Long‐Term Observations of
Subseafloor Temperatures and Pressures in a Low‐Temperature, Off‐axis
Hydrothermal System in North Pond on the Western Flank of the Mid‐Atlantic
Ridge. Geochemistry, Geophysics, Geosystems, p.e2021GC010496.
https://doi.org/10.1029/2022GC010496

Cucco, A., Martín, J., Quattrocchi, G., Fenco, H., Umgiesser, G. and Fernández,
D.A., 2022. Water Circulation and Transport Time Scales in the Beagle Channel,
Southernmost Tip of South America. Journal of Marine Science and Engineering,
10(7), p.941.
https://doi.org/10.3390/jmse10070941

Ferrarin, C., Roland, A., Bajo, M., Umgiesser, G., Cucco, A., Davolio, S.,
Buzzi, A., Malguzzi, P. and Drofa, O., 2013. Tide-surge-wave modelling and
forecasting in the Mediterranean Sea with focus on the Italian coast, Ocean
Modelling, Vol. 61, January 2013, pp. 38-48.
https://doi.org/10.1016/j.ocemod.2012.10.003

Ferrarin, C., Zaggia, L., Paschini, E., Scirocco, T., Lorenzetti, G., Bajo, M.,
Penna, P., Francavilla, M., D’Adamo, R. and Guerzoni, S., 2014. Hydrological
regime and renewal capacity of the micro-tidal Lesina Lagoon, Italy. Estuaries
and coasts, 37(1), pp.79-93.
https://doi.org/10.1007/s12237-013-9660-x

Ferrarin, C., Tomasin, A., Bajo, M., Petrizzo, A. and Umgiesser, G., 2015.
Tidal changes in a heavily modified coastal wetland. Continental Shelf
Research, 101, pp.22-33.
https://doi.org/10.1016/j.csr.2015.04.002

Gaeta, M.G., Samaras, A.G., Federico, I., Archetti, R., Maicu, F. and
Lorenzetti, G., 2016. A coupled wave–3-D hydrodynamics model of the Taranto Sea
(Italy): a multiple-nesting approach. Natural hazards and earth system
sciences, 16(9), pp.2071-2083.
https://doi.org/10.5194/nhess-16-2071-2016

Neves, L.J.P.F., Barbosa, S.M. and Pereira, A.J.S.C., 2009. Indoor radon
periodicities and their physical constraints: a study in the Coimbra region
(Central Portugal). Journal of environmental radioactivity, 100(10),
pp.896-904.
https://doi.org/10.1016/j.jenvrad.2009.06.017

Vergara-Chen, C., Pérez-Ruzafa, A., De Pascalis, F., Ghezzo, M.,
Quispe-Becerraa, J.I., Hernández-García, R., Muñoza, I., Pérez-Ruzafa, I.M.,
Umgiesserb, G. and Marcosa, C., 2018. Connectivity between coastal lagoons and
sea: Asymmetrical effects on assemblages' and populations' structure.
https://ridda2.utp.ac.pa/handle/123456789/4432

Žust, L., Fettich, A., Kristan, M. and Ličer3, M., 2021. HIDRA 1.0:
deep-learning-based ensemble sea level forecasting in the northern Adriatic,
Geosci. Model Dev., 14, 2057–2074, 2021
https://doi.org/10.5194/gmd-14-2057-2021
This work is distributed under the Creative Commons Attribution 4.0 License.

Please forward any citation of TAPPY to tim at cerazone.net.

Contributions
-------------
Any help is appreciated. Best would be a pull request on Github or Bitbucket or
if you would like to make a bunch of changes I can assign you developer
privileges to the source code repository. Just contact me at tim at
cerazone.net.
