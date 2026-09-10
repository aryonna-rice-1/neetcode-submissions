from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.main_map: defaultdict[str, list[tuple[str, int]]] = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.main_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.main_map[key]
        if not vals or timestamp < vals[0][1]:
            return ""
        
        l, mid, r = 0, 0, len(vals) - 1
        while (l != r):
            mid = l + ((r - l) // 2)
            mid_pair = vals[mid]

            if (timestamp == mid_pair[1]):
                return mid_pair[0]

            if (timestamp < mid_pair[1]):
                r = mid - 1
            else:
                if ((vals[mid + 1])[1] <= timestamp):
                    l = mid + 1
                else:
                    return mid_pair[0]
        return vals[l][0]