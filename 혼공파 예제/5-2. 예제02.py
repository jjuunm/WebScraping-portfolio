# 리스트 평탄화

# 기본적인 함수의 활용
"""
def 함수(매개변수):
    변수 = 초깃값
    # 여러 가지 처리
    # 여러 가지 처리
    # 여러 가지 처리
    return 변수
"""

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))
