"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

from shared.base_solution import BaseSolution

class Solution(BaseSolution):
    def is_input_valid(self):
        if self.input < 0:
            self.output = 'number can not be negative'
            return False
        return True
        
    def find_factorial_result(self) -> int:
        result = 1
        for x in range(1, self.input):
            result *= (self.input - x) 
        return result

    def count_zero_tail(self) -> int:
        factorial_result = self.find_factorial_result()
        print(f"factorial_result = ", factorial_result)

        # count 0 when input less than or equal to 5
        if self.input <= 5:
            return 0

        # start count zero amount when more than 5
        str_factorial_result = str(factorial_result)
        count = 0
        for x in range(-1, self.input*(-1) - 1, -1):
            if str_factorial_result[x] != '0':
                return count
            count += 1

    def find_tailing_zeroes(self):
        if not self.is_input_type_valid() or not self.is_input_valid():
            return
        self.output = self.count_zero_tail()


solution1 = Solution(7, int)
solution1.find_tailing_zeroes()
solution1.print_result()
print('-----------------------')
solution2 = Solution(-10, int)
solution2.find_tailing_zeroes()
solution2.print_result()