f = open("data/breadth_results.txt", "r")
i = 0
ie = 0.0
im = 0.0
ih = 0.0
se = 0
sm = 0
sh = 0
for line in f:
	line.rstrip()
	print(line)
	time = line.split("|")[1]
	space = line.split("|")[2]
	if i < 20:
		ie += float(time)
		se += int(space)
	elif i < 40:
		im += float(time)
		sm += int(space)
	elif i < 60:
		ih += float(time)
		sh += int(space)
	i += 1

print("easy avg time:", ie/20)
print("easy avg space:", se/20)

print("medium avg time:", im/20)
print("medium avg space:", sm/20)

print("hard avg time:", ih/20)
print("hard avg space:", sh/20)
