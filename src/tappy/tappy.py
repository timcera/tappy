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

# ===imports======================
import sys
from pathlib import Path

import numpy as np

from .analysis import analysis
from .prediction import prediction
from .toolbox_utils.src.toolbox_utils import tsutils

# ===globals======================
modname = "tappy"

debug_p = 0

deg2rad = np.pi / 180.0
rad2deg = 180.0 / np.pi


def main():
    """Set debug and run cltoolbox.main function."""
    if not Path("debug_tappy").exists():
        sys.tracebacklimit = 0
    import cltoolbox

    # ====================================
    @cltoolbox.command("prediction")
    @tsutils.copy_doc(prediction)
    def prediction_cli(
        xml_filename, start_date, end_date, interval, include_inferred=True, fname="-"
    ):
        prediction(
            xml_filename,
            start_date,
            end_date,
            interval,
            include_inferred=include_inferred,
            fname=fname,
        )

    # =============================
    @cltoolbox.command("analysis")
    @tsutils.copy_doc(analysis)
    def analysis_cli(
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
        print(
            analysis(
                data_filename,
                def_filename=def_filename,
                quiet=quiet,
                debug=debug,
                outputts=outputts,
                outputxml=outputxml,
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
                xmlname=xmlname,
                xmlcountry=xmlcountry,
                xmllatitude=xmllatitude,
                xmllongitude=xmllongitude,
                xmltimezone=xmltimezone,
                xmlcomments=xmlcomments,
                xmlunits=xmlunits,
                xmldecimalplaces=xmldecimalplaces,
            )
        )

    cltoolbox.main()


if __name__ == "__main__":
    main()
