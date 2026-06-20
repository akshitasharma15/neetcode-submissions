class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = r

        while l <= r:
            mid = l + ((r-l)//2)
            count = 0 
            
            for i in piles:
                count = count + (i//mid)
                if i%mid != 0:
                    count += 1
            if count <= h:
                k = min(mid, k)
                r = mid - 1
            else:
                l = mid + 1
        return k 
        