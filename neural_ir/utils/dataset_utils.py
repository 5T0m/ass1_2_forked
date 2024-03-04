from pathlib import Path
from tqdm import tqdm

# TODO: implement this method
def read_pairs(path: str):
    """
    Read tab-delimited pairs from file.
    Parameters
    ----------
    path: str 
        path to the input file
    Returns
    -------
        a list of pair tuple
    """
    # BEGIN SOLUTION
    pair_tpl_lst = []
    with open(path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            #print(line)
            fields = line.strip().split('\t')

            #print(fields)
            tupl = (fields[0], fields[1])
            pair_tpl_lst.append(tupl)

    return pair_tpl_lst




    # END SOLUTION


# TODO: implement this method
def read_triplets(path: str):
    """
    Read tab-delimited triplets from file.
    Parameters
    ----------
    path: str 
        path to the input file
    Returns
    -------
        a list of triplet tuple
    """
    # BEGIN SOLUTION
    pair_tpl_lst = []
    with open(path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            #print(line)
            fields = line.strip().split('\t')

            #print(fields)
            tupl = (fields[0], fields[1], fields[2])
            pair_tpl_lst.append(tupl)

    return pair_tpl_lst
    # END SOLUTION