from operator import itemgetter
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = list(zip(position, speed))
        sorted_pairs = sorted(pairs, key=itemgetter(0), reverse=True)
        times = [(target - sorted_pairs[0][0]) / sorted_pairs[0][1]]

        for p, s in sorted_pairs[1:]:
            if (((target - p) / s) > times[-1]):
                times.append((target - p) / s)
        return len(times)