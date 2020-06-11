Contains all the external files that will be required for executing the notebooks and other applications created.
# Datasets

File | Description | Source link (with details) | Label column
---|---|---|---
`Bike-Sharing-Dataset.zip` | Forecasting bike rental demand of Bike sharing program in Washington, D.C based on historical usage patterns in relation with weather, time and other data. | [UCI](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset) | `cnt`
`breast-cancer-wisconsin.data` | Classify whether the breast cancer is benign or malignant. | [UCI](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Prognostic%29) | `Outcome (R = recur, N = nonrecur)`
`machine.data` | Calculating CPU performance | [UCI](https://archive.ics.uci.edu/ml/datasets/Computer+Hardware) | `ERP`
`winequality.csv` | Quality ratings of Portuguese red wines | [UCI](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) | `quality`
`iris.data` | Predicting class of Iris plant | [UCI](http://archive.ics.uci.edu/ml/datasets/Iris) | `class`
`drugLib_raw.zip` |  Sentiment analysis of drug experience over multiple facets, i.e. sentiments learned on specific aspects such as effectiveness and side effect. | [UCI](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Druglib.com%29) | 
`Online Retail.xlsx` | Transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers. | [UCI](https://archive.ics.uci.edu/ml/datasets/Online+Retail) |

These can all be loaded using Pandas:

```python
import pandas as pd
dataset = pd.read_csv("file.csv")
```
