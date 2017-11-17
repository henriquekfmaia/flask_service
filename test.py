import matlab.engine
import numpy as np

eng = matlab.engine.start_matlab()
A = matlab.double([[1,2], [3,4]])
for i in range(0,100):
    print(eng.invmatrix(A))
