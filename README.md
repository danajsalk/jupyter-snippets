# jupyter-snippets
<br>

## Summary
<br>
Convenient pieces of jupyter code saved for later

Examples
```
# Columns and row display
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 500)
```

Automatically Format Graphs with Seaborn such as automatically adding grids
```
import seaborn as sns
sns.set(style="darkgrid")
```
Format Dates in Pandas Columns
```
import pandas as pd
df = pd.DataFrame({'DOB': {0: '26/1/2016', 1: '26/1/2016'}}) 
df['DOB'] = pd.to_datetime(df.DOB)
df['DOB1'] = df['DOB'].dt.strftime('%m/%d/%Y')
```


## Descriptions
<br>

* **Show Code Hide Code** - Creates an HTML formateed button to hide code kernals but leave open results, plots, or print statements. Very useful for building automated reports.
* **List Comprehension** - A list comprehension in Python works by loading the entire output list into memory. For small or even medium-sized lists, this is generally fine.

## Additional Jupyter Extenstions
<br>
new tab for `NBExtensions` 

run the line: `conda install -c conda-forge jupyter_contrib_nbextensions`

Just select the `ExecutionTime` extension from the `NBextensions` list and you will have an execution result at the bottom of the cell after every cell execution as well as the time when the cell was executed.
