class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp = {c: set() for w in words for c in w}
        inedge = {c: 0 for c in mp}

        # once inside edge == 0, add it to res
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in mp[w1[j]]:
                        mp[w1[j]].add(w2[j])
                        inedge[w2[j]] += 1
                    break
            
        q = deque([n for n in inedge if inedge[n] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in mp[c]:
                inedge[nei] -= 1
                if inedge[nei] == 0:
                    q.append(nei)
        
        return "".join(res) if len(mp) == len(res) else ""








        




