#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import string

import scipy as N

filename = "mayport_florida_8720220_data.txt"

fp = open(filename, "r")
fp.readline()
elevation = []
dates = []
for line in fp:
    words = string.split(line)
    elevation.append(float(words[3]))

    dt = [int(i) for i in string.split(words[1], "/")]
    hr = [int(i) for i in string.split(words[2], ":")]
    dates.append(datetime.datetime(dt[2], dt[1], dt[0], hr[0], hr[1]))

elevation = N.array(elevation)

fpo = open("mayport_xmgrace.dat", "w")
for index, d in enumerate(dates):
    fpo.write(f"{d.isoformat()} {elevation[index]:f}\n")

con = N.convolve(elevation, [1.0 / 25.0] * 25, mode=1)

fpo = open("mayport_xmgrace_data_convolved.dat", "w")
for index, d in enumerate(dates):
    fpo.write(f"{d.isoformat()} {elevation[index] - con[index]:f}\n")
