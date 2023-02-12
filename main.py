import math
import easygui
import pandas as pd
import sys

class Application:
    def choose_file():
        path = easygui.fileopenbox(msg = "Optimizer", title = 'sdf')
        return path

    def choose_sheet():
        sheet_name = easygui.enterbox(msg = "Wpisz nazwe arkusza")
        return sheet_name
    
    def close():
        sys.exit()


class Excel_sheet:
    def __init__(self, path, sheet):
        self.df = pd.read_excel(path, sheet_name=sheet)

    def get_weights():
        return

    def get_values():
        return

    def get_targets():
        return

class Combination:
    def __init__(self, combination):
        self.combination = combination

    def __repr__(self):
        return str(self.combination)

    def valuation(self, values):
        final_value = 0
        for item in self.combination:
            final_value += values[item]
        return (self.combination, final_value)


class Weights:
    def __init__(self, weights):
        self.weights = weights
    
    def value_all(self, target_sum, values):
        combinations = []
        self.dfs(self.weights, target_sum, [], combinations)
        combinations_values = []
        for item in combinations:
            combinations_values.append(item.valuation(values))
        return combinations_values

    def dfs(self, nums, target_sum, path, combinations):
        if target_sum < 0:
            return
        if target_sum == 0:
            combinations.append(Combination(path))
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target_sum-nums[i], path+[nums[i]], combinations)

    def least_valuable(self, target_sum, values):
        dp = [0]
        best_combinations = [[]]
        for i in range(1, target_sum + 1):
            dp.append(math.inf)
            best_combinations.append([])
            for j in range(0, len(self.weights)):
                if(i >= self.weights[j]):
                    if dp[i] > dp[i - self.weights[j]] + values[self.weights[j]]:
                        dp[i] = dp[i - self.weights[j]] + values[self.weights[j]]
                        best_combinations[i] = best_combinations[i - self.weights[j]] + [self.weights[j]]
        return (best_combinations[-1], dp[-1])

app = Application()

path = app.choose_file()
if(path == None):
    app.close()

sheet_name = app.choose_sheet()
if(sheet_name == None):
    app.close()

excel = Excel_sheet(path, sheet_name)

weights = excel.get_weights()
values = excel.get_values()
targets = excel.get_targets()










