# lst = ["가", "나", "다"]
#
# for lst_idx, lst_val in enumerate(lst):
#     print(lst_idx, lst_val)

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("balls :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue
    break