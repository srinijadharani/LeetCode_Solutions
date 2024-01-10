Java:
```java
class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i].charAt(j) == x) {
                    ans.add(i);
                    break;
                }
            }
        }
        return ans;
    }
```
Python:
```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l = []
        for i in range(len(words)):
            if x in words[i]:
                l.append(i)
        return l
```
