class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        
        for i, h in enumerate(heights):
            if st and h < st[-1][0]:
                last_index = st[-1][1]
                while st and h < st[-1][0]:
                    max_area = max(max_area, st[-1][0] * (i - st[-1][1]))
                    last_index = st[-1][1]
                    st.pop()
                st.append((h, last_index))
            
            elif not st or h >= st[-1][0]:
                st.append((h, i))

        while st:
            pop_h, pop_i = st.pop()
            max_area = max(max_area, pop_h * (len(heights) - pop_i))

        return max_area
