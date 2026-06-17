def generator_numbers(text):
    for item in text.split():
        try:
            number = float(item)
            yield number
        except ValueError:
            pass

def sum_profit(text, function):
    total = 0
    for number in function(text):
        total += number
    return total

text = ("Загальний дохід працівника складається з декількох" 
"частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"загальний дохід: {total_income}")
