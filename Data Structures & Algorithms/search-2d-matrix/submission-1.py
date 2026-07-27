class Solution:
    def binarySearch(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            col = len(matrix[row]) - 1
            if target > matrix[row][col]:
                continue
            else:
                return self.binarySearch(matrix[row], target)


        return False