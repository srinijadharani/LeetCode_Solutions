Python:
```python3
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n
        else:
            return n*2
```
Java:
```java
class Solution {
    public int smallestEvenMultiple(int n) {
        if(n%2==0) {
            return(n);
        }
        else{
            return(n*2);
        }
    }
}
```
