# When doing it in-place, the basic algo maintains two watchers, i and j.
# j is the boundry between the 'frontier' and the rest of the array
# i is the partition between the elements less than, greater than the pivot
# when a term which is smaller than the pivot is encountered, swap i with j,
# then increment i
# at the end, we swap i with the pivot to put pivot into proper place.
# all about the in-place swaps


# all list comprehensions FTW
def qsort_lc(list):
  if len(list) <=1:
    return list

  pivot = list[0]
  less_than = qsort([n for n in list[1:] if n < pivot])
  greater_than = qsort([n for n in list[1:] if n > pivot])
  return (less_than + pivot + greater_than)
