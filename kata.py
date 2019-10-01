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
            return res
        elif len(numbers) == 3:
            all_nums = numbers.split(',')
            num = list(map(int, all_nums))
            res += [max(num)]
            return res
        elif len(numbers) > 3:
            all_nums = numbers.split(',')
            num = list(map(int, all_nums))
            res = [len(all_nums), max(num)]
            return res
        return res


class minlen:
    def solver_function_minlen(self, numbers):
        if numbers == "":
            return []
        else:
            if len(numbers) == 1:
                nums = int(numbers)
                return [len(numbers), nums]
            elif len(numbers) == 3:
                list_nums = numbers.split(',')
                nums = list(map(int, list_nums))
                max_num = max(nums)
                return [len(list_nums), max_num]
