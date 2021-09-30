import numpy as np


def write_csv(data, filename, parts=None, **kwargs):
    """
    Write data to multiple csv files.

    Parameters
    ----------
    data : list
        List of dictionaries.
    filename : str
        Name of the CSV file.
    parts : int
        Number of parts to split the data into.

    Returns
    -------
    None.

    """
    if isinstance(parts, int):
        # Add column to identify parts
        data["__Part__"] = np.repeat(range(parts), np.ceil(len(data) / parts))[0 : len(data)]
        for j, g in data.groupby("__Part__"):
            g.drop(["__Part__"], axis=1).to_csv(filename, **kwargs)
    else:
        data.to_csv(filename, **kwargs)
