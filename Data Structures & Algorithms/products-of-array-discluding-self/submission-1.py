class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeros = []
        for i, num in enumerate(nums):
            if num != 0:
                product *= num
            else:
                zeros.append(i)
        for i, num in enumerate(nums):
            if len(zeros) > 1:
                res.append(0)
            else:
                if i in zeros:
                    res.append(product)
                else:
                    res.append(0) if len(zeros) == 1 else res.append(int(product/num))
        return res