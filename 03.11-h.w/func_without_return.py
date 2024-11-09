import statistics


# פונקציות ללא ערך מוחזר

# a
def my_ascending(a: int, b: int) -> int:
    if a < b:
        print(a, b)
    else:
        print(b, a)


my_ascending(7, -12)


# b
def my_details(st: str) -> str:
    first_char: str = st[0]
    middle_char: str = st[len(st) // 2]
    last_char: str = st[-1]
    print('first char:', first_char)
    print('middle char:', middle_char)
    print('last char:', last_char)


my_details('All is the best')


# c
def say_bool(bool1: bool) -> bool:
    if bool1:
        print('yes')
    else:
        print('no')


say_bool(True)
say_bool(False)


# d
def my_zugi(number: list = list[int]) -> list:
    for num in number:
        # 'even' if num % 2 == 0 else 'odd'
        if num % 2 == 0:
            print('even', end=' ')
        else:
            print('odd', end=' ')


my_zugi([5, 3, 2, 10, 15, 14, 14])


# e
def my_statistics(grades) -> float:
    highest: float = max(grades)
    lowest: float = min(grades)
    count: int = len(grades)
    avg: float = statistics.mean(grades)
    print('The highest grade is:', highest)
    print('The lowest grade is:', lowest)
    print('The amount of numbers is:', count)
    print(f'The avg grades is: {avg:.2f}')


grades = []
SENTINEL = -99
while True:
    try:
        grade = int(input('Enter a number:'))
        if grade == SENTINEL:
            break
        elif grade < 0 or grade > 100:
            print('invalid grade')
            continue
        grades.append(grade)
    except ValueError:
        print('invalid input')
my_statistics(grades)
