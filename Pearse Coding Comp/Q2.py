def twin_check(name1, age1, name2, age2):
    if age1 == age2:
        print(f"MAYBE TWINS:{name1} and {name2} are the same age")
    elif age1 > age2:
        print(f"NOT TWINS:{name1} is {age1 - age2} year(s) older than {name2}")
    elif age1 < age2:
        print(f"NOT TWINS:{name1} is {age2 - age1} years older than {name2}")

name1, age1 = input().split()
name2, age2 = input().split()

twin_check(name1, int(age1), name2, int(age2))