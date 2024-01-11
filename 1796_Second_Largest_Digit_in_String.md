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
Java:
```java
import java.util.*;

class Solution {
    public int secondHighest(String s) {
        char[] chars = s.toCharArray();
        Set<Character> set = new HashSet<>(); 
        for (int i = 0; i < chars.length; i++) {
            if (Character.isDigit(chars[i])) {
                set.add(chars[i]);
            }
        }

        List<Character> sortedList = new ArrayList<>(set);
        Collections.sort(sortedList, Collections.reverseOrder());
        if(sortedList.size() > 1) {
            return Character.getNumericValue(sortedList.get(1));
        }
        else {
            return(-1);
        }
    }
}
```
