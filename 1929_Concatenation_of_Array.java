class Solution {
    public int[] getConcatenation(int[] nums) {
        len = nums.length;
        int [] ans = new int[len * 2];
        for (int i = 0; i < len; i++) {
            ans[i] = nums[i];
            ans[i + nums.length] = nums[i];
        }
        return ans;
    }
}

// Solution in Python is very simple. Either concatenate using the + operator or extend the arrays. Since it was very simple, I programmed this using Java. I had help from the comments, but this uses a lot of memory though!
