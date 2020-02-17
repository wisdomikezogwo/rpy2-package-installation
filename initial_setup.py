author = 'Wisdom Ikezogwo'

#########################################################################
import rpy2.robjects.packages as rpackages
utils = rpackages.importr('utils')

utils.install_packages("analytics")

"""This will install the package: analytics and all its dependencies"""
###########################################################################
'''

There would be a prompt to chose your mirror to downlaod from, and I believe Algeria is a good one
if there is a TCL error run in the terminal and rerun the file:
conda install -c conda-forge r-tcltk2
'''



