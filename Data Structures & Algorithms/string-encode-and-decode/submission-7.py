class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "#" + word)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            next_word = s.find("#", i) + 1
            if next_word == 0:
                break
            length = int(s[i:next_word-1])
            decoded.append(s[next_word:next_word+length])
            i = next_word+length
        return decoded