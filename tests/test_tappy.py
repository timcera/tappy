#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import glob
import os
import os.path
import re
import shlex
import shutil
import string
import subprocess
import tempfile
import unittest

# directory dance to find tappy.py module in directory above
# test_tappy.py
file_loc = os.path.abspath(__file__)
cur_path = os.path.dirname(file_loc)

_cwd = os.getcwd()


class TappyTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(self.tmpdir)
        for files in ["*.dat", "*.xml"]:
            for f in glob.glob(files):
                os.remove(f)
        self.con_output1 = subprocess.Popen(
            [
                "tappy",
                "analysis",
                os.path.join(
                    _cwd,
                    "example",
                    "mayport_florida_8720220_data.txt",
                ),
                #        '--zero_ts="transform"',
                "--outputts",
                '--outputxml="testout.xml"',
                #        '--filter="transform"',
                "--include_inferred",
            ],
            stdout=subprocess.PIPE,
        )
        sts = os.waitpid(self.con_output1.pid, 0)[1]

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_constituents(self):
        os.chdir(self.tmpdir)
        for i in ["M2", "M8"]:
            alines = open(
                os.path.join(_cwd, "tests", "output_ts", f"outts_{i}.dat")
            ).readlines()
            blines = open(os.path.join(f"outts_{i}.dat")).readlines()
            d = difflib.Differ()
            result = list(d.compare(alines, blines))
            result = [i for i in result if i[0] in ["+", "-", "?"]]
            print(
                "".join(result),
            )
            self.assertEqual(result, [])

    def test_closure(self):
        os.chdir(self.tmpdir)
        inputf = os.path.join(_cwd, "example", "mayport_florida_8720220_data.txt")
        self.con_output1 = subprocess.call(
            shlex.split(
                f"tappy analysis {inputf} --outputxml testout.xml --include_inferred"
            )
        )
        self.con_output2 = subprocess.call(
            shlex.split(
                f"tappy prediction testout.xml 2000-01-01T00:00:00 2000-02-01T00:00:00 60 --fname predict.out"
            )
        )
        def_filename = os.path.join(_cwd, "tests", "predict_def.out")
        self.con_output3 = subprocess.call(
            shlex.split(
                f"tappy analysis predict.out --def_filename {def_filename} --outputxml testoutclosure.xml --include_inferred"
            )
        )
        alines = open("testout.xml").readlines()
        blines = open("testoutclosure.xml").readlines()
        nalines = []
        for a in alines:
            match = re.search(r"[0-9\.]+", a)
            if match is not None:
                nalines.append(str(round(float(match.group()), 2)))
        nblines = []
        for b in blines:
            match = re.search(r"[0-9\.]+", b)
            if match is not None:
                nblines.append(str(round(float(match.group()), 2)))
        d = difflib.Differ()
        result = list(d.compare(nalines, nblines))
        result = [i for i in result if i[0] in ["+", "-", "?"]]
        print(
            "".join(result),
        )
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
