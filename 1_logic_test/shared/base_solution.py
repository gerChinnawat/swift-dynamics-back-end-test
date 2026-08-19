class BaseSolution:
    def __init__(self, user_input: any, expected_type: type):
        self.input = user_input
        self.expected_type = expected_type
        
    def is_input_type_valid(self):
        if not isinstance(self.input, self.expected_type):
            self.output = f'input must be {self.expected_type.__name__}'
            return False
        return True

    def print_result(self):
        print('input = ', self.input)
        print('output = ', self.output)