# 반복문을 사용한 리스트 생성

# 변수 선언
array = []

# 반복문 적용
for i in range(0, 20, 2):
    array.append(i * i)

# 출력
print(array)


# 리스트 안에 for문 사용하기
array = [i * i for i in range(0, 20, 2)]
print(array)

# 조건을 활용한 리스트 내포

# 리스트 선언
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
ouput = [fruit for fruit in array if fruit != "초콜릿"]
print(ouput)

