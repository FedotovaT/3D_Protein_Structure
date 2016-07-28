Introduction

Building 3D protein structures based on homology modeling using Python (Modeller).

System requirements

Modeller is doing majority of the 3D modeling steps. The computer should have fast processor to get the job done 
in reasonable timeframe. In order to verify protein sequences and allignment the internet connection will be required.

Installation

1. Go to Modeller website https://salilab.org/modeller/download_installation.html and install Modeller.
2. Request a liscence key (free for non-profit institutions).
3. Start Modeller via command line prompt.

3D protein structure modeling

1. Find pdb file of the reference protein (#protein dga) in Protein Data Bank and download it.
2. Align sequence of your protein of interest (#dgat) with the dga protein sequence (#in most cases, sequences should 
3. have more than 70% of homology for the accurate generation of 3D model). Use any alignment tools available.
3. Generate model.py file (#model-dgat.py).
4. Generate sequence alignment file (#dga-dgat.ali).
5. Run script to generate your (#dgat.pdb) structure.

