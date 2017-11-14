def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 

	return result

def mergesort(list):
	if len(list) < 2:
		return list
	middle = len(list)//2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])
	return merge(left, right)
        
class Solution(object):
    def threeSum(self, nums):
        big_l=[]
        l=mergesort(nums)
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                for k in range(j+1, len(l)):
                    if(l[i]+l[j]+l[k] == 0):
                        lis = []
                        lis.append(l[i])
                        lis.append(l[j])
                        lis.append(l[k])
                        if(lis in big_l):
                            continue
                        else:
                            big_l.append(lis)
        return big_l
        