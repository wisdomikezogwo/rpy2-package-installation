#########################################################################
import rpy2
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
import rpy2.robjects.numpy2ri as rpyn #rpyn here converts the object to a usable numpy object.
from rpy2.robjects.packages import importr
utils = rpackages.importr('utils')
rpy2.robjects.numpy2ri.activate()
##########################################################################
package_name = "analytics"
try:
    analytics = importr(package_name)
except:
    robjects.r(f'install.packages("{package_name}")')
    analytics = importr(package_name)
###########################################################################
#utils.install_packages("analytics")
"""This will install the package: analytics and all its dependencies"""
###########################################################################
#R = rpy2.robjects.r
#analytics = importr('analytics')
"""
This line is similar to pythons:
    import analytics 
If only analytics was a pip package, but its not, its an R package
"""
###########################################################################
'''
Original:
weakly.stationary(tseries, signific_gen = 0.05, signific_pp.df = 0.05,
MK = FALSE, BP = TRUE, PSR = TRUE, weak.dep = FALSE,
mode = "neutral")

PS:  . in R is _ in rpy2, i.e weakly.stattionarity becomes weakly_stationarity.
NEW:
ws = rpyn.ri2py(analytics.weakly_stationary(tseries, signific_gen = 0.05, signific_pp_df = 0.05,
                                                 MK = FALSE, BP = TRUE, PSR = TRUE, weak_dep = FALSE,
                                                 mode = "neutral"))
'''
