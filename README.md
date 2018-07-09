# multiflow-rslvq
An implementation of the Robust Soft Learning Vector Quantizatin, which works with the scikit-multiflow streaming data framework.

## Known Issues
The following issues could be recognized:

   - After a while the model only predicts one class (this only happens irregular) --> I had many runs now and couldn't experience it again (seems to be a hyperparameter problem) (foxriver76)
   - When using more than one prototype per class you should limit the optimizer by the the max_iter atrribute --> it also takes so long in the original implementation https://github.com/MrNuggelz/sklearn-lvq/tree/stable/sklearn_lvq
   - We have to remove some unnecessary logging (only simple print functions e.g. weight matrix is printed on every iteration) and unneeded files

## To-Dos
The main file is stream_rslvq_test.py which uses our class RSLVQ from rslvq_stream.py.

For To-Dos check the following tasks:
   
   - Enable compatibility to HoldoutEvaluator
   - Add RMSprop and Adadelta as optimization algorithms for the gradient descent (choosable via a parameter e.g. optimizer='RMSprop') 
   - Remove unneeded files & testing files from Git
   - Add correct Prototype initilization when data for the label isn't included in initial fitting
   - Remove unnecessary logging
   - Check predicting on Sine Generator (see figure/naive_bayes_on_sine_generator_40k.png vs figure/rslvq_on_sine_generator_40k.png)
      --> it seems to be a hyperparameter optimization problem, not an implmentation one/also Sine has concept drift

