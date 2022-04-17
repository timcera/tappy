Typically the node factor from the middle of the time series is used for
tidal analysis. This is fine for relatively short time series. TAPPy
actually calculates the node factor for each point in the time series
and is therefore suited to long time series. TAPPy will also only report
the tidal constituents that can be resolved based on the length of the
input time series.

[TOC]

Input Data
----------

The input data can be in almost any text form as long as each line has
either (‘year’, ‘month’, ‘day’, ‘hour’, optional[‘minute’, ‘second’]) OR
a single real or integer number representing time since an origin, and
‘water elevation’. Time can be to any standard, though UTC is preferred.
TAPPy will maintain the input time throughout the analysis, but the only
way to calculate phases to compare against other tidal constituents is
to use UTC. The units for the water elevation can be anything and the
output amplitude will be in the input units.

Definition File
---------------

The glue that binds the input format to TAPPy is a definition file. It
is easy to understand and implement. Basically it tells TAPPy how to
parse the input data file. Delimiters and white space are ignored,
actually anything in the way of TAPPy finding the next value is ignored.

The definition file is a Python file (though with a .def extension) that
specifies the order that values can be found on each line. Two variables
are set within the definition file, ‘decimal_sep’ and ‘parse’. The
‘decimal_sep’ is set to the separator that marks the decimal part of a
real number. In most of Europe this would be a “,” whereas for the
United States it is a “.”. The ‘parse’ variable is where the magic
happens. It is an ordered list of Python functions that retrieve and
name values from each line in the order specified. TAPPy requires the
following named values; ‘water_level’, and either ‘datetime’ or the
group of (‘year’, ‘month’, ‘day’, ‘hour’, ‘minute’, ‘second’). If the
later selection to define the time stamp is used and ‘minute’ and
‘second’ are not specified they are both set to zero. All other names
(like ‘state’ and ‘station’ in the example below) are parsed, but
ignored by TAPPy.

Example Definition File
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <th>

Definition File

.. raw:: html

   </th>

.. raw:: html

   <th>

Matching Data File

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

You need to specify the separator between 
=========================================

the integer part and the decimal 
================================

part of real numbers, even if you only 
======================================

have integers in your data file. 
================================

decimal_sep = “.” # TAPPy needs the variables ‘year’, ‘month’, # ‘day’,
‘hour’, ‘minute’, ‘water_level’. # Any other variable name can be used
as a # placeholder. parse = [ integer(‘state’, exact=3),
integer_as_string(‘station’, exact=4), positive_integer(‘year’,
exact=4), positive_integer(‘month’, exact=2), positive_integer(‘day’,
exact=2), positive_integer(‘hour’), positive_integer(‘minute’),
positive_integer(‘toss’), real(‘water_level’), ]

.. raw:: html

   </td>

.. raw:: html

   <td>

Station Date Time Pred 6 Vrfy 6 DCP#: 1 Units: Feet Feet Data%: MLLW GMT
100.00 100.00 Maximum: 5.00 Minimum: -0.91 "“——- ——– —– ——- ——-”"
8721604 20061109 00:00 2.03 2.23 8721604 20061109 00:06 2.11 2.32
8721604 20061109 00:12 2.19 2.38 8721604 20061109 00:18 2.28 2.41
8721604 20061109 00:24 2.36 2.55 …

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

The example definition file above would correctly parse the data format
used by COOPS. `Example data for Trident Pier, Florida, USA from
COOPS. <http://tidesandcurrents.noaa.gov/data_menu.shtml?bdate=20061109&bdate_Month=10&edate=20061210&edate_Month=11&wl_sensor_hist=W1&relative=&datum=6&unit=1&shift=g&stn=8721604+Trident+Pier%2C+FL&type=Historic+Tide+Data&format=View+Data>`__

List of functions that can appear in the definition file.

+----------------------------------------------------+-----------------+
| Function name                                      | Find the next … |
+====================================================+=================+
| integer(name, minimum=1, maximum=None, exact=None) | integer         |
+----------------------------------------------------+-----------------+
| positive_integer(name, minimum=1, maximum=None,    | positive        |
| exact=None)                                        | integer (‘+’ is |
|                                                    | optional)       |
+----------------------------------------------------+-----------------+
| negative_integer(name, minimum=1, maximum=None,    | negative        |
| exact=None)                                        | integer         |
+----------------------------------------------------+-----------------+
| real(name)                                         | real            |
+----------------------------------------------------+-----------------+
| real_as_datetime(‘datetime’,                       | indexed time,   |
| origin=datetime.datetime(1900,1,1), unit=‘days’)   | (days since… or |
|                                                    | hours since…)   |
|                                                    | origin and unit |
|                                                    | have to be      |
|                                                    | compatible with |
|                                                    | Python          |
|                                                    | datetime. The   |
|                                                    | name will       |
|                                                    | always be       |
|                                                    | ‘datetime’.     |
+----------------------------------------------------+-----------------+
| integer_as_datetime(‘datetime’, minimum=1,         | indexed time    |
| maximum=None, exact=None,                          | (days since… or |
| origin=datetime.datetime(1900,1,1), unit=‘days’)   | hours since…),  |
|                                                    | origin and unit |
|                                                    | have to be      |
|                                                    | compatible with |
|                                                    | Python          |
|                                                    | datetime. The   |
|                                                    | name will       |
|                                                    | always be       |
|                                                    | ‘datetime’.     |
+----------------------------------------------------+-----------------+
| positive_real(name)                                | positive real   |
|                                                    | (‘+’ is         |
|                                                    | optional)       |
+----------------------------------------------------+-----------------+
| negative_real(name)                                | negative real   |
+----------------------------------------------------+-----------------+
| number(name)                                       | an integer or a |
|                                                    | real            |
+----------------------------------------------------+-----------------+
| number_as_real(name)                               | an integer or a |
|                                                    | real, converted |
|                                                    | to a real using |
|                                                    | float()         |
+----------------------------------------------------+-----------------+
| number_as_integer(name)                            | an integer or a |
|                                                    | real, converted |
|                                                    | to an integer   |
|                                                    | using int()     |
+----------------------------------------------------+-----------------+

Additional general purpose parsing functions probably not useful to
TAPPy users.

+--------------------------------+-------------------------------------+
| Function name                  | Find the next …                     |
+================================+=====================================+
| real_as_string(name)           | real, but return as a string        |
+--------------------------------+-------------------------------------+
| integer_as_string(name,        | integer, but return as string       |
| minimum=1, maximum=None,       |                                     |
| exact=None)                    |                                     |
+--------------------------------+-------------------------------------+
| qstring(name)                  | quoted string (single or double)    |
+--------------------------------+-------------------------------------+
| delimited_as_string(name)      | any group of letters and/or numbers |
+--------------------------------+-------------------------------------+
| string(name, exact=None)       | any group of letters, numbers,      |
|                                | and/or spaces                       |
+--------------------------------+-------------------------------------+
| number_as_string(name)         | and number as string                |
+--------------------------------+-------------------------------------+
| insert(name, value)            | sets name to value                  |
+--------------------------------+-------------------------------------+

Filters
-------

[CompareTidalFilters]

Command Line Arguments
----------------------

Subcommands
~~~~~~~~~~~

::

   tappy.py


   Usage: /usr/bin/tappy.py COMMAND &lt;options&gt;

   Available commands:

    analysis     Traditional analysis with separately calculated nodal factors.
                 Constituent amplitude units are the same as the input heights.
                 Constituent phases are based in the same time zone as the
                 dates.
    prediction   Prediction based upon earlier constituent analysis saved in
                 IHOTC XML transfer format.
    writeconfig  OVERWRITES an ini style config file that holds all of default
                 the command line options.

   Use "/usr/bin/tappy.py &lt;command&gt; --help" for individual command help.

Analysis Arguments
~~~~~~~~~~~~~~~~~~

::

   tappy.py analysis --help


   Usage: /usr/bin/tappy.py analysis &lt;data_filename&gt; [&lt;def_filename&gt;] [&lt;config&gt;] [&lt;quiet&gt;] [&lt;debug&gt;] [&lt;outputts&gt;] [&lt;outputxml&gt;] [&lt;ephemeris&gt;] [&lt;rayleigh&gt;] [&lt;print_vau_table&gt;] [&lt;missing_data&gt;] [&lt;linear_trend&gt;] [&lt;remove_extreme&gt;] [&lt;zero_ts&gt;] [&lt;filter&gt;] [&lt;pad_filters&gt;] [&lt;include_inferred&gt;] [&lt;xmlname&gt;] [&lt;xmlcountry&gt;] [&lt;xmllatitude&gt;] [&lt;xmllongitude&gt;] [&lt;xmltimezone&gt;] [&lt;xmlcomments&gt;] [&lt;xmlunits&gt;] [&lt;xmldecimalplaces&gt;]

   Traditional analysis with separately calculated nodal factors. Constituent
   amplitude units are the same as the input heights. Constituent phases are
   based in the same time zone as the dates.

   Required Arguments:

     data_filename     The time-series of elevations to be analyzed.

   Options:

      --rayleigh          The Rayleigh coefficient is used to compare against
                          to determine time series length to differentiate
                          between two frequencies. [default: default]

      --xmlunits          Not used in analysis. Used ONLY to complete the XML
                          file. Units of the observed water level. Defaults to
                          'm'.

      --xmllongitude      Not used in analysis. Used ONLY to complete the XML
                          file. Longitude of the station. Defaults to 0.0.

      --missing_data      What should be done if there is missing data. One of:
                          fail, ignore, or fill. [default: default]

      --ephemeris         Print out ephemeris tables.

      --zero_ts           Zero the input time series before constituent
                          analysis by subtracting filtered data. One of:
                          transform,usgs,doodson,boxcar

      --pad_filters       Pad input data set with values to return same size
                          after filtering. Realize edge effects are
                          unavoidable. One of ["tide", "minimum", "maximum",
                          "mean", "median", "reflect", "wrap"]

      --xmldecimalplaces  Not used in analysis. Used ONLY to complete the XML
                          file. Format of the observed amplitude and phase.
                          Default depends on length of analysis record.

      --xmlname           Not used in analysis. Used ONLY to complete the XML
                          file. Name of the station supplying the observations.
                          Defaults to 'A port in a storm'.

      --config            Read command line options from config file, override
                          config file entries on the command line.

      --def_filename      Containes the definition string to parse the input
                          data.

      --xmlcountry        Not used in analysis. Used ONLY to complete the XML
                          file. Name of the country containing the station.
                          Defaults to 'A man without a country'.

      --xmltimezone       Not used in analysis. Used ONLY to complete the XML
                          file. Time zone of the station. Defaults to '0000'.

      --include_inferred  Do not incorporate any inferred constituents into the
                          least squares fit.

      --xmllatitude       Not used in analysis. Used ONLY to complete the XML
                          file. Latitude of the station. Defaults to 0.0.

      --linear_trend      Include a linear trend in the least squares fit.

      --outputts          Output time series for each constituent.

      --xmlcomments       Not used in analysis. Used ONLY to complete the XML
                          file. Station comments. Defaults to 'No comment'.

      --quiet             Print nothing to the screen.

      --print_vau_table   For debugging - will print a table of V and u values
                          to compare against Schureman.

      --filter            Filter input data set with tide elimination filters.
                          The -o outputts option is implied. Any mix separated
                          by commas and no spaces:
                          transform,usgs,doodson,boxcar

      --remove_extreme    Remove values outside of 2 standard deviations before
                          analysis.

      --outputxml         File name to output constituents as IHOTC XML format.

      --debug             Print debug messages.


   (specifying a single hyphen (-) in the argument list means all
   subsequent arguments are treated as bare arguments, not options)

Prediction Arguments
~~~~~~~~~~~~~~~~~~~~

::

   tappy.py prediction --help


   Usage: /usr/bin/tappy.py prediction &lt;xml_filename&gt; &lt;start_date&gt; &lt;end_date&gt; &lt;interval&gt; [&lt;include_inferred&gt;] [&lt;fname&gt;]

   Prediction based upon earlier constituent analysis saved in IHOTC XML
   transfer format.

   Required Arguments:

     xml_filename     The tidal constituents in IHOTC XML transfer format.

     start_date       The start date as a ISO 8601 string. '2010-01-01T00:00:00'

     end_date         The end date as a ISO 8601 string. '2011-01-01T00:00:00:00'

     interval         The interval as the number of minutes.

   Options:

      --fname             Output filename, default is '-' to print to screen.

      --include_inferred  Include the inferred constituents.


   (specifying a single hyphen (-) in the argument list means all
   subsequent arguments are treated as bare arguments, not options)
