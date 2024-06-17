
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year_result = 2022
result= is_year_leap(year_result)


print("Год", year_result,":", result)