All the imports I might need to use:

```
# tools from the python standard lib
from collections import defaultdict, namedtuple, Counter
from functools import reduce
import hashlib
import re
from time import sleep
import operator
from functools import lru_cache

# my helper lib
import utils

# external libs
import requests
import numpy as np
import pandas as pd
from tqdm import tnrange, tqdm_notebook

# visualization stuff
from plotly.offline import iplot
import plotly.graph_objs as go
import ipywidgets as ipw

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from IPython.display import clear_output, display, Markdown
```