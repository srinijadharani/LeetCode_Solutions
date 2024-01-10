Python:
```python
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(x.count(" ") for x in sentences)+1
```
Java:
```java
class Solution {
    public int mostWordsFound(String[] sentences) {
        int max_len = 0;
        for (String i : sentences) {
            int length_i = i.split(" ").length;
            if (max_len < length_i) {
                max_len = length_i;
            }
        }
        return max_len;
    }
}
```
