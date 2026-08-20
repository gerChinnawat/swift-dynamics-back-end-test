"""
เขียนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

from shared.base_solution import BaseSolution
from .utils import ones_digit_to_roman, tens_digit_to_roman, hundreds_digit_to_roman, thousands_digit_to_roman

class Solution(BaseSolution):
    def is_input_valid(self):
        if self.input <= 0:
            self.output = 'number can not less than or equals to 0'
            return False
        elif self.input > 3999:
            self.output = 'number can not more than 3999'
            return False
        return True

    def fullfill_zero(self):
        str_number = str(self.input)
        if len(str_number) < 4:
            dif = 4 - len(str_number)
            return '0' * dif + str_number
        return str_number
        
    def number_to_roman(self):
        if not self.is_input_type_valid() or not self.is_input_valid():
            return

        fullfilled_number = self.fullfill_zero()
        ones_digit = ones_digit_to_roman(int(fullfilled_number[3]))
        tens_digit = tens_digit_to_roman(int(fullfilled_number[2]))
        hundreds_digit = hundreds_digit_to_roman(int(fullfilled_number[1]))
        thousands_digit = thousands_digit_to_roman(int(fullfilled_number[0]))
        self.output = f'{thousands_digit}{hundreds_digit}{tens_digit}{ones_digit}'


example1 = Solution(101, int)
example1.number_to_roman()
example1.print_result()
print('-----------------------')
example2 = Solution(-1, int)
example2.number_to_roman()
example2.print_result()