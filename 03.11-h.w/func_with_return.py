# פונקציות עם ערך מוחזר

# a
def my_avg(num1: int, num2: int) -> float:
    """this function calculates the average of two numbers"""
    result: float = (num1 + num2) / 2
    return result


avg1: float = my_avg(90, 99)
print(avg1)


# b
def my_headline(title: str) -> str:
    """this function takes a string converts it to uppercase and adds an exclamation mark at the end"""
    head = title.upper() + '!'
    return head


head1: str = my_headline('python has concurred the world')
print(head1)
print(head1)


# c
def concat_list(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    """this function concatenates three lists of numbers in to one list"""
    result: list = list1 + list2 + list3
    return result


list1: list = [1, 2, 3]
list2: list = [4, 5, 6]
list3: list = [7, 8, 9]
res_con: list = list1 + list2 + list3
print(res_con)
print(len(res_con))
