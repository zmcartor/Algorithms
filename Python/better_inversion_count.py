# based on killer algo found here:
# http://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort
import sys, bisect

input_list = map(int,open(sys.argv[1]))
sorted_list = sorted(input_list)
inversions = 0

# we compare the unsorted list to the sorted list
# to compute inversion count, neat!
for d in input_list:
	#locate insertion point in sorted_list for d
    p = bisect.bisect_left(sorted_list,d)
    inversions += p
    input_list.pop(p)
print inversions
