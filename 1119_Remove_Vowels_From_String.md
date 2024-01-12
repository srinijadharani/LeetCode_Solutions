Python:
```python
class Solution:
    def removeVowels(self, s: str) -> str:
        s1 = ""
        v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in range(len(s)):
            if s[i] not in v:
                s1 = s1+s[i]
        return(s1)
```
Java:
```java
