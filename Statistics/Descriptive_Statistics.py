import numpy as np
from collections import Counter

def descriptive_statistics(data):
    data = np.array(data)
    data = data[~np.isnan(data)]  # Remove NaN values if any

    mean = np.mean(data)
    median = np.median(data)
    
    # Manual mode calculation using Counter
    counts = Counter(data)
    max_freq = max(counts.values())
    mode = min([val for val, freq in counts.items() if freq == max_freq])

    variance = np.var(data, ddof=0)
    std_dev = np.std(data, ddof=0)
    percentiles = np.percentile(data, [25, 50, 75])
    iqr = percentiles[2] - percentiles[0]

    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance, 4),
        "standard_deviation": np.round(std_dev, 4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }

    return stats_dict
