#!/usr/bin/env python

"""
NAME:
    tappy.py

SYNOPSIS:
    tappy.py [options] filename

DESCRIPTION:
    Tidal Analysis Program in PYthon.

    Uses least squares fit to estimate tidal amplitude and phase.
    Specific to tides generated on Earth by the Moon and Sun.

EXAMPLES:
    1. As standalone
        tappy.py -d myfile
    2. As library
        import tappy
        ...

#Copyright (C) 2005  Tim Cera timcera@earthlink.net
#http://tappy.sourceforge.net
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


"""
import datetime

import numpy as np

from .utils import Tappy

deg2rad = np.pi / 180.0
rad2deg = 180.0 / np.pi


def analysis(
    data_filename,
    def_filename=None,
    quiet=False,
    debug=False,
    outputts=False,
    outputxml="",
    ephemeris=False,
    rayleigh=1.0,
    print_vau_table=False,
    missing_data="ignore",
    linear_trend=False,
    remove_extreme=False,
    zero_ts=None,
    filter=None,
    pad_filters=None,
    include_inferred=True,
    xmlname="A port in a storm",
    xmlcountry="A man without a country",
    xmllatitude=0.0,
    xmllongitude=0.0,
    xmltimezone="0000",
    xmlcomments="No comment",
    xmlunits="m",
    xmldecimalplaces="full",
):
    """Traditional analysis with separately calculated nodal factors.

     Constituent amplitude units are the same as the input heights.
     Constituent phases are based in the same time zone as the dates.

    Parameters
    ----------
    data_filename : str
        The time-series of elevations to be analyzed.  Can be a file name
        that is parsed with a companion definition file or a CSV, WDM,
        HDF5, or XLSX file.  The options for each file type are listed in
        "tstoolbox read --help" on the command line or "help(tstoolbox.read)
        in Python.
    def_filename : str, optional
        Contains the definition string to parse the input data.
    quiet : bool, optional
        Print nothing to the screen.
    debug : bool, optional
        Print debug messages.
    outputts : bool, optional
        Output time series for each constituent.
    ephemeris : bool, optional
        Print out ephemeris tables.
    rayleigh : float, optional
        The Rayleigh coefficient is used to compare against to determine
        time series length to differentiate between two frequencies.
        [default: default]
    missing_data : str, optional
        What should be done if there is missing data.  One of: fail, ignore,
        or fill. [default: default]
    linear_trend : bool, optional
        Include a linear trend in the least squares fit.
    remove_extreme : bool, optional
        Remove values outside of 2 standard deviations before analysis.
    zero_ts : str, optional
        Zero the input time series before constituent analysis by subtracting
        filtered data. One of: transform,usgs,doodson,boxcar
    filter : str, optional
        Filter input data set with tide elimination filters. The -o outputts
        option is implied. Any mix separated by commas and no spaces:
        transform,usgs,doodson,boxcar
    pad_filters : str, optional
        Pad input data set with values to return same size after filtering.
        Realize edge effects are unavoidable.  One of ["tide", "minimum",
        "maximum", "mean", "median", "reflect", "wrap"]
    include_inferred : bool, optional
        Do not incorporate any inferred constituents into the least squares
        fit.
    print_vau_table : bool, optional
        For debugging - will print a table of V and u values to compare
        against Schureman.
    outputxml : str, optional
        File name to output constituents as IHOTC XML format.
    xmlname : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Name of the
        station supplying the observations. [default: A port in a storm]
    xmlcountry : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Name of the
        country containing the station. Defaults to 'A man without a country'.
    xmllatitude : float, optional
        Not used in analysis. Used ONLY to complete the XML file. Latitude of
        the station. Defaults to 0.0.
    xmllongitude : float, optional
        Not used in analysis. Used ONLY to complete the XML file. Longitude of
        the station. Defaults to 0.0.
    xmltimezone : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Time zone of
        the station. Defaults to '0000'.
    xmlcomments : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Station
        comments. Defaults to 'No comment'.
    xmlunits : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Units of the
        observed water level. Defaults to 'm'.
    xmldecimalplaces : str, optional
        Not used in analysis. Used ONLY to complete the XML file. Format of the
        observed amplitude and phase. Default depends on length of analysis
        record.  'full' is the default and means that full accuracy, 'ihotc'
        is formatted according to IHOTC standard which severly limits the
        number of decimal places, and if an integer number lists the number
        of decimal places.
    """
    x = Tappy(
        outputts=outputts,
        outputxml=outputxml,
        quiet=quiet,
        debug=debug,
        ephemeris=ephemeris,
        rayleigh=rayleigh,
        print_vau_table=print_vau_table,
        missing_data=missing_data,
        linear_trend=linear_trend,
        remove_extreme=remove_extreme,
        zero_ts=zero_ts,
        filter=filter,
        pad_filters=pad_filters,
        include_inferred=include_inferred,
    )

    if ephemeris:
        x.print_ephemeris_table()
    if print_vau_table:
        x.print_v_u_table()

    x.open(data_filename, def_filename=def_filename)

    if x.missing_data == "fail":
        x.dates_filled, x.elevation_filled = x.missing(
            x.missing_data, x.dates, x.elevation
        )

    if x.remove_extreme:
        x.remove_extreme_values()

    package = x.astronomic(x.dates)
    (
        x.zeta,
        x.nu,
        x.nup,
        x.nupp,
        x.kap_p,
        x.ii,
        x.R,
        x.Q,
        x.T,
        x.jd,
        x.s,
        x.h,
        x.N,
        x.p,
        x.p1,
    ) = package

    if rayleigh:
        ray = float(rayleigh)
    else:
        ray = 1.0
    (x.speed_dict, x.key_list) = x.which_constituents(
        len(x.dates), package, rayleigh_comp=ray
    )
    if x.zero_ts:
        # FIX - have to run the constituents package here in order to have
        # filters available , and then run AGAIN later on.
        x.constituents()
        print(len(x.dates), len(x.elevation))
        x.dates_filled, x.elevation_filled = x.missing("fill", x.dates, x.elevation)
        print(len(x.dates_filled), len(x.elevation_filled))
        x.dates, filtered = x.filters(zero_ts, x.dates_filled, x.elevation_filled)
        print(len(x.dates), len(filtered))
        x.elevation = x.elevation_filled - filtered
        package = x.astronomic(x.dates)
        (
            x.zeta,
            x.nu,
            x.nup,
            x.nupp,
            x.kap_p,
            x.ii,
            x.R,
            x.Q,
            x.T,
            x.jd,
            x.s,
            x.h,
            x.N,
            x.p,
            x.p1,
        ) = package
        (x.speed_dict, x.key_list) = x.which_constituents(
            len(x.dates), package, rayleigh_comp=ray
        )

    x.constituents()

    if x.missing_data == "fill":
        x.dates_filled, x.elevation_filled = x.missing(
            x.missing_data, x.dates, x.elevation
        )
        x.write_file(x.dates_filled, x.elevation_filled, fname="outts_filled.dat")

    if x.filter:
        for item in x.filter.split(","):
            if item in (
                "mstha",
                "wavelet",
                "cd",
                "boxcar",
                "usgs",
                "doodson",
                "lecolazet1",
                "kalman",
                "transform",
            ):  # 'lecolazet', 'godin', 'sfa']:
                filtered_dates, result = x.filters(item, x.dates, x.elevation)
                x.write_file(filtered_dates, result, fname=f"outts_filtered_{item}.dat")
        (x.speed_dict, x.key_list) = x.which_constituents(
            len(x.dates), package, rayleigh_comp=ray
        )

    if not x.quiet:
        x.print_con()

    if x.outputts:
        for key in x.key_list:
            x.write_file(
                x.dates,
                x.sum_signals([key], x.dates, x.speed_dict),
                fname=f"outts_{key}.dat",
            )
            x.write_file(x.dates, x.speed_dict[key]["FF"], fname=f"outts_ff_{key}.dat")
        x.write_file(
            x.dates,
            x.sum_signals(x.key_list, x.dates, x.tidal_dict),
            fname="outts_total_tidal_components.dat",
        )
        x.write_file(x.dates, x.elevation, fname="outts_original.dat")

    if x.outputxml:
        import xml.etree.ElementTree as et

        def indent(elem, level=0):
            i = f"\n{level * '  '}"
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = f"{i}  "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i

        transfer = et.Element(
            "Transfer",
            attrib={
                "ns0:noNamespaceSchemaLocation": "HC_Schema_V1.xsd",
                "xmlns:ns0": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

        port = et.SubElement(transfer, "Port")

        name = et.SubElement(port, "name")
        name.text = xmlname

        country = et.SubElement(port, "country")
        country.text = xmlcountry

        position = et.SubElement(port, "position")

        latitude = et.SubElement(position, "latitude")
        latitude.text = str(xmllatitude)

        longitude = et.SubElement(position, "longitude")
        longitude.text = str(xmllongitude)

        timezone = et.SubElement(port, "timeZone")
        timezone.text = str(xmltimezone)

        units = et.SubElement(port, "units")
        units.text = str(xmlunits)

        observationstart = et.SubElement(port, "observationStart")
        observationstart.text = x.dates[0].isoformat()

        comments = et.SubElement(port, "comments")
        comments.text = xmlcomments

        observationend = et.SubElement(port, "observationEnd")
        observationend.text = x.dates[-1].isoformat()

        ndict = {"Z0": 0.0}
        for k in x.key_list + x.inferred_key_list:
            ndict[k] = x.tidal_dict[k]["speed"]
        klist = [i[0] for i in x.sortbyvalue(ndict)]

        if xmldecimalplaces == "ihotc":
            ampformatstr = "{0:.3f}"
            phaformatstr = "{0:.1f}"
            daterange = x.dates[-1] - x.dates[0]
            if daterange < datetime.timedelta(days=90):
                ampformatstr = "{0:.2f}"
                phaformatstr = "{0:.0f}"
        elif xmldecimalplaces == "full":
            ampformatstr = "{0}"
            phaformatstr = ampformatstr
        else:
            ampformatstr = f"{{0:.{xmldecimalplaces}f}}"
            phaformatstr = ampformatstr

        for key in klist:
            if key in x.key_list:
                if float(ampformatstr.format(x.r[key])) == 0.0:
                    continue
            elif key in x.inferred_key_list:
                if float(ampformatstr.format(x.inferred_r[key])) == 0.0:
                    continue

            tmp = et.SubElement(port, "Harmonic")

            hname = et.SubElement(tmp, "name")
            hname.text = key

            speed = et.SubElement(tmp, "speed")
            inferred = et.SubElement(tmp, "inferred")
            phaseangle = et.SubElement(tmp, "phaseAngle")
            amplitude = et.SubElement(tmp, "amplitude")

            if key in x.key_list:
                inferred.text = "false"
                amplitude.text = ampformatstr.format(x.r[key])
                phaseangle.text = phaformatstr.format(x.phase[key])
                speed.text = str(x.tidal_dict[key]["speed"] * rad2deg)
            elif key in x.inferred_key_list:
                inferred.text = "true"
                amplitude.text = ampformatstr.format(x.inferred_r[key])
                phaseangle.text = phaformatstr.format(x.inferred_phase[key])
                speed.text = str(x.tidal_dict[key]["speed"] * rad2deg)
            elif key == "Z0":
                inferred.text = "false"
                amplitude.text = ampformatstr.format(x.fitted_average)
                phaseangle.text = phaformatstr.format(0.0)
                speed.text = "0.0"

        indent(transfer)
        tree = et.ElementTree(transfer)
        tree.write(x.outputxml)
