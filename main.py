"""
HW05 — City Bike Registry (Resizing Chaining Map)
"""

class HashMap:
    """Chaining hash map with auto-resize at load factor > 0.75."""

    def __init__(self, m=4):
        """Create m empty buckets and set size counter."""
        self.m = m
        self.buckets = [[] for _ in range(m)]
        self.size = 0

    def _hash(self, s):
        """Return simple integer hash for string s."""
        return sum(ord(c) for c in s)

    def _index(self, key, m=None):
        """Return bucket index for key with current or given bucket count."""
        if m is None:
            m = self.m
        return self._hash(key) % m

    def __len__(self):
        """Return number of stored pairs."""
        return self.size

    def _resize(self, new_m):
        """Resize to new_m buckets and rehash all pairs."""
        old_buckets = self.buckets
        self.m = new_m
        self.buckets = [[] for _ in range(new_m)]
        self.size = 0
        
        # Rehash all pairs from old buckets
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        """Insert or overwrite. Resize first if load will exceed 0.75."""
        # Check if we need to resize (before inserting)
        load_factor = (self.size + 1) / self.m
        if load_factor > 0.75:
            self._resize(self.m * 2)
        
        # Get bucket index
        index = self._index(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Insert new pair
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        """Return value for key or None if missing."""
        index = self._index(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None

    def delete(self, key):
        """Remove key if present. Return True if removed else False."""
        index = self._index(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False

if __name__ == "__main__":
    # Optional manual check
    pass
