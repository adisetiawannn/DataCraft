# this code used for map the length of stay on pandas dataframe
# Define bins and labels
import pandas as pd

def map_length_of_stay(month_diff_series):
    """
    Map a pandas Series of month differences to length of stay categories.
    """
    bins = [0, 6, 12, 24, 36, 48, 60, float('inf')]
    labels = [
        '< 6 Bulan',
        '6 - 12 Bulan',
        '1-2 Tahun',
        '2-3 Tahun',
        '3-4 Tahun',
        '4-5 Tahun',
        '> 5 tahun'
    ]
    return pd.cut(month_diff_series, bins=bins, labels=labels, right=True, include_lowest=True)