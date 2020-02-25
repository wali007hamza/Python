import sys
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 0):
            return list()
        sorted_intervals = Solution.sort_intervals(intervals)
        interval_stack = list()
        interval_stack.append(sorted_intervals[0])
        for interval in sorted_intervals[1:]:
            prev_interval = interval_stack.pop()

            # merge
            if (prev_interval[1] >= interval[0]):
                if(prev_interval[1] > interval[1]):
                    new_interval = [prev_interval[0], prev_interval[1]]
                else:
                    new_interval = [prev_interval[0], interval[1]]
                interval_stack.append(new_interval)
            # don't merge
            else:
                interval_stack.append(prev_interval)
                interval_stack.append(interval)

        return interval_stack

    @staticmethod
    def sort_intervals(intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        return sorted_intervals


if __name__ == "__main__":
    list_of_intervals = [
        list(map(int, interval.split(",")))
        for interval in input().strip().split(" ")
    ]
    intervals = Solution().merge(list_of_intervals)
    print(intervals)
