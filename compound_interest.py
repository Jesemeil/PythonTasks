principal = 1000
rate = 0.05
for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(F'{year:>2}{amount: > 10.2f}')


