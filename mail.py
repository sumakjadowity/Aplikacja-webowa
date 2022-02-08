import matlab.engine

# eng = matlab.engine.start_matlab()
from matlab.engine import MatlabEngine

eng = matlab.engine.connect_matlab('Engine_1')
# t = eng.sqrt(4.0)
# print(t)

eng.load(r"C:\Users\marty\Documents\studia\TSwM\projekt\8.jpg")
plik = eng.evalc(r"run C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\kod_matlab.m")
x = eng.load(r"C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\mat2.mat")
print(x["text"])


