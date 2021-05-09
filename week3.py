# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 1. 날짜, 시간, 날씨가 포함된 문자열을 만들고
# 2. 슬라이싱을 통해 날짜, 시간, 날씨를 나누어 출력해봅시다
# a = ["20210504", "08:00", "raniny"]
# print("날짜:", a[0])
# print("시간:", a[1])
# print("날씨:", a[2])

# 사용자에게 초를 입력받아 시간, 분, 초를 계산하는 프로그램
s = int(input("시간을 초단위로 입력하세요: "))
hours = s / 3600
m = s/60
ss = s - m * 60
print(s ,"초는:")
print(hours, '시간', m, '분', ss, '초 입니다.')
