from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower().replace(" ", "")
        t = t.lower().replace(" ", "")

        if (len(s) != len(t) and set(s) != set(t)):
            return False
        
        return Counter(s) == Counter(t)