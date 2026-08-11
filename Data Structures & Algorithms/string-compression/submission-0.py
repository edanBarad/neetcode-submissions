class Solution:
    def compress(self, chars: List[str]) -> int:
        i, k = 0, 0
        while i < len(chars):
            curr = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1
            
            chars[k] = curr
            k += 1
            
            if count > 1:
                for digit in str(count):
                    chars[k] = digit
                    k += 1
                    
        return k