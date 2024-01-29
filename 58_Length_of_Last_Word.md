Python:
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```
Java:
```java
class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        String lastWord = words[words.length - 1];
        return lastWord.length();
    }
}
```
