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
   
   
## Evaluation Tables

### Immediate Accuracy

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|85.3|85.3|85.3|   |80.9|   |
|GMSC|71.5|93.1|85.8|   |93.2|   |
|POKR|74.7|75.1|74.8|   |71.2|   |
|---|---|---|---|---|---|---|
|Real Avg|77.2|84.5|82.0|   |81.8|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|70.0|70.0|70.0|   |60.8|   |
|GMSC|-0.4|0.0|-1.1|   |19.3|   |
|POKR|55.0|56.2|55.3|   |47.5|   |
|---|---|---|---|---|---|---|
|Real Avg|41.5|42.1|41.4|   |42.5|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa T

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|0.0|0.0|0.0|   |-30.4|   |
|GMSC|-121.1|46.0|-10.3|   |47.1|   |
|POKR|0.6|2.3|0.9|   |-13.0|   |
|---|---|---|---|---|---|---|
|Real Avg|-40.2|16.1|-3.1|   |1.2|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa M

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|65.4|65.4|65.4|   |54.9|   |
|GMSC|-309.8|0|-104.4   |2.0|   |   |
|POKR|73.8|74.2|73.8|   |52.6|   |
|---|---|---|---|---|---|---|
|Real Avg|-56.9|46.5|11.6|   |36.5|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate CPU-Time

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|156.332|28.727|29.116|   |11.059|   |
|GMSC|72.103|82.454|75.308|   |15.062|   |
|POKR|1543.254|1498.409|1530.084|   |882.931|   |
|---|---|---|---|---|---|---|
|Real Avg|590.6|536.5|544.8|   |303.0|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Accuracy

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|51.7|57.6|51.7|   |58.1|   |
|GMSC|77.0|92.9|89.1|   |93.1|   |
|POKR|49.9|48.1|50.8|   |61.2|   |
|---|---|---|---|---|---|---|
|Real Avg|59.5|66.2|63.9|   |70.8|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|3.4|0.0|3.4|   |18.2|   |
|GMSC|0.1|0.0|-1.9|   |20.3|   |
|POKR|9.3|7.6|10.0|   |28.2|   |
|---|---|---|---|---|---|---|
|Real Avg|4.3|2.5|3.8|   |22.2|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa T

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|-240.9|-199.5|-240.9|   |-195.7|   |
|GMSC|-75.0|46.1|16.9|   |47.7|   |
|POKR|-95.9|-102.8|-92.4|   |-51.8|   |
|---|---|---|---|---|---|---|
|Real Avg|-137.3|-85.4|-105.5|   |-66.6|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa M

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|-13.9|0.0|-13.9|   |1.2|   |
|GMSC|-224.7|0.0|-54.1|   |2.9|   |
|POKR|41.2|39.1|42.3| |   |54.4|
|---|---|---|---|---|---|---|
|Real Avg|-65.8|13.0|-8.5|   |19.5|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed CPU-Time

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|AGR A|   |   |   |   |   |   |
|AGR G|   |   |   |   |   |   |
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|81.771|11.036|10.880|   |4.550|   |
|GMSC|26.620|30.008|27.415|   |7.512|   |
|POKR|652.104|694.198|688.450|   |458.636|   |
|---|---|---|---|---|---|---|
|Real Avg|253.5|245.1|242.2|   |156.9|   |
|Real Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |