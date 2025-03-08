def padovan_series(n):
    series = [1, 1, 1]
    for i in range(3, n):
        next_term = series[i-2] + series[i-3]
        series.append(next_term)
    return series
n = int(input("Enter the number of terms in the Padovan series: "))
padovan = padovan_series(n)
print("Padovan series:", padovan)
