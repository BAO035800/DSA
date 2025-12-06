Given an array of integers nums and an integer target, return chỉ số của hai con số sao cho chúng cộng lại với mục tiêu.

You có thể giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp và bạn có thể không sử dụng cùng một phần tử hai lần.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 