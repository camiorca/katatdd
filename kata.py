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
        res = []
        if numbers =="":
            return []
        elif len(numbers) == 1:
            res += [int(numbers)]
        elif len(numbers) == 3:
            all_nums = numbers.split(',')
            num = list(map(int, all_nums))
            res += [max(num)]
        elif len(numbers) == 4:
            return []
        return res