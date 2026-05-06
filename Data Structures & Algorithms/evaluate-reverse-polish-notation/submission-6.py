class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                right = stack.pop()
                left = stack.pop()
                match t:
                    case "+":
                        res = left + right
                    case "-":
                        res = left - right
                    case "*":
                        res = left * right
                    case "/":
                        res = int(left/right)
                stack.append(res)
                
        return stack.pop()