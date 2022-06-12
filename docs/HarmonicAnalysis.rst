Harmonic Analysis
-----------------

The equation that defines the water level changes due to tide is:

.. math::
    \widehat{h} = H_0 + \sum_{i=1}^n {\widehat{f_i} H_i \cos \left ( a_i \widehat{t} - \left ( \kappa_i - \left [ V_o + \mu \right ]_i \right ) \right )}\\

.. math::
    where:\\
    \widehat{h} &=\mbox{measured water level (1 dimensional array)}\\
    H_0 &=\mbox{average water level}\\
    n &=\mbox{number of constituents}\\
    \widehat{f_i} &=\mbox{nodal factor for constituent }i\mbox{ (1 dimensional array)}\\
    H_i &=\mbox{amplitude of constituent }i\\
    a_i &=\mbox{speed of constituent }i\\
    \widehat{t} &=\mbox{time (1 dimensional array)}\\
    \kappa_i &=\mbox{phase angle of constituent }i\\
    \left [ V_o + \mu \right ] &=\mbox{equilibrium argument for constituent }i

Typical tidal analysis programs specify the node factor at the center of
the analyzed time-series. I think this is something that is true for a
29-day series, but for longer analysis, the node factor at each
measurement should be calculated. This is what TAPPY does.
