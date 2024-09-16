.. image:: https://github.com/timcera/tappy/actions/workflows/pypi-package.yml/badge.svg
    :alt: Tests
    :target: https://github.com/timcera/tappy/actions/workflows/pypi-package.yml
    :height: 20

.. image:: https://img.shields.io/coveralls/github/timcera/tappy
    :alt: Test Coverage
    :target: https://coveralls.io/r/timcera/tappy?branch=master
    :height: 20

.. image:: https://img.shields.io/pypi/v/tappy.svg
    :alt: Latest release
    :target: https://pypi.python.org/pypi/tappy/
    :height: 20

.. image:: https://img.shields.io/pypi/l/tappy.svg
    :alt: BSD-3 clause license
    :target: https://pypi.python.org/pypi/tappy/
    :height: 20

.. image:: https://img.shields.io/pypi/dd/tappy.svg
    :alt: tappy downloads
    :target: https://pypi.python.org/pypi/tappy/
    :height: 20

.. image:: https://img.shields.io/pypi/pyversions/tappy
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/tappy/
    :height: 20

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
Barbosa, S. M. (2009). Analysis of trends in North Atlantic tidal amplitudes.
University of Porto, Portugal (susana.barbosa@fc.up.pt)
http://meetingorganizer.copernicus.org/EGU2009/EGU2009-5154.pdf

Bechet, V., Verstraeten, E., Hanert, E. and Deleersnijder, E. (2018).
Multiple-year marine connectivity modeling in the Florida Coral Reef Tract to
assess *Acropora Cervicornis* recovery. (Unpublished master's thesis). Ecole
polytechnique de Louvain, Université catholique de Louvain.
https://dial.uclouvain.be/downloader/downloader.php?pid=thesis%3A14852&datastream=PDF_01

Becker, K., Davis, E. E., and Villinger, H. (2022). Long‐Term Observations of
Subseafloor Temperatures and Pressures in a Low‐Temperature, Off‐Axis
Hydrothermal System in North Pond on the Western Flank of the Mid‐Atlantic
Ridge. Geochemistry, Geophysics, Geosystems, 23(9). Portico.
https://doi.org/10.1029/2022gc010496

Billings, W. Z. (2018). An Exploration of the Two-Dimensional Poroelastic
Properties of Oceanic Crust at the Formation Scale (Order No. 10846298).
Available from Earth, Atmospheric and Aquatic Science Collection. (2113533060).
https://www.proquest.com/dissertations-theses/exploration-two-dimensional-poroelastic/docview/2113533060/se-2

Campos, E. J. D., Kjerfve, B., Cavalcante, G., Vieira, F., and Abouleish, M.
(2022). Water exchange across the Strait of Hormuz. Effects of tides and river
runoff. Regional Studies in Marine Science, 52, 102336.
https://doi.org/10.1016/j.rsma.2022.102336

Cucco, A., Martín, J., Quattrocchi, G., Fenco, H., Umgiesser, G., and
Fernández, D. A. (2022). Water Circulation and Transport Time Scales in the
Beagle Channel, Southernmost Tip of South America. Journal of Marine Science
and Engineering, 10(7), 941. https://doi.org/10.3390/jmse10070941

Davis, E. E., Sun, T., Heesemann, M., Becker, K., and Schlesinger, A. (2023).
Long‐Term Offshore Borehole Fluid‐Pressure Monitoring at the Northern Cascadia
Subduction Zone and Inferences Regarding the State of Megathrust Locking.
Geochemistry, Geophysics, Geosystems, 24(6), e2023GC010910.
https://doi.org/10.1029/2023GC010910

Desmet, N. (2019). Modelling coral larvae exchanges between the Great Barrier
Reef and outer reefs. Ecole polytechnique de Louvain, Université catholique de
Louvain. Promoter : Hanert, Emmanuel ; Deleersnijder, Eric.
http://hdl.handle.net/2078.1/thesis:19591

El Akmal, P. N. (2013). Determination of the Permeability of the South Chamorro
Seamount in Mariana Forearc Crust Using Pressure Response to Tidal Loading
Method (Doctoral dissertation, University of Miami).
https://scholarship.miami.edu/esploro/outputs/991031448068902976

Federico, I., Pinardi, N., Coppini, G., Oddo, P., Lecci, R., and Mossa, M.
(2017). Coastal ocean forecasting with an unstructured grid model in the
southern Adriatic and northern Ionian seas. Natural Hazards and Earth System
Sciences, 17(1), 45-59. https://doi.org/10.5194/nhess-17-45-2017

Ferrarin, C., Roland, A., Bajo, M., Umgiesser, G., Cucco, A., Davolio, S.,
Buzzi, A., Malguzzi, P., and Drofa, O. (2013). Tide-surge-wave modelling and
forecasting in the Mediterranean Sea with focus on the Italian coast. Ocean
Modelling, 61, 38–48. https://doi.org/10.1016/j.ocemod.2012.10.003

Ferrarin, C., Zaggia, L., Paschini, E., Scirocco, T., Lorenzetti, G., Bajo, M.,
Penna, P., Francavilla, M., D’Adamo, R., and Guerzoni, S. (2013). Hydrological
Regime and Renewal Capacity of the Micro-tidal Lesina Lagoon, Italy. Estuaries
and Coasts, 37(1), 79–93. https://doi.org/10.1007/s12237-013-9660-x

Ferrarin, C., Tomasin, A., Bajo, M., Petrizzo, A., and Umgiesser, G. (2015).
Tidal changes in a heavily modified coastal wetland. Continental Shelf
Research, 101, 22–33. https://doi.org/10.1016/j.csr.2015.04.002

Gaeta, M. G., Samaras, A. G., Federico, I., Archetti, R., Maicu, F., and
Lorenzetti, G. (2016). A coupled wave–3-D hydrodynamics model of the Taranto
Sea (Italy): a multiple-nesting approach. Natural Hazards and Earth System
Sciences, 16(9), 2071–2083. https://doi.org/10.5194/nhess-16-2071-2016

Kay, S., Caesar, J., Wolf, J., Bricheno, L., Nicholls, R. J., Islam, A. S.,
Haque, A., Pardaens, A. and Lowe, J. A. (2015). Modelling the increased
frequency of extreme sea levels in the Ganges–Brahmaputra–Meghna delta due to
sea level rise and other effects of climate change. Environmental Science:
Processes and Impacts, 17(7), 1311-1322. https://doi.org/10.1039/C4EM00683F

Lavaud, L., Bertin, X., Martins, K., and Arnaud, G. (2019). The contribution of
short wave breaking in the storm surge associated with Klaus (January 24, 2009)
in the Southern Bay of Biscay. Coastal Sediments 2019.
https://doi.org/10.1142/9789811204487_0123

Neves, L. J. P. F., Barbosa, S. M., and Pereira, A. J. S. C. (2009). Indoor
radon periodicities and their physical constraints: a study in the Coimbra
region (Central Portugal). Journal of Environmental Radioactivity, 100(10),
896–904. https://doi.org/10.1016/j.jenvrad.2009.06.017

Pérez-Ruzafa, A., De Pascalis, F., Ghezzo, M., Quispe-Becerra, J. I.,
Hernández-García, R., Muñoz, I., Vergara, C., Pérez-Ruzafa, I. M., Umgiesser,
G., and Marcos, C. (2019). Connectivity between coastal lagoons and sea:
Asymmetrical effects on assemblages’ and populations’ structure. Estuarine,
Coastal and Shelf Science, 216, 171–186.
https://doi.org/10.1016/j.ecss.2018.02.031

Vergara-Chen, C., Pérez-Ruzafa, A., De Pascalis, F., Ghezzo, M.,
Quispe-Becerra, J. I., Hernández-García, R., Muñoz, I., Pérez-Ruzafa, I. M.,
Umgiesserb, G. and Marcos, C. (2018). Connectivity between coastal lagoons and
sea: Asymmetrical effects on assemblages' and populations' structure.
https://ridda2.utp.ac.pa/handle/123456789/4432

Vinas, K. A. (2013). Mariana forearc crust CORK pressure data: observations and
implications. University of Miami.
https://scholarship.miami.edu/esploro/outputs/991031448074702976

Žust, L., Fettich, A., Kristan, M., and Ličer, M. (2021). HIDRA 1.0:
deep-learning-based ensemble sea level forecasting in the northern Adriatic.
Geoscientific Model Development, 14(4), 2057–2074.
https://doi.org/10.5194/gmd-14-2057-2021

Please forward any citation of TAPPY to tim at cerazone.net.

Contributions
-------------
Any help is appreciated. Best would be a pull request on Github or Bitbucket or
if you would like to make a bunch of changes I can assign you developer
privileges to the source code repository. Just contact me at tim at
cerazone.net.
