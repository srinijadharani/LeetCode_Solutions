class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        # if no strings to compare
        if not strs:
            return longest_prefix
        # calculate the shortest string using the min function
        shortest_string = min(strs, key = len)
    
        for i in range(len(shortest_string)):
            # check all the strings (x) in strs start with the substring of the shortest string up to the current index
            if all([x.startswith(shortest_string[:i+1]) for x in strs]):
                # If the current substring is a common prefix for all strings, update the longest_prefix to be this substring
                longest_prefix = shortest_string[:i+1]
            else:
                break
        return longest_prefix
