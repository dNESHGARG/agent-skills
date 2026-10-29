# Intentional bug: cache key ignores the namespace.
class ScopedCache:
    def __init__(self):
        self.entries = {}

    def get(self, namespace, item_id, loader):
        if item_id not in self.entries:
            self.entries[item_id] = loader(namespace, item_id)
        return self.entries[item_id]
