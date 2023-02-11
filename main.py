class Combination:
    def __init__(self, combination):
        self.combination = combination

    def __repr__(self):
        return str(self.combination)

    def weigh(self, weights):
        final_weight = 0
        for item in self.combination:
            final_weight += weights[item]
        return (self.combination, final_weight)


class Dimensions:
    def __init__(self, dimensions):
        self.dimensions = dimensions
    
    def generate_combinations(self, target_sum):
        combinations = []
        self.dfs(self.dimensions, target_sum, [], combinations)
        return combinations

    def dfs(self, nums, target_sum, path, combinations):
        if target_sum < 0:
            return
        if target_sum == 0:
            combinations.append(Combination(path))
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target_sum-nums[i], path+[nums[i]], combinations)





