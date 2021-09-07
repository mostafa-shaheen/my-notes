#replace printing
import time
for t in range(100):
  print('step:',t,end='')
  time.sleep(1)#whatever is hapenning here
  print('\r',end='')
#or use std.out.flush  
=============================================================================== 
#print numby array with rounded values
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(np.array([1.6559995,.015995]))
===============================================================================
pytorch use .detach() when using calculated targets in loss functions
===============================================================================
#download dataset from kaggle 
import os
os.environ['KAGGLE_USERNAME'] = "mostafa77" # username from the json file
os.environ['KAGGLE_KEY'] = "347368f5c64dba7e88eaa79d996db0ec" # key from the json file
!kaggle competitions download favorita-grocery-sales-forecasting -f test.csv.7z
================================================================================
# get the path from where a package was imported
import package_name
print(package_name.__file__)
================================================================================
#  import from parent directory by adding it's path 
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
================================================================================
# auto reload, no need for restarting kernel
%load_ext autoreload
%autoreload 2
================================================================================
# know python version you'r working with
from platform import python_version
print(python_version())
================================================================================
# check system path where python imports from 
import sys
print(sys.path)
#insert path with the first priority, (checked at first)
sys.path.insert(0, any_path)
#insert path with the least priority, (checked at last)
sys.path.append(any_path)
================================================================================
#Autocomplete (with hinterland) in Jupyter notebook not working
%config Completer.use_jedi = False
