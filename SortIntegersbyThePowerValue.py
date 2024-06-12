class Solution(object):
    def getKth(self, lo, hi, k):
        def calc(x):
            counter = 0
            while x != 1:
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3 * x + 1
                counter += 1
            return counter
        arr = [x for x in range(lo,hi+1)]
        arr2 = map(lambda x:calc(x), arr)
        arr = zip(arr, arr2)
        arr = sorted(arr, key=lambda x:x[1])
        arr,arr2 = map(list, zip(*arr))

        return arr[k-1]
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        