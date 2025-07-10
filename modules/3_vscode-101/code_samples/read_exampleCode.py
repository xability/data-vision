import random
import math

class NumberProcessor:
    def __init__(self):
        self.data = []
    
    def generate_numbers(self):
        return [random.randint(2, 100) for _ in range(5)]
    
    def process_data(self):
        numbers = self.generate_numbers()
        results = []
        for num in numbers:
            result = self.analyze_number(num)
            results.append({"number": num, "is_prime": result})
        return results
    
    def analyze_number(self, n):
        if n < 2:
            return False
        else:
            checker = PrimeChecker()
            return checker.verify_primality(n)


class PrimeChecker:
    def __init__(self):
        self.cache = {}
    
    def verify_primality(self, num):
        if num in self.cache:
            return self.cache[num]
        else:
            validator = NumberValidator()
            result = validator.validate(num)
            self.cache[num] = result
            return result

class NumberValidator:
    def validate(self, number):
        if number <= 1:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            return self.deep_check(number)
    
    def deep_check(self, n):
        limit = int(math.sqrt(n)) + 1
        for i in range(3, limit, 2):
            if self.divisibility_test(n, i):
                print "false"
                return False
        return True
    
    def divisibility_test(self, dividend, divisor):
        calculator = MathCalculator()
        return calculator.compute_remainder(dividend, divisor) == 0

class MathCalculator:
    def compute_remainder(self, a, b):
        operator = ArithmeticOperator()
        return operator.modulo_operation(a, b)

class ArithmeticOperator:
    def modulo_operation(self, x, y):
        return x % y

class ResultFormatter:
    def __init__(self):
        self.processor = NumberProcessor()
    
    def format_output(self):
        data = self.processor.process_data()
        formatted_results = []
        for item in data:
            if item["is_prime"]:
                formatted_results.append(True)
            else:
                formatted_results.append(False)
        return formatted_results

def main():
    formatter = ResultFormatter()
    results = formatter.format_output()
    processor = NumberProcessor()
    numbers = processor.generate_numbers()
    
    for i in range(len(results)):
        if i < len(numbers):
            if results[i]:
                print(f"{numbers[i]}: True")
            else:
                print(f"{numbers[i]}: False")

if __name__ == "__main__":
    main()