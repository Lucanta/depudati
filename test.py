import pandas as pd
import numpy as np

poll_id = 9999

polls = pd.read_csv('voting_intention_polls.csv',header=None,delimiter=',',usecols=list(range(23)),error_bad_lines=False)

print(polls)

data = pd.Series(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(data)

polls = polls.append(data,ignore_index=True)

print(polls)