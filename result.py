names = ["陳巧巧", "吳大大", "李乖乖"]
courses = ["國文", "英文", "數學"]
chinese = [80, 75, 86]
english = [90, 88, 94]
math = [70, 67, 55]
score = []
averages = []

print("姓名\t國文\t英文\t數學\t總分\t平均")
for _name, _courses, _chinese, _english, _math in zip(names, courses, chinese, english, math):
    total_score = _chinese + _english + _math
    score.append(total_score)

    print(score)
    avg_score = round(total_score / len(names), 2)
    averages.append(avg_score)
    print(f"{_name}\t{_chinese}\t{_english}\t{_math}\t{total_score}\t{avg_score}")

print(f"國文最高分是：{names[chinese.index(max(chinese))]}")
print(f"英文最高分是：{names[english.index(max(english))]}")
print(f"數學最高分是：{names[math.index(max(math))]}")
print(f"第1名是：{names[averages.index(max(averages))]}")
print(f"第後1名是：{names[averages.index(min(averages))]}")
