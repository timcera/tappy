TAPPy has two options for dealing with missing values, the default is to
ignore them.

The ‘-m fill’ option will fill the missing values with the signal
created from the sum of the tidal constituent signals.

The ‘-m fail’ option will stop TAPPy.

The fill option has some problems, but in general terms, the performance
improves if the missing time span is short and the time-series itself is
lengthy.

[[img src=missing.png]]
