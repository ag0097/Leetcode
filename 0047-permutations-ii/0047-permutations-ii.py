class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def helper(array,soln):
            if array == []:
                result.add(tuple(soln))
                return 
            for idx in range(len(array)):
                helper(array[:idx]+array[idx+1:], soln+[array[idx]])
        helper(nums,[])
        return list(result)