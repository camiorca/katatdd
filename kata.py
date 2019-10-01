class Kata:
    def solver_function(self, numbers):
        if numbers == "":
            return []
        else:
            res = []
            if len(numbers) == 1:
               res = [int(numbers)]
            elif len(numbers) >= 3:
                all_nums = numbers.split(',')
                for num in all_nums:
                    res += [int(num)]

            return res

class maxmin:
    def solver_function_max(self,numbers):
        if numbers =="":
            return []
        else:
            res = []
            res += [int(numbers)]
        return res