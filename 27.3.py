import matplotlib.pyplot as pit
import numpy as np # math stuff dont ask me
import pandas as pd # idk probly just adding a panda



#sinus graph

x=np.arange(0,10,0.1)#needs to be imported 1. parameter -number is included 2. parameter is not included 3. parameter id the step for each action example (0,10,1) it will go by 1 from 1 to 9
y=np.sin(x)

z=np.arange(0,10,0.1)
w=np.cos(z)

pit.plot(x,y, color="lime", label="ni... wait never mind")
pit.plot(z,w, color="red", label="not another one")
pit.xlabel("why is x so long and curvy")
pit.ylabel("y do you think this is a good idea")
pit.title("Painfully not so simple maby simple sinus and cosinus graph")
pit.legend()
pit.show()