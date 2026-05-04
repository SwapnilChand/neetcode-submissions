class Solution:
#     Input: s = "racecar", t = "carrace"
#     Output: true

    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        # create counter map
        # countS, countT = {}, {}
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        # check for number of occurrence
        for c in count:
            if count[c] != 0:
                return False
        
        return True