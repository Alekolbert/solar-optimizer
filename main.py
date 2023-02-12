import math

class Combination:
    def __init__(self, combination):
        self.combination = combination

    def __repr__(self):
        return str(self.combination)

    def weigh(self, values):
        final_value = 0
        for item in self.combination:
            final_value += values[item]
        return (self.combination, final_value)


class Weights:
    def __init__(self, weights):
        self.weights = weights
    
    def generate_combinations(self, target_sum, values):
        combinations = []
        self.dfs(self.weights, target_sum, [], combinations)
        combinations_values = []
        for item in combinations:
            combinations_values.append(item.weigh(values))
        return combinations_values

    def dfs(self, nums, target_sum, path, combinations):
        if target_sum < 0:
            return
        if target_sum == 0:
            combinations.append(Combination(path))
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target_sum-nums[i], path+[nums[i]], combinations)

    def generate_best(self, target_sum, values):
        dp = [0]
        best_combinations = [[]]
        for i in range(1, target_sum + 1):
            dp.append(math.inf)
            best_combinations.append([])
            for j in range(0, len(self.weights)):
                if(i >= self.weights[j]):
                    if dp[i] > dp[i - self.weights[j]] + values[j]:
                        dp[i] = dp[i - self.weights[j]] + values[j]
                        best_combinations[i] = best_combinations[i - self.weights[j]] + [self.weights[j]]
        return (best_combinations[-1], dp[-1])


values = {2:4, 3:7, 4:6}

obj = Weights([2,3,4])
print(min(obj.generate_combinations(10, values), key=lambda x: x[1])[1])

obj1 = Weights([2,3,4])

print(obj1.generate_best(values))







