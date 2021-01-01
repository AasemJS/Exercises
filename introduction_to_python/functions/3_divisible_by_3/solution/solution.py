# Write your code here

def divisible_by_3(*args):
    div_by_3 = []
    for arg in args:
        if arg % 3 == 0:
            div_by_3.append(arg)
    return div_by_3