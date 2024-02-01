with open('number.txt') as numbers:
    content = numbers.readlines()

content_filter = list(filter(lambda i: i % 2 == 0,
                      map(lambda n: int(n), content)))

top_five = sorted(content_filter)[:-6:-1]

sum_top_five = sum(sorted(content_filter)[-5:])

print(top_five)
print(sum_top_five)
