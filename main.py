import math
import easygui
import pandas as pd
import sys
import tkinter as tk 


def generate_excel(targets, weights, combinations):
    return


class Window():
    def __init__(self):
  
        # Creating the tkinter Window
        self.root = tk.Tk()
        self.root.geometry("200x100")
        self.sheet = ''
  
        # Button for closing
        exit_button = tk.Button(self.root, text="Exit", command=self.Close)
        exit_button.pack(pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.root.mainloop()
  
    # Function for closing window
    def Close(self):
        self.sheet = self.entry.get()
        self.root.destroy()


class Application:
    def __init__(self, master):
        self.master = master
        self.sheet = ''

    def choose_file_window(self):
        self.master.withdraw()
        path = tk.filedialog.askopenfilename()
        return path

    def on_button(self, entry):
        self.sheet = entry.get()
        self.close()

    def close(self):
        self.master.destroy()


class Excel_sheet:
    def __init__(self, path, sheet):
        df = pd.read_excel(path, sheet_name=sheet, header=None, index_col=False)
        df['Result'] = df.apply(lambda row: row[row == 'V/H'].index.tolist(), axis=1)
        a2 = df[df[0] == 'Cena zł/Konstrukcja'].index.item()
        self.sheet = df.iloc[3:a2+1, 0:max(df['Result'][2])+1].reset_index(drop = True)

    def get_weights(self): 
        return self.sheet.iloc[0, 2::].tolist()

    def get_values(self):
        return self.sheet.iloc[-1, 2::].tolist()

    def get_targets(self):
        a1 = self.sheet[self.sheet[1] == 'rzedy'].index.item()
        a2 = self.sheet[self.sheet[0] == 'Suma rzędów'].index.item()
        return self.sheet.iloc[a1+1:a2, 1].tolist()


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
        return (best_combinations)

root = tk.Tk()
app = Application(root)
path = app.choose_file_window()
print(path)
app.close()
app1 = Window()


print(app1.sheet)












