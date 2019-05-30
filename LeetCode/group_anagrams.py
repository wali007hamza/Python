import sys
from typing import List

class AnagramStrNode:
    def __init__(self, string: str):
        self.string = string
        char_list = [i for i in string]
        char_list.sort()
        self.sorted_string = "".join(char_list)

def group_anagrams(anagram_str_node_list: List):
    anagram_dict = {}
    for anagram_str_node in anagram_str_node_list:
        dict_key = anagram_str_node.sorted_string
        if(not(dict_key in anagram_dict)):
            anagram_dict[dict_key] = list()
        anagram_dict[dict_key].append(anagram_str_node)

    return anagram_dict


if __name__ == "__main__":
    string_list = [str(string.strip()) for string in input().strip().split(",")]
    anagram_str_node_list = list()
    for string in string_list:
        anagram_str_node = AnagramStrNode(string)
        anagram_str_node_list.append(anagram_str_node)

    anagram_dict = group_anagrams(anagram_str_node_list)
    for key in anagram_dict.keys():
        grouped_list = list()
        for anagram_node in anagram_dict[key]:
            grouped_list.append(anagram_node.string)

        print(grouped_list)
