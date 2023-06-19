#!/usr/bin/env python

import difflib
import glob
import os
import re
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path
from unittest import TestCase

# directory dance to find tappy.py module in directory above
# test_tappy.py
file_loc = Path(__file__).resolve()
cur_path = file_loc.parent


class TappyTest(TestCase):
    def setUp(self):
        self.cwd = Path.cwd()
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(self.tmpdir)
        open("debug_tappy", "a").close()
        for files in ["*.dat", "*.xml"]:
            for f in glob.glob(files):
                os.remove(f)
        ret = subprocess.call(
            [
                "tappy",
                "analysis",
                self.cwd / "example" / "mayport_florida_8720220_data.txt",
                #        '--zero_ts="transform"',
                "--outputts",
                '--outputxml="testout.xml"',
                #        '--filter="transform"',
                "--include_inferred",
            ]
        )
        print(ret)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmpdir)

    def test_constituents(self):
        os.chdir(self.tmpdir)
        for i in ["M2", "M8"]:
            alines = open(
                self.cwd / "tests" / "output_ts" / f"outts_{i}.dat"
            ).readlines()
            print(Path.cwd())
            print(glob.glob("*"))
            blines = open(Path(f"outts_{i}.dat")).readlines()
            d = difflib.Differ()
            result = list(d.compare(alines, blines))
            result = [i for i in result if i[0] in ["+", "-", "?"]]
            print(
                "".join(result),
            )
            self.assertEqual(result, [])

    def test_closure(self):
        os.chdir(self.tmpdir)
        inputf = self.cwd / "example" / "mayport_florida_8720220_data.txt"
        _ = subprocess.call(
            shlex.split(
                f"tappy analysis {inputf} --outputxml testout.xml --include_inferred"
            )
        )
        _ = subprocess.call(
            shlex.split(
                "tappy prediction testout.xml 2000-01-01T00:00:00 2000-02-01T00:00:00 60 --fname predict.out"
            )
        )
        def_filename = self.cwd / "tests" / "predict_def.out"
        _ = subprocess.call(
            shlex.split(
                f"tappy analysis predict.out --def_filename {def_filename} --outputxml testoutclosure.xml --include_inferred"
            )
        )
        print(os.getcwd())
        print(glob.glob("*"))
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
