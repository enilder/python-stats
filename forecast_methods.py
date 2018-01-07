import pandas as pd
import numpy as np

def cagr(frame):

	#  Calculates Compound Annual Growth
	#  Takes a DataFrame with a datetime value as the index
	#  Returns pandas Series
	
	annual_sums = frame.groupby([frame.index.year]).sum()
	firstp = pd.Series(annual_sums.iloc[0], index=annual_sums.columns)
	lastp = np.array(annual_sums.iloc[-1], index=annual_sums.columns)
	periods = float(len(annual_sums))
	change = (lastp/firstp).replace(np.inf, np.nan) 
	cagr = change ** (1/periods) - 1.0
	return cagr
	