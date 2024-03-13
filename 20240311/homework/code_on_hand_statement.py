from datetime import datetime

name = "Luna"
number1 = 299792458
number2 = 149_597_870_700
number3 = 9.80665

HANNALS_FAVORITE_NUMBER = [number1, number2, number3]

my_favorite_numbers = (12, 16, 42)

staffs = {
    "hannal": "강의자",
    "younamjoo": "코치",
    "kaychang": "코치",
}

def print_puddingcamp_staffs(title, find_role: str):
    """푸딩캠프의 스태프 목록을 출력합니다.
    
    Args:
        title (str): 출력할 제목
        find_role (str): 찾을 역할

    Returns:
        count (int): 찾은 역할의 수

    Examples:
        >>> print_puddingcamp_staffs("title", "코치")
        2
    """

    count = 0
    for name, role in staffs.items():
        if role == find_role:
            count += 1
        else:
            pass
    
    return count

if __name__ == "__main__":
    print_puddingcamp_staffs(
        "푸딩캠프의 스태프 목록은 다음과 같습니다.",
        "코치"
    )


