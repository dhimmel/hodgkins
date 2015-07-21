import numpy
import numpy.linalg

def walk(r, seeds, adjacency_matrix, stop_theshold = 10e-10):
    """
    Random walk with restart. See link for more information:
    https://dx.doi.org/10.1016/j.ajhg.2008.02.013

    Parameters
    ----------
    r : float
        Restart probability.
    seeds : 1D numpy.ndarray
        Initial walker weights.
    adjacency_matrix : numpy.matrix
        An adjecency matrix encoding the graph.
    stop_theshold : float
        If no probabilities change by more than this amount
        between two iterations, walking is considered complete.
    
    Returns
    -------
    pt : numpy.ndarray
        A 1D array with probabilities for the random walker being on each node.
    steps : int
        The number of iterations before the stop_theshold was reached.
    """
    # column-normalize the adjacency matrix
    W = adjacency_matrix / adjacency_matrix.sum(axis=0)
    p0 = seeds / sum(seeds) # initial probability vector
    p0 = p0[:, None]
    pt = p0 # probability vector at time step t
    pt1 = None # probability vector at time step t + 1
    steps = 0
    while True:
        pt1 = (1 - r) * W.dot(pt) + r * p0
        l1_norm_t1 = numpy.linalg.norm(numpy.array(pt1)[:, 0], 1)
        change = max(abs(pt1 - pt))
        pt = pt1
        steps += 1
        if change < stop_theshold:
            pt = numpy.array(pt)[:, 0]
            return pt, steps