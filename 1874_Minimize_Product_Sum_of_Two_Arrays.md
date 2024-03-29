Python code:

```python
def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
    return sum(x*y for x, y in zip(sorted(nums1), sorted(nums2, reverse = True)))
```
Since this is a little too simple, here's the Java version:
```java
public int minProductSum(int[] nums1, int[] nums2) {
    // Sort both arrays in ascending order
    Arrays.sort(nums1);
    Arrays.sort(nums2);

    // Initialize variables for accumulating the product sum and iterating through nums2 in reverse
    int sum = 0;
    int j = nums2.length - 1;

    // Iterate through each element of nums1
    for (int i = 0; i < nums1.length; i++) {
        // Add the product of the current elements from nums1 and nums2 to the sum
        sum += nums1[i] * nums2[j];

        // Move to the next smaller element in nums2
        j--;
    }

    // Return the calculated sum as the minimum product sum
    return sum;
}
```
