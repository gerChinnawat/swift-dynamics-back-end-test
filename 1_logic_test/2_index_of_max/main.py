"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""
from shared.base_solution import BaseSolution

class Solution(BaseSolution):
    def is_input_valid(self):
        if len(self.input) == 0:
            self.output = 'list can not blank'
            return False
        return True
    
    def find_max_index(self):
        if not self.is_input_type_valid() or not self.is_input_valid():
            return
        
        input_list1 = self.input.copy()
        input_list2 = self.input.copy()
        input_list1.sort()
        max_value = input_list1[-1]
        max_index = input_list2.index(max_value)
        self.output = max_index

example1 = Solution([1,2,1,3,5,6,4], list)
example1.find_max_index()
example1.print_result()
print('-----------------------')
example2 = Solution([], list)
example2.find_max_index()
example2.print_result()