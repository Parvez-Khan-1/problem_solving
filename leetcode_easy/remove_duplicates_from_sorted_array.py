#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/


class Solution:

    def removeDuplicates(self, nums):
        prev = nums[0]
        for idx, next_element in enumerate(nums[1:]):
            if idx == len(nums):
                break
            if prev == next_element:
                nums.remove(prev)
                self.removeDuplicates(nums)
            else:
                prev = next_element
        return len(nums), nums


s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
length, nums = s.removeDuplicates(nums)
print(length)
print(nums)


# def delete_dup(self, arry, element):
#     if arry.count(element)>1:
# #         arry.remove(element)
# #         self.delete_dup(arry, element)
# #     return arry
#
#
# def removeDuplicates(self, nums):
# # for idx, item in enumerate(nums):
# #     if nums.count(item) != 1:
# #         nums = self.delete_dup(nums, item)
# # return len(nums)
