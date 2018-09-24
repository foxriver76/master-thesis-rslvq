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

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|99.9|67.2|99.6|99.9|**100**|**100**|**100**|
|LED G|99.9|67.1|99.8|**100**|**100**|**100**|99.9|
|SEA A|**90.0**|82.9|88.7|89.9|71.6|**90.0**|83.9|
|SEA G|**89.9**|82.2|88.9|**89.9**|67.7|89.6|83.2|
|AGR A|   |50.1|54.3|51.5|50.8|**99.9**|79.8|
|AGR G|   |52.7|53.3|53.3|55.5|**86.7**|79.3|
|RTG  |   |58.8|68.5|62.3|73.1|**84.0**|60.5|
|RBF F|   |59.7|59.8|52.5|---|59.8|68.8|
|RBF M|   |53.8|57.6|59.5|---|68.1|74.4|
|HYPER|   |56.7|**87.3**|86.1|73.6|80.3|84.9|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|85.3|85.3|85.3|85.3|58.0|80.9|**88.3**|
|GMSC|86.5|71.5|93.1|85.8|14.8|**93.2**|88.1|
|POKR|73.4|74.7|**75.1**|74.8|38.9|71.2|71.3|
|---|---|---|---|---|---|---|---|
|Real Avg|81.7|77.2|**84.5**|82.0|37.2|81.8|82.6|
|Real Avg Rank|3.3|3.7|**1.7**|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|4|7|6|4|1|1|1|
|LED G|4|7|6|1|1|1|4|
|SEA A|1|6|4|3|7|1|5|
|SEA G|1|6|4|1|7|3|5|
|AGR A|   |6|3|4|5|1|2|
|AGR G|   |6|4|4|3|1|2|
|RTG  |   |6|3|4|2|1|5|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|1|2|5|4|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|2|2|2|2|7|6|1|
|GMSC|4|6|2|5|7|1|3|
|POKR|4|3|1|2|7|6|5|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|3.7|1.7|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Immediate Kappa

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|99.9|63.5|99.6|99.9|**100**|**100**|99.9|
|LED G|99.8|63.4|99.8|**100**|**100**|**100**|99.9|
|SEA A|75.5|59.0|72.6|75.1|29.9|**75.6**|60.7|
|SEA G|**78.9**|62.8|76.8|78.8|30.5|78.2|64.9|
|AGR A|   |0.3|-0.1|1.4|0.3|**99.9**|58.6|
|AGR G|   |4.1|5.9|6.0|10.6|**73.3**|57.6|
|RTG  |   |17.3|31.5|23.8|36.2|**66.0**|20.7|
|RBF F|   |15.6|15.4|4.4|---|13.0|24.1|
|RBF M|   |6.3|14.0|17.0|---|35.9|43.2|
|HYPER|   |13.5|**74.6**|72.2|47.1|60.6|69.8|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|70.0|70.0|70.0|70.0|6.3|60.8|**76.0**|
|GMSC|0.2|-0.4|0.0|-1.1|0.5|**19.3**|1.2|
|POKR|53.5|55.0|**56.2**|55.3|6.1|47.5|49.0|
|---|---|---|---|---|---|---|---|
|Real Avg|41.2|41.5|42.1|41.4|4.3|**42.5**|42.1|
|Real Avg Rank|3.3|4.0|**2.7**|3.3|5.7|4.3|**2.7**|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|3|7|6|3|1|1|3|
|LED G|5|7|5|1|1|1|4|
|SEA A|2|6|4|3|7|1|5|
|SEA G|1|6|4|2|7|3|5|
|AGR A|   |4|6|3|4|1|2
|AGR G|   |6|5|4|3|1|2|
|RTG  |   |6|3|4|2|1|5|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|1|2|5|4|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|2|2|2|2|7|6|1|
|GMSC|4|7|5|6|3|1|2|
|POKR|4|3|1|2|7|6|5|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|4.0|2.7|3.3|5.7|4.3|2.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |


### Immediate Kappa T

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|99.9|63.5|99.6|99.9|**100**|**100**|99.9|
|LED G|99.8|63.4|99.8|**100**|**100**|**100**|99.9|
|SEA A|**76.4**|59.6|73.3|76.0|33.0|76.3|61.9|
|SEA G|**79.0**|62.8|76.8|78.8|32.5|78.4|65.0|
|AGR A|   |-3.3|5.4|-0.3|-1.8|**99.9**|58.2|
|AGR G|   |-1.5|-0.1|-0.1|4.6|**71.5**|57.2|
|RTG  |   |17.6|34.1|24.2|41.1|**66.3**|20.5|
|RBF F|   |17.7|17.8|5.1|---|17.6|30.3|
|RBF M|   |5.9|14.5|18.2|---|35.9|45.4|
|HYPER|   |13.6|**74.6**|72.2|47.1|60.6|69.8|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|0.0|0.0|0.0|0.0|-186.3|-30.4|**20.0**|
|GMSC|-0.5|-121.1|46.0|-10.3|-561.2|**47.1**|7.0|
|POKR|-4.3|0.6|**2.3**|0.9|-139.9|-13.0|-12.6|
|---|---|---|---|---|---|---|---|
|Real Avg|-1.6|-40.2|**16.1**|-3.1|-289.8|1.2|4.8|
|Real Avg Rank|3.3|3.7|**1.7**|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|3|7|6|3|1|1|3|
|LED G|5|7|5|1|1|1|4|
|SEA A|1|6|4|3|7|2|5|
|SEA G|1|6|4|2|7|3|5|
|AGR A|   |6|3|4|5|1|2|
|AGR G|   |6|4|4|3|1|2|
|RTG  |   |6|3|4|2|1|5|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|1|2|5|4|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|2|2|2|2|7|6|1|
|GMSC|4|6|2|5|7|1|3|
|POKR|4|3|1|2|7|6|5|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|3.7|1.7|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |

### Immediate Kappa M

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|
|LED A|99.9|63.5|99.6|99.9|**100**|**100**|99.9|
|LED G|99.8|63.4|99.8|**100**|**100**|**100**|99.9|
|SEA A|**85.6**|75.4|83.7|85.4|59.2|85.5|76.8|
|SEA G|**83.1**|70.1|81.3|83.0|45.7|82.6|71.9|
|AGR A|   |-16.2|-6.0|-12.8|-14.1|**99.9**|52.9|
|AGR G|   |-3.5|-2.1|-2.2|2.6|**71.0**|51.8|
|RTG  |   |14.2|48.0|18.5|24.1|**58.6**|15.5|
|RBF F|   |59.7|6.1|7.6|---|30.8|7.9|
|RBF M|   |-6.0|7.2|11.5|---|32.4|59.3|
|HYPER|   |13.4|**74.6**|72.2|47.0|60.5|69.8|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|65.4|65.4|65.4|65.4|1.0|54.9|**72.3**|
|GMSC|-94.6|-309.8|0|-104.4|-1125.7|**2.0**|-72.6|
|POKR|72.5|73.8|**74.2**|73.8|36.7|52.6|70.3|
|---|---|---|---|---|---|---|---|
|Real Avg|14.4|-56.9|**46.5**|11.6|-362.7|36.5|23.3|
|Real Avg Rank|3.3|3.3|**1.7**|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|3|7|6|3|1|1|3|
|LED G|5|7|5|1|1|1|4|
|SEA A|1|6|4|3|7|2|5|
|SEA G|1|6|4|2|7|3|5|
|AGR A|   |6|3|4|5|1|2|
|AGR G|   |6|4|5|3|1|2|
|RTG  |   |6|2|4|3|1|5|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|1|2|5|4|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|2|2|2|2|7|6|1|
|GMSC|4|6|2|5|7|1|3|
|POKR|4|2|1|2|7|6|5|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|3.3|1.7|3.0|7.0|4.3|3.0|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Immediate CPU-Time

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1851.961|1645.471|1820.586|1711.530|678.343|**372.769**|770.533|
|LED G|1993.335|1577.543|1783.463|1713.072|633.197|**390.222**|846.303|
|SEA A|761.711|871.610|673.142|655.546|467.963|**208.932**|336.949|
|SEA G|724.383|898.286|659.586|672.898|439.970|**208.876**|326.061|
|AGR A|   |784.518|1751.439|791.685|553.756|**398.257**|563.763|
|AGR G|   |832.535|815.114|821.120|597.256|**381.478**|619.775|
|RTG  |   |662.155|685.154|694.892|489.937|**294.316**|493.638|
|RBF F|   |1477.024|1450.661|1359.879|---|949.117|1047.347|
|RBF M|   |1218.254|1319.601|1260.614|---|967.928|1113.365|
|HYPER|   |688.266|733.378|736.123|452.480|**287.279**|504.931|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|31.085|156.332|28.727|29.116|18.302|**11.059**|14.859|
|GMSC|82.105|72.103|82.454|75.308|48.292|**15.062**|32.658|
|POKR|1602.605|1543.254|1498.409|1530.084|**446.357**|882.931|986.171|
|---|---|---|---|---|---|---|---|
|Real Avg|571.9|590.6|536.5|544.8|**171.0**|303.0|344.6|
|Real Avg Rank|6.0|6.0|5.0|5.0|2.3|**1.3**|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|7|4|6|5|2|1|3|
|LED G|7|4|6|5|2|1|3|
|SEA A|6|7|5|4|3|1|2|
|SEA G|6|7|4|5|3|1|2|
|AGR A|   |4|6|5|2|1|3|
|AGR G|   |6|4|5|2|1|3|
|RTG  |   |4|5|6|2|1|3|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |4|5|6|2|1|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|6|7|4|5|3|1|2|
|GMSC|6|4|7|5|3|1|2|
|POKR|6|7|4|5|1|2|3|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|6.0|6.0|5.0|5.0|2.3|1.3|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Delayed Accuracy

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|**100**|66.1|99.8|**100**|**100**|**100**|**100**|
|LED G|**100**|63.7|**100**|**100**|**100**|**100**|99.6|
|SEA A|**90.2**|81.8|87.7|90.0|71.6|89.9|83.6|
|SEA G|**89.9**|81.5|88.5|89.7|67.6|89.7|82.9|
|AGR A|   |50.3|54.1|49.7|51.3|**98.8**|78.3|
|AGR G|   |53.4|51.5|53.6|55.7|**85.8**|77.9|
|RTG  |   |56.1|68.2|60.7|67.1|**94.0**|65.2|
|RBF F|   |50.9|50.3|63.7|---|50.1|53.4|
|RBF M|   |52.7|55.8|58.0|---|62.3|64.6|
|HYPER|   |50.1|49.5|50.4|49.6|**50.5**|49.8|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|51.7|51.7|57.6|51.7|51.9|58.1|**74.5**|
|GMSC|78.7|77.0|92.9|89.1|12.4|**93.1**|78.7|
|POKR|49.9|49.9|48.1|50.8|40.5|**61.2**|52.6|
|---|---|---|---|---|---|---|---|
|Real Avg|60.1|59.5|66.2|63.9|34.9|**70.8**|68.6|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|**1.3**|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1|7|6|1|1|1|1|
|LED G|1|7|1|1|1|1|6|
|SEA A|1|6|4|2|7|3|5|
|SEA G|1|6|4|2|7|2|5|
|AGR A|   |5|3|6|4|1|2|
|AGR G|   |5|6|4|3|1|2|
|RTG  |   |6|2|5|3|1|4|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |3|5|2|4|1|6|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|5|5|3|5|4|2|1|
|GMSC|4|6|2|3|7|1|4|
|POKR|4|4|6|3|7|1|2|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|1.3|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Delayed Kappa

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|**100**|62.4|99.8|**100**|**100**|**100**|**100**|
|LED G|**100**|59.6|**100**|**100**|**100**|**100**|99.6|
|SEA A|**75.9**|56.8|70.6|75.4|29.8|75.4|60.0|
|SEA G|**78.9**|61.4|75.9|78.5|30.5|78.4|64.3|
|AGR A|   |1.1|-0.2|-0.2|-0.1|**97.5**|55.6|
|AGR G|   |6.2|3.6|6.3|10.8|**71.6**|54.8|
|RTG  |   |6.1|35.2|17.7|31.2|**87.4**|29.0|
|RBF F|   |1.7|0.2|0.0|---|-0.3|18.5|
|RBF M|   |4.4|11.3|12.9|---|3.9|28.9|
|HYPER|   |**1.2**|-0.7|0.7|-0.5|0.1|-0.1|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|3.4|3.4|0.0|3.4|3.3|18.2|**45.9**|
|GMSC|0.5|0.1|0.0|-1.9|0.3|**20.3**|0.9|
|POKR|9.3|9.3|7.6|10.0|2.1|**28.2**|13.6|
|---|---|---|---|---|---|---|---|
|Real Avg|4.4|4.3|2.5|3.8|1.9|**22.2**|20.1|
|Real Avg Rank|3.3|4.0|6.3|4.3|5.7|**1.3**|1.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1|7|6|1|1|1|1|
|LED G|1|7|1|1|1|1|6|
|SEA A|1|6|4|2|7|2|5|
|SEA G|1|6|4|2|7|3|5|
|AGR A|   |3|5|5|4|1|2|
|AGR G|   |5|6|4|3|1|2|
|RTG  |   |6|2|5|3|1|4|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |1|6|2|5|3|4|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|3|3|7|3|6|2|1|
|GMSC|3|5|6|7|4|1|2|
|POKR|4|4|6|3|7|1|2|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|3.3|4.0|6.3|4.3|5.7|1.3|1.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Delayed Kappa T

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|**100**|62.4|99.8|**100**|**100**|**100**|**100**|
|LED G|**100**|59.7|**100**|**100**|**100**|**100**|99.6|
|SEA A|**76.7**|57.0|70.9|76.3|32.9|76.1|61.2|
|SEA G|**79.0**|61.3|75.9|78.5|32.4|78.5|64.4|
|AGR A|   |-2.9|5.2|-0.4|-0.8|**97.5**|55.1|
|AGR G|   |0.1|-4.1|0.5|4.9|**69.6**|54.3|
|RTG  |   |10.6|36.1|19.9|32.8|**87.4**|29.5|
|RBF F|   |1.7|0.4|21.4|---|0.0|5.1|
|RBF M|   |5.0|11.5|15.5|---|21.7|28.9|
|HYPER|   |-196.6|-200.9|-195.6|-200.6|**-192.3**|-196.7|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|-240.9|-240.9|-199.5|-240.9|-239.2|-195.7|**-79.9**|
|GMSC|-61.8|-75.0|46.1|16.9|-566.3|**47.7**|-62.1|
|POKR|-95.9|-95.9|-102.8|-92.4|-132.8|**-51.8**|-85.2|
|---|---|---|---|---|---|---|---|
|Real Avg|-132.9|-137.3|-85.4|-105.5|-312.8|**-66.6**|-75.7|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|**1.3**|2.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1|7|6|1|1|1|1|
|LED G|1|7|1|1|1|1|6|
|SEA A|1|6|4|2|7|3|5|
|SEA G|1|6|4|2|7|2|5|
|AGR A|   |6|3|4|5|1|2|
|AGR G|   |5|6|4|3|1|2|
|RTG  |   |6|2|5|3|1|4|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |3|6|2|5|1|4|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|5|5|3|5|4|2|1|
|GMSC|4|6|2|3|7|1|5|
|POKR|4|4|6|3|7|1|2|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|1.3|2.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Delayed Kappa M

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|**100**|62.4|99.8|**100**|**100**|**100**|**100**|
|LED G|**100**|59.7|**100**|**100**|**100**|**100**|99.6|
|SEA A|**85.8**|73.9|82.3|85.6|59.2|85.4|76.4|
|SEA G|**83.1**|68.9|80.6|82.7|45.7|82.7|71.4|
|AGR A|   |12.6|-6.0|11.6|-12.6|**97.2**|61.8|
|AGR G|   |14.3|10.8|14.7|18.5|**73.9**|61.2|
|RTG  |   |22.7|31.1|31.2|22.6|**90.3**|22.2|
|RBF F|   |2.6|-2.4|-0.1|---|4.1|-8.0|
|RBF M|   |-2.1|15.6|23.6|---|6.3|24.7|
|HYPER|   |-12.0|8.3|-103.0|-11.7|-0.7|**11.0**|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|-13.9|-13.9|0.0|-13.9|-13.3|1.2|**39.9**|
|GMSC|-200.1|-224.7|0.0|-54.1|-1136.2|**2.9**|-200.8|
|POKR|41.2|41.2|39.1|42.3|-4.1|**54.4**|44.4|
|---|---|---|---|---|---|---|---|
|Real Avg|-57.6|-65.8|13.0|-8.5|-384.5|**19.5**|-38.8|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|**1.3**|2.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1|7|6|1|1|1|1|
|LED G|1|7|1|1|1|1|6|
|SEA A|1|6|4|2|7|3|5|
|SEA G|1|6|4|2|7|2|5|
|AGR A|   |3|5|4|6|1|2|
|AGR G|   |5|6|4|3|1|2|
|RTG  |   |4|3|2|5|1|6|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|2|4|5|3|1|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|5|5|3|5|4|2|1|
|GMSC|4|6|2|3|7|1|5|
|POKR|4|4|6|3|7|1|2|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|4.3|5.0|3.7|3.7|6.0|1.3|2.7|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |

### Delayed CPU-Time

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|1012.091|795.131|893.665|820.796|288.025|**191.365**|373.476|
|LED G|917.185|729.234|895.148|1000.183|309.330|**187.175**|398.284|
|SEA A|269.649|346.151|250.556|255.098|209.188|**99.808**|152.553|
|SEA G|300.443|347.493|283.960|255.368|197.863|**100.626**|151.474|
|AGR A|   |364.802|859.119|405.709|292.374|**184.668**|349.424|
|AGR G|   |384.454|407.795|404.792|339.822|**237.133**|323.537|
|RTG  |   |273.405|292.777|294.298|233.565|**137.419**|220.481|
|RBF F|   |886.757|795.317|869.959|---|689.294|826.780|
|RBF M|   |833.409|785.766|894.627|---|751.568|814.607|
|HYPER|   |254.839|239.510|254.784|202.320|**123.865**|233.962|
|---|---|---|---|---|---|---|---|
|Synthetic Avg|   |   |   |   |   |   |   |
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|11.679|81.771|11.036|10.880|8.336|**4.550**|6.784|
|GMSC|30.089|26.620|30.008|27.415|19.984|**7.512**|17.629|
|POKR|746.798|652.104|694.198|688.450|**209.899**|458.636|618.694|
|---|---|---|---|---|---|---|---|
|Real Avg|262.9|253.5|245.1|242.2|**79.4**|156.9|214.4|
|Real Avg Rank|6.7|5.0|5.7|4.7|2.3|**1.3**|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg|   |   |   |   |   |   |   |
|Overall Avg Rank|   |   |   |   |   |   |   |

Rank Table:

|Data set|ARSLVQ|RSLVQ SGD|RSLVQ ADA|RSLVQ RMS|Naive Bayes|Hoeffding Tree|Hoeffding Adaptive Tree|
|---|---|---|---|---|---|---|---|
|LED A|7|4|6|5|2|1|3|
|LED G|6|4|5|7|2|1|3|
|SEA A|6|7|4|5|3|1|2|
|SEA G|6|7|5|4|3|1|2|
|AGR A|   |4|6|5|2|1|3|
|AGR G|   |4|6|5|3|1|2|
|RTG  |   |4|5|6|3|1|2|
|RBF F|   |   |   |   |   |   |   |
|RBF M|   |   |   |   |   |   |   |
|HYPER|   |6|4|5|2|1|3|
|---|---|---|---|---|---|---|---|
|Synthetic Avg Rank|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|ELEC|6|7|5|4|3|1|2|
|GMSC|7|4|6|5|3|1|2|
|POKR|7|4|6|5|1|2|3|
|---|---|---|---|---|---|---|---|
|Real Avg Rank|6.7|5.0|5.7|4.7|2.3|1.3|2.3|
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|
|Overall Avg Rank|   |   |   |   |   |   |   |