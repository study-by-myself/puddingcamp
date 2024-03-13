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

result = super_calculator(149_597_870_700, 299_792_458)
print(result)
