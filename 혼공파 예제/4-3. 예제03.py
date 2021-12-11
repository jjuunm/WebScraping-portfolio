limit = 10000
i = 1

# sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value라는 변수 이름을 사용

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))
