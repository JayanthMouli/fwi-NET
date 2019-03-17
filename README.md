# fwi-NET
fwiNET is an artificial intelligence approach to predicting wildfire intensity. The neural network, a
multilayer perceptron, analyzes environmental factors that affect wildfire spreading. The factors, developed 
by the Meteorological Service of Canada, are collectively known as the Fire Weather Index (FWI). FWI consists 
of various codes that reflect climate conditions at the fire source. The codes used in fwiNET are the Drought 
Code (DC), Duff Moisture Code (DMC), Fine Fuel Moisture Code (FFMC), Initial Spread Index (ISI), Buildup Index, 
(BUI), and the collective Fire Weather Index (FWI). fwiNET was trained using a dataset of FWI values for corresponding 
fires in the United States state of California in the year 2015, and these values were obtained by analyzing MERRA-2 data 
from NASA's Global Fire WEather Database (GFWED). fwiNET was written in the Python programming language, and uses the
Keras wrapper for the numerical library TensorFlow.
