import math

def calculateStats(numbers):
    # Filter out NaN values
    filtered = [n for n in numbers if not math.isnan(n)]

    stats = {}
    if filtered:
        stats['avg'] = sum(filtered) / len(filtered)
        stats['max'] = max(filtered)
        stats['min'] = min(filtered)
    else:
        stats['avg'] = float('nan')
        stats['max'] = float('nan')
        stats['min'] = float('nan')
    return stats
