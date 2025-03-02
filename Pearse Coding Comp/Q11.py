n = input().strip()

def count_sevens(x):
    count = 0
    factor = 1

    while factor <= x:
        lower_numbers = x - (x // factor) * factor
        current_digit = (x // factor) % 10
        higher_numbers = x // (factor * 10)

        if current_digit < 7:
            count += higher_numbers * factor
        elif current_digit == 7:
            count += higher_numbers * factor + lower_numbers + 1
        else:
            count += (higher_numbers + 1) * factor

        factor *= 10

    return count

n_int = int(n)
print(count_sevens(n_int))