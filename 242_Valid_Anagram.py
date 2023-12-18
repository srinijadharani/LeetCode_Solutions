# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
  return Counter(s) == Counter(t)

# Counter is used to count the occurrences of each element in a list or a string. 
# This comparison is used to check if two collections have the same set of elements with the same counts, the order doesnt matter.
