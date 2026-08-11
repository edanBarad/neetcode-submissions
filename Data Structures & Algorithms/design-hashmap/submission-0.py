class MyHashMap:

    def __init__(self):
        # 0 means empty slot, -1 will mean a deleted slot (tombstone)
        self.buckets = [0] * 10000

    def put(self, key: int, value: int) -> None:
        start_cell = key % len(self.buckets)
        cell = start_cell
        
        # Find an empty slot, a tombstone, or the matching key
        while self.buckets[cell] != 0 and self.buckets[cell] != -1:
            if self.buckets[cell][0] == key:
                break
            cell = (cell + 1) % 10000  # Wrap around cleanly
            
        self.buckets[cell] = [key, value]

    def get(self, key: int) -> int:
        start_cell = key % len(self.buckets)
        cell = start_cell
        
        while self.buckets[cell] != 0:
            # Skip tombstone markers (-1) safely
            if self.buckets[cell] != -1 and self.buckets[cell][0] == key:
                return self.buckets[cell][1]
                
            cell = (cell + 1) % 10000  # Wrap around cleanly
            if cell == start_cell:     # Checked the whole array
                break
                
        return -1

    def remove(self, key: int) -> None:
        start_cell = key % len(self.buckets)
        cell = start_cell
        
        while self.buckets[cell] != 0:
            if self.buckets[cell] != -1 and self.buckets[cell][0] == key:
                # Mark as tombstone so linear probing chains don't break
                self.buckets[cell] = -1
                return
                
            cell = (cell + 1) % 10000
            if cell == start_cell:
                break

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)