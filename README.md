# multiflow-rslvq
An implementation of the Robust Soft Learning Vector Quantizatin, which works with the scikit-multiflow streaming data framework.

## Known Issues
The following issues could be recognized:

   - After a while the model only predicts one class (this only happens irregular)
   - The model currently isn't compatible with the HoldoutEvaluator of scikit-multiflow (prediction dosen't seem to work)
   - When using more than one prototype per class you should limit the optimizer by the the max_iter atrribute
   - We have to remove some unnecessary logging (only simple print functions e.g. weight matrix is printed on every iteration) and unneeded files
   
## To-Dos
The main files are stream_rslvq_test.py which uses our classes RSLVQ from rslvq_stream.py which inherits from _LvqBaseModel (also modified by us and located in lvq_stream.py)

For To-Dos check the following tasks:
   
   - Merge classes _LvqBaseModel and RSLVQ to a single RSLVQ class
   - Enable compatibility to HoldoutEvaluator
   - Add RMSprop and Adadelta as optimization algorithms for the gradient descent (choosable via a parameter e.g. optimizer='RMSprop') 
   - Remove unneeded files & testing files from Git
   - Remove unnecessary logging

