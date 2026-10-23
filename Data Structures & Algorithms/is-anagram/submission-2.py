class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_tracker, t_tracker = {}, {}
        for i in range(len(s)):
            s_tracker[s[i]] = 1 + s_tracker.get(s[i],0)
            t_tracker[t[i]] = 1 + t_tracker.get(t[i],0)
        
        for c in s_tracker:
            if s_tracker[c] != t_tracker.get(c,0):
                return False
            
        return True