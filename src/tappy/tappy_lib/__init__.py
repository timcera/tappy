# -*- coding: utf-8 -*-
import os
import sys

ced = os.path.abspath(os.sep.join(__path__))
sys.path.insert(0, ced)

ced = os.path.abspath(os.sep.join(__path__ + ["astronomia"]))
sys.path.insert(0, ced)

os.environ["TAPPY_LIB"] = os.sep.join(__path__)
