def mergesort(list):
	
	def combine(list1, list2):
		combined = []
		while list1 and list2:
			if list1[0] <= list2[0]:
				combined.append(list1.pop(0))
			else:
				combined.append(list2.pop(0))
		return combined + list1 + list2
	
	if len(list) <= 1:
		return list

	list1 = mergesort(list[0:len(list)/2])
	list2 = mergesort(list[len(list)/2:len(list)])
	return combine(list1, list2)
