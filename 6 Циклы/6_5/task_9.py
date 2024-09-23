line = '+----'*10+'+'
for i in range(10):
    line_num = ''
    numbers = range(i*10+1,i*10+11) if i%2 == 0 else range(i*10+10,i*10,-1)
    for num in numbers:
        if len(str(num)) == 1:
            line_num += f'|  {num} '
        elif len(str(num)) == 2:
            line_num += f'| {num} '
        elif len(str(num)) == 3:
            line_num += f'|{num} '
    line_num += '|'
    print(line)
    print(line_num)
print(line)