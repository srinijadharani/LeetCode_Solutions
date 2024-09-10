class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        longest = 0
        sett = set()
        n = len(s)
        
        # we move l if it's invalid and r if it's valid
        for r in range(n):
            # we check if it's invalid first. if it is, remove the previous element and move l
            while s[r] in sett: # this is invalid
                sett.remove(s[l])
                l+=1
            # we define the window size - add 1 because the last char in the window is inclusive
            w = r - l + 1
            longest = max(longest, w)
            # add s[r] if the s[r] is not in sett - valid condition
            sett.add(s[r])
        return longest
