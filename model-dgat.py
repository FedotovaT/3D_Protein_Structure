
from modeller import *              
from modeller.automodel import *    

log.verbose()    
env = environ()  

env.io.atom_files_directory = 'C:\Structure\dga'

a = automodel(env,
              alnfile  = 'dga.dgat.ali',     
              knowns   = 'dga',              
              sequence = 'dgat')              
a.starting_model= 1                 
a.ending_model  = 1                 
                                    
a.make()                            # homology modeling