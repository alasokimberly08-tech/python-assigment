def count_above_50(numbers):
    count=0
    for n in numbers:
        if n > 50:
            count += 1
    return count

marks =[45, 67, 89, 23, 56, 78, 12,50,30, 90]
print(count_above_50(marks)) 