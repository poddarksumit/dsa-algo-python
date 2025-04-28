from typing import List

class PairSumSorted:

    def find_pair_sum(numbers: List[int], target:int) -> List[int]:
        if len(numbers) == 0:
            return []
        
        lowIndex, highIndex = 0,len(numbers) - 1

        while lowIndex < highIndex:
            sum = numbers[lowIndex] + numbers[highIndex]

            if sum == target:
                return [numbers[lowIndex],numbers[highIndex]]
            elif sum < target:
                lowIndex += 1
            else:
                highIndex -= 1
        
        return []
            


