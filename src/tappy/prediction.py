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
from contextlib import suppress

import numpy as np

from .utils import Util

deg2rad = np.pi / 180.0
rad2deg = 180.0 / np.pi


def prediction(
    xml_filename, start_date, end_date, interval, include_inferred=True, fname="-"
):
    """Prediction based upon earlier constituent analysis saved in IHOTC XML transfer format.

    Parameters
    ----------
    xml_filename : str
        The tidal constituents in IHOTC XML transfer format.
    start_date : str
        The start date as a ISO 8601 string. '2010-01-01T00:00:00'
    end_date : str
        The end date as a ISO 8601 string. '2011-01-01T00:00:00:00'
    interval : int
        The interval as the number of minutes.
    include_inferred : bool, optional
        Include the inferred constituents.
    fname : str, optional
        Output filename, default is '-' to print to screen.
    """
    import xml.etree.ElementTree as et

    tree = et.parse(xml_filename)
    root = tree.getroot()
    rin = {}
    phasein = {}
    skey_list = []
    for constituent in root.iter("Harmonic"):
        inf = constituent.findtext("inferred")
        if (not include_inferred) and (inf.lower() == "true"):
            continue
        nam = constituent.findtext("name")
        amp = constituent.findtext("amplitude")
        pha = constituent.findtext("phaseAngle")
        rin[nam] = float(amp)
        phasein[nam] = float(pha)
        skey_list.append(nam)

    u = Util(rin, phasein)
    u.dates = [datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")]
    delta = datetime.timedelta(minutes=int(interval))
    nextdate = u.dates[0] + delta
    end_date = datetime.datetime.strptime(
        end_date, "%Y-%m-%dT%H:%M:%S"
    ) + datetime.timedelta(minutes=1)
    while nextdate < end_date:
        u.dates.append(nextdate)
        nextdate = u.dates[-1] + delta

    package = u.astronomic(u.dates)
    (zeta, nu, nup, nupp, kap_p, ii, R, Q, T, u.jd, s, h, Nv, p, p1) = package

    # Should change this - runs ONLY to get tidal_dict filled in...
    (_, key_list) = u.which_constituents(len(u.dates), package)

    prediction = 0.0
    with suppress(KeyError):
        prediction = rin["Z0"]

    with suppress(ValueError):
        skey_list.remove("Z0")

    calcdates = (
        np.array(list(range(len(u.dates))), dtype=np.float64) * float(interval) / 60.0
    )
    prediction = prediction + u.sum_signals(skey_list, calcdates, u.tidal_dict)

    u.write_file(u.dates, prediction, fname=fname)
