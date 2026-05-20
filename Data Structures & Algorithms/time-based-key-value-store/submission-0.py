class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = {}
        if timestamp not in self.time_map[key]:
            self.time_map[key][timestamp] = []
        self.time_map[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        seen = 0
        for t in self.time_map[key]:
            if t <= timestamp:
                seen = max(seen, t)
        
        return "" if seen == 0 else self.time_map[key][seen][-1]