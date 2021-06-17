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
=================================================================================
# display multiple dataframes in loop
from IPython.display import display
for i in df_list:
    display(i)
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
# know python version you'r working with
from platform import python_version
print(python_version())
