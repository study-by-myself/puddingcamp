from code_on_hand import *

def calc_bmi(weight, height):
    """BMI 계산기
    Args:
        weight (float): 체중 (kg)
        height (float): 신장 (cm)
    Returns:
        BMI (float) : 계산 결과
    """
    return div(weight, mul(height, height))
    # return weight / (height ** 2)

print(calc_bmi(64000, 160))
assert calc_bmi(64000, 160) == 25

def calc_wacc(E, V, Re, D, Rd, Tc):
    """가중 평균 자본 비용(WACC) 계산기
    Args:
        E (float): 기업의 시장가치에서의 자기자본 가치
        V (float): 기업의 전체 시장가치(자기자본 + 부채)
        Re (float): 자기자본의 비용(보통주 자본비용)
        D (float): 기업의 시장가치에서의 부채 가치
        Rd (float): 부채의 비용(이자율)
        Tc (float): 기업의 법인세율
    """
    # return (E / V) * Re + (D / V) * Rd * (1 - Tc)
    return add(mul(div(E / V), Re), mul(mul(div(D / V), Rd), sub(1, Tc)))

# print(calc_wacc(E=600_000_000, V=400_000_000, Re=8, D=?, Rd=5, Tc=30))
