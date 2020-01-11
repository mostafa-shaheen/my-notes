#replace printing
for t in range(100):
  print('time step: ',t,'\r', end="")
#or use std.out.flush  
  
#print numby array with rounded values
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(np.array([1.6559995,.015995]))

