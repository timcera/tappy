
# shellcheck disable=SC2129

rm citation.txt
touch citation.txt

echo "Akmal, P. N. E., (2013). Determination of the Permeability of the South Chamorro Seamount in Mariana Forearc Crust Using Pressure Response to Tidal Loading Method. University of Miami. https://scholarship.miami.edu/esploro/outputs/991031448068902976
" >> citation.txt

echo "Barbosa, S. M., (2009). Analysis of trends in North Atlantic tidal amplitudes University of Porto, Portugal (susana.barbosa@fc.up.pt) http://meetingorganizer.copernicus.org/EGU2009/EGU2009-5154.pdf
" >> citation.txt

echo "Bechet, V., Verstraeten, E., Hanert, E. & Deleersnijder, E., (2018). Multiple-year marine connectivity modeling in the Florida Coral Reef Tract to assess Acropora Cervicornis recovery. (Unpublished master’s thesis). Ecole polytechnique de Louvain, Université catholique de Louvain.
" >> citation.txt

# Becker
cite --style apa https://doi.org/10.1029/2022GC010496 >> citation.txt

echo "Billings, W. Z., (2018). An Exploration of the Two-Dimensional Poroelastic Properties of Oceanic Crust at the Formation Scale.  University of Miami ProQuest Dissertations Publishing,  10846298.
" >> citation.txt

# Campos
cite --style apa https://doi.org/10.1016/j.rsma.2022.102336 >> citation.txt

# Cucco
cite --style apa https://doi.org/10.3390/jmse10070941 >> citation.txt

# Davis
cite --style apa https://doi.org/10.1029/2023GC010910 >> citation.txt

echo "Desmet, N., (2019). Modelling coral larvae exchanges between the Great Barrier Reef and outer reefs. Ecole polytechnique de Louvain, Université catholique de Louvain. Prom. : Hanert, Emmanuel ; Deleersnijder, Eric. http://hdl.handle.net/2078.1/thesis:19591
" >> citation.txt

# Ferrarin
cite --style apa https://doi.org/10.1016/j.ocemod.2012.10.003 >> citation.txt

# Ferrarin
cite --style apa https://doi.org/10.1007/s12237-013-9660-x >> citation.txt

# Ferrarin
cite --style apa https://doi.org/10.1016/j.csr.2015.04.002 >> citation.txt

# Gaeta
cite --style apa https://doi.org/10.5194/nhess-16-2071-2016 >> citation.txt

# commented out because makes everything uppercase
# cite --style apa https://doi.org/10.1142/9789811204487_0123 >> citation.txt
# entered manually below:
echo "Lavaud, L., Bertin, X., Martins, K., & Arnaud, G. (2019). The contribution of short wave breaking in the storm surge associated with Klaus (January 24, 2009) in the Southern Bay of Biscay. Coastal Sediments 2019. https://doi.org/10.1142/9789811204487_0123
" >> citation.txt

# Neves
cite --style apa https://doi.org/10.1016/j.jenvrad.2009.06.017 >> citation.txt

# Pérez-Ruzafa
cite --style apa https://doi.org/10.1016/j.ecss.2018.02.031 >> citation.txt

echo "Vergara-Chen, C., Pérez-Ruzafa, A., De Pascalis, F., Ghezzo, M., Quispe-Becerra, J. I., Hernández-García, R., Muñoz, I., Pérez-Ruzafa, I. M., Umgiesserb, G. and Marcos, C., (2018). Connectivity between coastal lagoons and sea: Asymmetrical effects on assemblages' and populations' structure. https://ridda2.utp.ac.pa/handle/123456789/4432
" >> citation.txt

echo "Vinas, K. A., (2013). Mariana forearc crust CORK pressure data: observations and implications. University of Miami. https://scholarship.miami.edu/esploro/outputs/991031448074702976
" >> citation.txt

# Žust
cite --style apa https://doi.org/10.5194/gmd-14-2057-2021 >> citation.txt

fmt -w 80 citation.txt > tmp.txt
mv tmp.txt citation.txt
