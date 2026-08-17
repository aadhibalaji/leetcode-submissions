class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        tTable = {}

        for c in t:
            tTable[c] = tTable.get(c, 0) + 1

        left, right = 0, 0
        res = ""
        have, need = 0, len(tTable)

        sTable = {}

        while right < len(s):
            char = s[right]

            if char in tTable:
                
                sTable[char] = sTable.get(char, 0) + 1

                if sTable[char] == tTable[char]:
                    have += 1


            while have == need:
                if not res:
                    res = s[left:right+1]
                if (right - left + 1) < len(res):
                    res = s[left:right+1]
                
                if s[left] in tTable:
                    if sTable[s[left]] == tTable[s[left]]:
                        have -= 1
                
                    if sTable[s[left]] > 1:
                        sTable[s[left]] -= 1
                    else:
                        del sTable[s[left]]
                
                left += 1

            right += 1

 
        return res
                    

            

            

            
            
                

        
