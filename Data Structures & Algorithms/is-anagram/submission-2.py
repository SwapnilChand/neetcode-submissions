class Solution:
#     Input: s = "racecar", t = "carrace"
#     Output: true

    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        # create counter map
        countS, countT = {}, {}
        
        for cs, ct in zip(s, t):
            countS[cs] = 1 + countS.get(cs, 0)
            countT[ct] = 1 + countT.get(ct, 0)

        # check for number of occurrence
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True