# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter={}
#
# for number in numbers:
#     if number in counter:
#         counter[number] = counter[number] + 1
#     else:
#         counter[number] = 1
#
# print(counter)

#
# character = {"name": "기사", "level": 12, "items": {"sword": "불꽃의 검", "armor": "풀플레이트"}, "skill": ["베기", "세게 베기", "아주 세게 베기"]}
#
# for key in character:
#     if type(character[key]) is dict:
#         for small_key in character[key]:
#             print(small_key, ":", character[key][small_key])
#     elif type(character[key]) is list:
#         for item in character[key]:
#             print(key, ":", item)
#     else:
#         print(key, ":", character[key])


# 2021.08.11 4-3 반복문과 while 반복문

# for 반복문 과 범위를 함께 조합해서 사용합니다.

# for i in range(5):
#     print(str(i) + "= 반복 변수")
# print()
#
# for i in range(5, 10):
#     print(str(i) + "= 반복 변수")
# print()
#
# for i in range(0, 10, 3):
#     print(str(i) + "= 반복 변수")
# print()

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

