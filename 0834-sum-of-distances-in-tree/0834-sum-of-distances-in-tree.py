class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        child = [0] * n
        def dfs1(u, p):
            c, d = 1, 0
            for v in adj[u]:
                if v != p:
                    x = dfs1(v, u)
                    c += x[0]
                    d += x[1]
            child[u] = c
            return c, d + c
        
        s = [0] * n
        s[0] = dfs1(0, -1)[1] - child[0]

        def dfs2(u, p):
            s[u] = s[p] - child[u] + (n - child[u])
            for v in adj[u]:
                if v != p:
                    dfs2(v, u)
        
        for v in adj[0]:
            dfs2(v, 0)

        return s