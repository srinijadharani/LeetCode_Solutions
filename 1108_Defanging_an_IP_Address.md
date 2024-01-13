Python:
```python
res = ""
for i in address:
    if i == ".":
        res = address.replace(i, "[.]")
print(res)
```
Python (single line code):
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return (address.replace(".", "[.]"))
```
Java:
```
class Solution {
    public String defangIPaddr(String address) {
        return(address.replace(".", "[.]"));
    }
}
```
