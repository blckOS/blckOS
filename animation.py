def easeOut (time, initialVal, finalVal, duration=1500):
	change = finalVal - initialVal
	time/=duration
	ts=(time/duration)*time
	tc=ts*time
	return initialVal+change*(33*tc*ts + -106*ts*ts + 126*tc + -67*ts + 15*time)

p1X = 100
p2X = 200
i=0

while i <= 101:
	print (int(easeOut(i,p1X,p2X)))
	i+=1
