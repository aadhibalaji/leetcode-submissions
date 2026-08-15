class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        diff = [0] * 1001

        for numPassengers, start, end in trips:
            diff[start] += numPassengers
            diff[end] -= numPassengers

        cap = 0
        for change in diff:
            cap += change
            if cap > capacity:
                return False

        return True
