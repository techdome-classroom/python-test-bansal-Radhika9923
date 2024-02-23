class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
      brackets = {')': '(' ,'}': '{',']':  '['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys();
                if not stack  or brackets[char] != stack.pop():
                    return False
            else:
                return False
    return not stack
s=Solution()
print(s.is_valid("()"))
print(s.is_valid("()[]{}"))
print(s._valid("(]"))

    

                

    



  

