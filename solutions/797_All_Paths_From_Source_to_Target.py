class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        t = len(graph)-1

        def dfs(pos):
            if pos == t: return [[t]]
            if len(graph[pos]) == 0: return []

            r = []
            for n in graph[pos]:
                s = dfs(n)
                for sa in s:
                    r.append([pos] + sa)

            return r

        return dfs(0)

