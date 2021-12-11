# 키워드 매개 변수

def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활요합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수 호출
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
