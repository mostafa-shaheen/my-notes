#replace printing
for t in range(100):
  print('time step: ',t,'\r', end="")
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
