# Calculate number and percentage of NaNs
import pandas as pd
def nans_sum_perc(x):
    nans_sum_perc_d = {}
    for i in x.columns:
        sum_nan = x[i].isna().sum() 
        if  sum_nan > 0:
            perc_nan = round((sum_nan / x[i].shape[0]) * 100, 2)
            nans_sum_perc_d.update({i: [sum_nan, perc_nan]})
    return pd.DataFrame.from_dict(nans_sum_perc_d, orient='index', columns=['NaN Count', 'NaN %'])