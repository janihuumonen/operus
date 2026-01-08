########################################################
# Task A10_TLib
# Developer Jani Huumonen
# Date 2025-12-12
########################################################



def readValues(fn: str, lst: list[int]) -> None:
	try:
		with open(fn, 'r', encoding='UTF-8') as f:
			lst.extend(map(
				int, filter(
					lambda s: s, map(
						lambda l: l.strip(), f.readlines()
			))))
	except FileNotFoundError:
		print(f'''Couldn't read file "{fn}".''')
	return None



# Measure execution time

import time

def measureExecTime(f,p):
	t0 = time.perf_counter_ns()
	f(p)
	return time.perf_counter_ns() - t0



# Bubblesort

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
	comp = (lambda a,b: a > b) if PAsc else (lambda a,b: a < b)
	r = max(0, len(PValues)-1)
	while r:
		for i in range(r):
			if comp(PValues[i], PValues[i+1]):
				PValues[i], PValues[i+1] = PValues[i+1], PValues[i]
		r -= 1
	return None



# Mergesort

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
	comp = (lambda a,b: a <= b) if PAsc else (lambda a,b: a >= b)
	PMerge.clear()
	while len(PLeft) and len(PRight):
		if comp(PLeft[0], PRight[0]):
			PMerge.append(PLeft[0])
			PLeft.pop(0)
		else:
			PMerge.append(PRight[0])
			PRight.pop(0)
	PMerge.extend(PLeft + PRight)
	return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
	# Sort PValues.
	# PAsc: in ascending order by default. False will sort in descending order.
	if len(PValues) <= 1: return None
	mid = len(PValues) // 2
	left = PValues[:mid]
	mergeSort(left, PAsc)
	right = PValues[mid:]
	mergeSort(right, PAsc)
	res = []
	merge(left,right,res,PAsc)
	PValues.clear()
	PValues.extend(res)
	return None



# Quicksort

def partition(a,lo,hi):
	pv = a[hi]
	i = j = lo
	while j<hi:
		if a[j] <= pv:
			a[i],a[j] = a[j],a[i]
			i += 1
		j += 1
	a[i],a[hi] = a[hi],a[i]
	return i

def qsort(a,lo,hi):
	if lo>=hi or lo<0: return
	p = partition(a,lo,hi)
	qsort(a,lo,p-1)
	qsort(a,p+1,hi)

def quickSort(arr):
	qsort(arr,0,len(arr)-1)

