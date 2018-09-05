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

For To-Dos check the following tasks:
   
   - Add common streams (see page 12 of Bifet: Adaptive random forests for evolving data stream classification)
   - Do grid search for params of every algorithm per stream
   - When found good params, comparsion between the algos per stream
   - Algorithms: Hoeffding Tree, Adaptive Hoeffding Tree, Naive Bayes and our three RSLVQ versions
   
   
## Evaluation Tables

### Immediate Accuracy

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|50.1|54.3|51.5|50.8|**99.9**|79.8|
|AGR G|52.7|53.3|53.3|55.5|**86.7**|79.3|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|85.3|85.3|85.3|58.0|80.9|**88.3**|
|GMSC|71.5|93.1|85.8|14.8|**93.2**|88.1|
|POKR|74.7|**75.1**|74.8|38.9|71.2|71.3|
|---|---|---|---|---|---|---|
|Real Avg|77.2|**84.5**|82.0|37.2|81.8|82.6|
|Real Avg Rank|3.3|**1.7**|2.7|6|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|6|3|4|5|1|2|
|AGR G|6|4|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|2|2|2|6|5|1|
|GMSC|5|2|4|6|1|3|
|POKR|3|1|2|6|5|4|
|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|1.7|2.7|6|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|0.3|-0.1|1.4|0.3|**99.9**|58.6|
|AGR G|4.1|5.9|6.0|10.6|**73.3**|57.6|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|70.0|70.0|70.0|6.3|60.8|**76.0**|
|GMSC|-0.4|0.0|-1.1|0.5|**19.3**|1.2|
|POKR|55.0|**56.2**|55.3|6.1|47.5|49.0|
|---|---|---|---|---|---|---|
|Real Avg|41.5|42.1|41.4|4.3|**42.5**|42.1|
|Real Avg Rank|3.3|**2.3**|3.3|5.0|3.7|**2.3**|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|4|6|3|4|1|2
|AGR G|6|5|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|2|2|2|6|5|1|
|GMSC|5|4|6|3|1|2|
|POKR|3|1|2|6|5|4|
|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|2.3|3.3|5.0|3.7|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |


### Immediate Kappa T

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|-3.3|5.4|-0.3|-1.8|**99.9**|58.2|
|AGR G|-1.5|-0.1|-0.1|4.6|**71.5**|57.2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|0.0|0.0|0.0|-186.3|-30.4|**20.0**|
|GMSC|-121.1|46.0|-10.3|-561.2|**47.1**|7.0|
|POKR|0.6|**2.3**|0.9|-139.9|-13.0|-12.6|
|---|---|---|---|---|---|---|
|Real Avg|-40.2|**16.1**|-3.1|-289.8|1.2|4.8|
|Real Avg Rank|3.3|**1.7**|2.7|6.0|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|6|3|4|5|1|2|
|AGR G|6|4|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|2|2|2|6|5|1|
|GMSC|5|2|4|6|1|3|
|POKR|3|1|2|6|5|4|
|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|1.7|2.7|6.0|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa M

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|-16.2|-6.0|-12.8|-14.1|**99.9**|52.9|
|AGR G|-3.5|-2.1|-2.2|2.6|**71.0**|51.8|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|65.4|65.4|65.4|1.0|54.9|**72.3**|
|GMSC|-309.8|0|-104.4|-1125.7|**2.0**|-72.6|
|POKR|73.8|**74.2**|73.8|36.7|52.6|70.3|
|---|---|---|---|---|---|---|
|Real Avg|-56.9|**46.5**|11.6|-362.7|36.5|23.3|
|Real Avg Rank|3.0|**1.7**|2.7|6.0|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|6|3|4|5|1|2|
|AGR G|6|4|5|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|2|2|2|6|5|1|
|GMSC|5|2|4|6|1|3|
|POKR|2|1|2|6|5|4|
|---|---|---|---|---|---|---|
|Real Avg Rank|3.0|1.7|2.7|6.0|3.7|2.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate CPU-Time

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|784.518|1751.439|791.685|553.756|**398.257**|563.763|
|AGR G|832.535|815.114|821.120|597.256|**381.478**|619.775|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|156.332|28.727|29.116|18.302|**11.059**|14.859|
|GMSC|72.103|82.454|75.308|48.292|**15.062**|32.658|
|POKR|1543.254|1498.409|1530.084|**446.357**|882.931|986.171|
|---|---|---|---|---|---|---|
|Real Avg|590.6|536.5|544.8|**170.983**|303.0|344.6|
|Real Avg Rank|5.3|4.7|5.0|2.3|**1.3**|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|4|6|5|2|1|3|
|AGR G|6|4|5|2|1|3|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|6|4|5|3|1|2|
|GMSC|4|6|5|3|1|2|
|POKR|6|4|5|1|2|3|
|---|---|---|---|---|---|---|
|Real Avg Rank|5.3|4.7|5.0|2.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Accuracy

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|50.3|54.1|49.7|51.3|**98.8**|78.3|
|AGR G|53.4|51.5|53.6|55.7|**85.8**|77.9|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|51.7|57.6|51.7|51.9|58.1|**74.5**|
|GMSC|77.0|92.9|89.1|12.4|**93.1**|78.7|
|POKR|49.9|48.1|50.8|40.5|**61.2**|52.6|
|---|---|---|---|---|---|---|
|Real Avg|59.5|66.2|63.9|34.9|**70.8**|68.6|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|5|3|6|4|1|2|
|AGR G|5|6|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|5|3|5|4|2|1|
|GMSC|5|2|3|6|1|4|
|POKR|4|5|3|6|1|2|
|---|---|---|---|---|---|---|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|1.1|-0.2|-0.2|-0.1|**97.5**|55.6|
|AGR G|6.2|3.6|6.3|10.8|**71.6**|54.8|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|3.4|0.0|3.4|3.3|18.2|**45.9**|
|GMSC|0.1|0.0|-1.9|0.3|**20.3**|0.9|
|POKR|9.3|7.6|10.0|2.1|**28.2**|13.6|
|---|---|---|---|---|---|---|
|Real Avg|4.3|2.5|3.8|1.9|**22.2**|20.1|
|Real Avg Rank|3.3|5.3|4.0|4.7|1.3|1.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|3|5|5|4|1|2|
|AGR G|5|6|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|3|6|3|5|2|1|
|GMSC|4|5|6|3|1|2|
|POKR|4|5|3|6|1|2|
|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|5.3|4.0|4.7|1.3|1.7|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa T

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|-2.9|5.2|-0.4|-0.8|**97.5**|55.1|
|AGR G|0.1|-4.1|0.5|4.9|**69.6**|54.3|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|-240.9|-199.5|-240.9|-239.2|-195.7|**-79.9**|
|GMSC|-75.0|46.1|16.9|-566.3|**47.7**|-62.1|
|POKR|-95.9|-102.8|-92.4|-132.8|**-51.8**|-85.2|
|---|---|---|---|---|---|---|
|Real Avg|-137.3|-85.4|-105.5|-312.8|**-66.6**|-75.7|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|6|3|4|5|1|2|
|AGR G|5|6|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|5|3|5|4|2|1|
|GMSC|5|2|3|6|1|4|
|POKR|4|5|3|6|1|2|
|---|---|---|---|---|---|---|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed Kappa M

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|12.6|-6.0|11.6|-12.6|**97.2**|61.8|
|AGR G|14.3|10.8|14.7|18.5|**73.9**|61.2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|-13.9|0.0|-13.9|-13.3|1.2|**39.9**|
|GMSC|-224.7|0.0|-54.1|-1136.2|**2.9**|-200.8|
|POKR|41.2|39.1|42.3|-4.1|**54.4**|44.4|
|---|---|---|---|---|---|---|
|Real Avg|-65.8|13.0|-8.5|-384.5|**19.5**|-38.8|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|3|5|4|6|1|2|
|AGR G|5|6|4|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|5|3|5|4|2|1|
|GMSC|5|2|3|6|1|4|
|POKR|4|5|3|6|1|2|
|---|---|---|---|---|---|---|
|Real Avg Rank|4.7|3.3|3.7|5.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Delayed CPU-Time

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|364.802|859.119|405.709|292.374|**184.668**|349.424|
|AGR G|384.454|407.795|404.792|339.822|**237.133**|323.537|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|81.771|11.036|10.880|8.336|**4.550**|6.784|
|GMSC|26.620|30.008|27.415|19.984|**7.512**|17.629|
|POKR|652.104|694.198|688.450|**209.899**|458.636|618.694|
|---|---|---|---|---|---|---|
|Real Avg|253.5|245.1|242.2|**79.4**|156.9|214.4|
|Real Avg Rank|5.3|5.7|4.7|2.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |

Rank Table:

|Data set|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|   |   |   |   |   |   |
|LED G|   |   |   |   |   |   |
|SEA A|   |   |   |   |   |   |
|SEA G|   |   |   |   |   |   |
|AGR A|4|6|5|2|1|3|
|AGR G|4|6|5|3|1|2|
|RTG|   |   |   |   |   |   |
|RBF F|   |   |   |   |   |   |
|HYPER|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|ELEC|6|5|4|3|1|2|
|GMSC|4|6|5|3|1|2|
|POKR|4|6|5|1|2|3|
|---|---|---|---|---|---|---|
|Real Avg Rank|5.3|5.7|4.7|2.3|1.3|2.3|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |