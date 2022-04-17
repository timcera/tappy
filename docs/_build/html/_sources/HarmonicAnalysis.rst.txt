The equation that defines the water level changes due to tide is:

<math> :raw-latex:`\widehat{h}` = H_0 + :raw-latex:`\sum`\_{n}
:raw-latex:`\widehat{f}`\_n H_n
:raw-latex:`\cos{\left[ a_n \widehat{t} - \left( \kappa_n - \left[ V_0 + \mu \right]_n \right) \right]}`
</math>

<math>
:raw-latex:`\begin{align} \widehat{h} &amp;=&amp; \mbox{measured water level (1 dimensional array)} \\\ H_0 &amp;=&amp; \mbox{average water level} \\\ n &amp;=&amp; \mbox{number of tidal constituents analyzed} \\\ \widehat{f}_n &amp;=&amp; \mbox{node factor for constituent }n \mbox{ (1 dimensional array)} \\\ H_n &amp;=&amp; \mbox{amplitude of constituent }n \\\ a_n &amp;=&amp; \mbox{speed of constituent }n \\\ \widehat{t} &amp;=&amp; \mbox{time (1 dimensional array)} \\\ \kappa_n &amp;=&amp; \mbox{phase angle of constituent }n \\\ \left[V_0+\mu\right]_n &amp;=&amp; \mbox{equilibrium argument for constituent }n \\\ \end{align}`
</math>

Typical tidal analysis programs specify the node factor at the center of
the analyzed time-series. I think this is something that is true for a
29-day series, but for longer analysis, the node factor at each
measurement should be calculated. This is what TAPPY does.
