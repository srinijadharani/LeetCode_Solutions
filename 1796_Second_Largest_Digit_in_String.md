Python:
```python
class Solution:
    def secondHighest(self, s: str) -> int:
        s_set = set()
        for i in s:
            if i.isdigit():
                s_set.add(int(i))
        s_set = sorted(s_set)
        if len(s_set) > 1:
            return s_set[-2]
        else:
            return(-1)
```
