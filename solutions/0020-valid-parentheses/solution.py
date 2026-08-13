class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = deque()
        openBracks = {"{", "(", "["}
        closedBracks = {"}", ")", "]"}
        pairs = {"()", "[]", "{}"}
        
        for bracket in s:
            
            if bracket in openBracks:
                stack.append(bracket)
                continue
            
            if stack:
                opened = stack.pop()
                
                pair = opened + bracket

                if pair not in pairs:
                    return False
            else:
                return False

        if stack:
            return False

        
        return True


