from scipy.sparse.csgraph import floyd_warshall

# Floyd-Warshall
# distは隣接行列
dist = floyd_warshall(dist)
dist = dist.astype(int).tolist()