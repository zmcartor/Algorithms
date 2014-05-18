def mergesort_inversions(list, inversions =0):
	
	def combine(list1, list2, inversions =0):
		combined = []
		while list1 and list2:
			if list1[0] <= list2[0]:
				combined.append(list1.pop(0))
			else:
				combined.append(list2.pop(0))
				inversions += len(list1)
		return (combined + list1 + list2, inversions)
	
	if len(list) <= 1:
		return (list, inversions)

	list1 = mergesort_inversions(list[0:len(list)/2])
	list2 = mergesort_inversions(list[len(list)/2:len(list)])
	return combine(list1[0], list2[0], list1[1]+list2[1])
