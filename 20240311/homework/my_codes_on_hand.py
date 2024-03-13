def is_even(n):
    """
    1. n이 짝수이면 True를 반환
    Args:
        n: int
    Returns:
        bool
    
    >>> is_even(2)
    True
    """
    return n % 2 == 0

def is_odd(n):
    """
    2. n이 홀수이면 True를 반환
    Args:
        n: int
    Returns:
        bool
    
    >>> is_odd(3)
    True
    """
    return n % 2 != 0

def is_three_multiple(n):
    """
    3. n이 3의 배수이면 True를 반환
    Args:
        n: int
    Returns:
        bool
    >>> is_three_multiple(3)
    True
    """
    return n % 3 == 0

def is_five_multiple(n):
    """
    4. n이 5의 배수이면 True를 반환
    Args:
        n: int
    Returns:
        bool
    >>> is_five_multiple(5)
    True
    """
    return n % 5 == 0

def get_average(numbers):
    """
    5. numbers의 평균을 반환
    Args:
        numbers: list of int
    Returns:
        float
    >>> get_average([1, 2, 3, 4, 5])
    3.0
    """
    return sum(numbers) / len(numbers)

def get_max(numbers):
    """
    6. numbers의 최대값을 반환
    Args:
        numbers: list of int
    Returns:
        int
    >>> get_max([1, 2, 3, 4, 5])
    5
    """
    return max(numbers)

def get_min(numbers):
    """
    7. numbers의 최소값을 반환
    Args:
        numbers: list of int
    Returns:
        int
    >>> get_min([1, 2, 3, 4, 5])
    1
    """
    return min(numbers)

def get_sum(numbers):
    """
    8. numbers의 합을 반환
    Args:
        numbers: list of int
    Returns:
        int
    >>> get_sum([1, 2, 3, 4, 5])
    15
    """
    return sum(numbers)

def get_even_numbers(numbers):
    """
    9. numbers 중 짝수만 리스트로 반환
    Args:
        numbers: list of int
    Returns:
        list of int
    >>> get_even_numbers([1, 2, 3, 4, 5])
    [2, 4]
    """
    return [n for n in numbers if is_even(n)]

def get_odd_numbers(numbers):
    """
    10. numbers 중 홀수만 리스트로 반환
    Args:
        numbers: list of int
    Returns:
        list of int
    >>> get_odd_numbers([1, 2, 3, 4, 5])
    [1, 3, 5]
    """
    return [n for n in numbers if is_odd(n)]

def get_three_multiple_numbers(numbers):
    """
    11. numbers 중 3의 배수만 리스트로 반환
    Args:
        numbers: list of int
    Returns:
        list of int
    >>> get_three_multiple_numbers([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [n for n in numbers if is_three_multiple(n)]

def get_five_multiple_numbers(numbers):
    """
    12. numbers 중 5의 배수만 리스트로 반환
    Args:
        numbers: list of int
    Returns:
        list of int
    >>> get_five_multiple_numbers([1, 2, 3, 4, 5, 6])
    [5]
    """
    return [n for n in numbers if is_five_multiple(n)]

def get_bmi(height, weight):
    """
    13. BMI를 계산하여 반환
    Args:
        height: float
        weight: float
    Returns:
        float
    >>> get_bmi(1.7, 60)
    20.761245674740486
    """
    return weight / height ** 2

def get_grade(score):
    """
    14. 점수에 따라 학점을 반환
    Args:
        score: int
    Returns:
        str
    >>> get_grade(90)
    'A'
    >>> get_grade(80)
    'B'
    >>> get_grade(70)
    'C'
    >>> get_grade(60)
    'D'
    >>> get_grade(50)
    'F'
    """
    score_dict = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
        }
    
    for grade, score in score_dict.items():
        if score >= score:
            return grade
    return 'F'

def get_circle_area(radius):
    """
    15. 원의 넓이를 반환
    Args:
        radius: float
    Returns:
        float
    >>> get_circle_area(3)
    28.274333882308138
    """
    return 3.14 * radius ** 2

def get_triangle_area(base, height):
    """
    16. 삼각형의 넓이를 반환
    Args:
        base: float
        height: float
    Returns:
        float
    >>> get_triangle_area(3, 4)
    6.0
    """
    return base * height / 2

def get_rectangle_area(width, height):
    """
    17. 사각형의 넓이를 반환
    Args:
        width: float
        height: float
    Returns:
        float
    >>> get_rectangle_area(3, 4)
    12
    """
    return width * height

def get_lcm(a, b):
    """
    18. a, b의 최소공배수를 반환
    Args:
        a: int
        b: int
    Returns:
        int
    >>> get_lcm(3, 5)
    15
    """
    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i
    
def get_gcd(a, b):
    """
    19. a, b의 최대공약수를 반환
    Args:
        a: int
        b: int
    Returns:
        int
    >>> get_gcd(3, 5)
    1
    """
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def is_luna_here(s):
    """
    20. s에 '루나'가 포함되어 있으면 True를 반환
    Args:
        s: str
    Returns:
        bool
    >>> is_luna_here('루나')
    True
    """
    return '루나' in s
