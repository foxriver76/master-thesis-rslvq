# multiflow-rslvq
An  of the Robust Soft Learning Vector Quantizatin, which works with the scikit-multiflow streaming data framework.
# multiflow-rslvq



## Known Issues
The following issues could be recognized:

   - After a while the model only predicts one class (this only happens irregular)
   - The model currently isn't compatible with the HoldoutEvaluator of scikit-multiflow (prediction dosen't seem to work)
   - When using more than one prototype per class you should limit the optimizer by the the max_iter atrribute
   - We have to remove some unnecessary logging (only simple print functions e.g. weight matrix is printed on every iteration) and unneeded files
