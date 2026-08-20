class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower().replace(" ","")
        t=t.lower().replace(" ","")

        if len(s) != len(t) and set(s) != set(t):
            return False

        s_freq = {}
        t_freq = {}

        for i in s:
            s_freq[i] = s_freq.get(i,0)+1
        for i in t:
            t_freq[i] = t_freq.get(i,0)+1
        return s_freq == t_freq
        