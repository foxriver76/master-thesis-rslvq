# multiflow-rslvq
An implementation of the Robust Soft Learning Vector Quantizatin, which works with the scikit-multiflow streaming data framework.

## Known Issues
The following issues could be recognized:

   - At the moment --> Everything seems to work well :-)
   
## Overview of stream generators

|Dataset|Drift Rate|
|---|---|
|[AGRAWAL](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.agrawal_generator.html#module-skmultiflow.data.agrawal_generator)|?|
|[Hyper Plane](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.hyper_plane_generator.html#module-skmultiflow.data.hyper_plane_generator)|incremental|
|[LED Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.led_generator.html#module-skmultiflow.data.led_generator)|None|
|[LED Generator Drift](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.led_generator_drift.html#module-skmultiflow.data.led_generator_drift)|?|
|[Mixed Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.mixed_generator.html#module-skmultiflow.data.mixed_generator)|Abrupt|
|[Random RBF](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.random_rbf_generator.html#module-skmultiflow.data.random_rbf_generator)|None|
|[Random RBF Drift](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.random_rbf_generator_drift.html#module-skmultiflow.data.random_rbf_generator_drift)|?|
|[Random Tree Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.random_tree_generator.html#module-skmultiflow.data.random_tree_generator)|?|
|[SEA Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.sea_generator.html#module-skmultiflow.data.sea_generator)|Abrupt| 
|[Sine Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.sine_generator.html#module-skmultiflow.data.sine_generator)|Abrupt|   
|[Data Stagger Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.stagger_generator.html#module-skmultiflow.data.stagger_generator)|Abrupt|
|[Waveform Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.waveform_generator.html#module-skmultiflow.data.waveform_generator)|None|
|[Multilabel Generator](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.multilabel_generator.html#module-skmultiflow.data.multilabel_generator)|None|
|[Data Regression](https://scikit-multiflow.github.io/scikit-multiflow/skmultiflow.data.regression_generator.html#module-skmultiflow.data.regression_generator)|None|

## To-Dos
The main file is stream_rslvq_test.py which uses our class RSLVQ from rslvq_stream.py.

For To-Dos check the following tasks:
   
   - Add common streams (see page 12 of Bifet: Adaptive random forests for evolving data stream classification)
   - Do grid search for params of every algorithm per stream
   - When found good params, comparsion between the algos per stream
   - Algorithms: Hoeffding Tree, Adaptive Hoeffding Tree, Adaptive RF, SAMKNN and our three RSLVQ versions
 