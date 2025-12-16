def collectInts():
        l = []
        while True:
                s = int(input("Insert positive integer(negative stops): "))
                if s < 0: break
                l.append(s)
        return l

print('Program starting.')
print('Collect positive integers.')
ints = collectInts()
print('Stopped collecting positive integers.')
print(f'Displaying {len(ints)} integers:')
for i in range(0,len(ints)):
	print(f'- Index {i} => Ordinal {i+1} => Integer {ints[i]}')
print('Program ending.')
