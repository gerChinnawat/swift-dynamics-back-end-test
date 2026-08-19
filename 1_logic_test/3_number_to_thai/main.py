"""
เขียนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

from shared.base_solution import BaseSolution
from .utils import digit_number_to_th, digit_value_to_th

class Solution(BaseSolution):
    def is_input_valid(self):
        if self.input < 0:
            self.output = 'number can not less than 0'
            return False
        elif self.input > 10000000:
            self.output = 'number can not more than 10,000,000'
            return False
        return True
    
    def number_to_thai(self):
        if not self.is_input_type_valid() or not self.is_input_valid():
            return
        
        str_number = str(self.input)
        reversed_number = str_number[::-1]
        result = ''
        for digit_no, number in enumerate(reversed_number, start=1):
            digit_number = digit_number_to_th(int(number), digit_no, len(str_number))
            digit_value = '' if int(number) == 0 else digit_value_to_th(digit_no)
            result = f"{digit_number}{digit_value}" + result

        self.output = result

example1 = Solution(101, int)
example1.number_to_thai()
example1.print_result()
print('-----------------------')
example2 = Solution(-1, int)
example2.number_to_thai()
example2.print_result()