class StoragePolicy:
    def __init__(self, storage):
        self.storage = storage

    def should_move(self, key):
        pass

    def decide_target_cloud(self, key):
        pass

    def apply(self, key):
        pass