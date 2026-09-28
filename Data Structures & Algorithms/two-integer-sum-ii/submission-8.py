class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = defaultdict(int)

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in numDict:
                return [1+numDict[diff], 1+i]
            
            numDict[numbers[i]] = i


