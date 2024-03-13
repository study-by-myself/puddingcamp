
# 실습 20240307-1-2-1
def say(message):
    print(message)

say("hello world")

# 실습 20240307-1-2-2
def super_calculator(a: int, b: int) -> int | float:
	"""짱 멋진 계산기
	함수 이름은 snake case로 써야 한다.

	Args:
		a (int): 첫 번째 숫자
		b (int): 두 번째 숫자
	
	Returns:
		int | float : 계산 결과
		
	>>> super_calculator(10, 2)
	5.0
	"""
	result = a / b
	return result

result = super_calculator(1, 2)
print(result)

result = super_calculator(4, 2)
print(result)

result = super_calculator(32, 8)
print(result)

result = super_calculator(149_597_870_700, 299_792_458)
print(result)

## 실습 20240307-1-2-3
# >>> puddingcamp
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'puddingcamp' is not defined


# 실습-20240307-1-2-4
def add(a, b):
    """더하기 함수
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
    Returns:
        int : 계산 결과
    
    >>> add(10, 2)
    12
    """
    return a + b

def sub(a, b):
    """빼기 함수
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
    Returns:
        int : 계산 결과
    
    >>> sub(10, 2)
    8
    """
    return a - b

def mul(a, b):
    """곱하기 함수
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
    Returns:
        int : 계산 결과
    
    >>> mul(10, 2)
    20
    """
    return a * b

def div(a, b):
    """나누기 함수
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
    Returns:
        int | float : 계산 결과
    
    >>> div(10, 2)
    5.0
    """
    return a / b


## 실습-20240307-1-2-5

# >>> super_calculator.__doc__
# '짱 멋진 계산기\n\t함수 이름은 snake case로 써야 한다.\n\n\tArgs:\n\t\ta (int): 첫 번째 숫자\n\t\tb (int): 두 번째 숫자\n\t\n\tReturns:\n\t\tint | float : 계산 결과\n\t\t\n\t>>> super_calculator(10, 2)\n\t5.0\n\t'
# >>> id(super_calculator.__doc__)
# 4302262064

# >>> numbers = [299_792_458, 149_597_870_700, 1, 256, 257]
# >>> for number in numbers:
# ...     number1 = number2 = number
# ...     print(number1 == number2, number1, number2)
# ...     print(number1 is number2, id(number1), id(number2))
# ... 
# True 299792458 299792458
# True 4302629168 4302629168
# True 149597870700 149597870700
# True 4302629360 4302629360
# True 1 1
# True 4314476240 4314476240
# True 256 256
# True 4314484400 4314484400
# True 257 257
# True 4302628720 4302628720

# 실습 20240307-1-2-6
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

# 실습 20240307-1-2-7
    
class Calculator:
    a = 3
    b = 10

    @classmethod
    def add(cls):
        return cls.a + cls.b

    @classmethod
    def subtract(cls):
        return cls.a - cls.b

    @classmethod
    def multiply(cls):
        return cls.a * cls.b

    @classmethod
    def divide(cls):
        return cls.a / cls.b

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"
