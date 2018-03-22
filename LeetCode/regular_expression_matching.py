import sys
from abc import ABC, abstractmethod, abstractproperty

class StateMachine(ABC):
    def __init__(self):
        self._next_state_machine = None

    @property
    def next_state_machine(self):
        return self._next_state_machine

    @next_state_machine.setter
    def next_state_machine(self, new_value):
        self._next_state_machine = new_value

    @abstractmethod
    def process(self, string, start_pos):
        pass

class CharAndStarStateMachine(StateMachine):
    def __init__(self, character: str):
        self.character = character
        super()

    @property
    def next_state_machine(self):
        return super().next_state_machine

    @next_state_machine.setter
    def next_state_machine(self, new_value):
        StateMachine._next_state_machine = new_value

    def process(self, string, start_pos):
        i = start_pos
        while(string[i] == self.character):
            i += 1
        start_pos = i

        result = True
        if(super().next_state_machine != None):
            result = super().next_state_machine.process(string, start_pos)

        print(self.character)
        return result


class DotStateMachine(StateMachine):
    def __init__(self):
        self._next_state_machine = None


class Solution:
    def isMatch(self, string, pattern):
        charAndStarStateMachine = CharAndStarStateMachine('b')
        charAndStarStateMachine2 = CharAndStarStateMachine('c')
        charAndStarStateMachine.next_state_machine = charAndStarStateMachine2
        result = charAndStarStateMachine.process(string, 0)
        return result


if __name__ == "__main__":
    string, pattern = tuple(input().strip().split())
    ret_value = Solution().isMatch(string, pattern)
    print(ret_value)
