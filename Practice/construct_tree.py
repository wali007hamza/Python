import sys


class TreeNode:
    def __init__(self, value):
        self.left: TreeNode
        self.right: TreeNode
        self.val = value


preorder_idx = 0

def construct_tree(inorder_seq, preorder_seq, inorder_low, inorder_high):
    global preorder_idx
    if(inorder_low > inorder_high):
        return None
    current_node_val = preorder_seq[preorder_idx]
    preorder_idx += 1
    index_of_node_in_inorder_seq = find_index_for_node_value(inorder_seq, current_node_val, inorder_low, inorder_high)
    tree_root = TreeNode(current_node_val)
    tree_root.left = construct_tree(inorder_seq, preorder_seq, inorder_low, index_of_node_in_inorder_seq - 1)
    tree_root.right = construct_tree(inorder_seq, preorder_seq, index_of_node_in_inorder_seq + 1, inorder_high)
    return tree_root

def find_index_for_node_value(inorder_seq, val, inorder_low, inorder_high):
    idx = inorder_low
    while(idx <= inorder_high):
        if(inorder_seq[idx] == val):
            return idx
        idx += 1

def dfs(node: TreeNode):
    if(node == None):
        return
    dfs(node.left)
    print(node.val)
    dfs(node.right)


if __name__ == "__main__":
    inorder_seq = list(map(str, input().strip().split()))
    preorder_seq = list(map(str, input().strip().split()))
    preorder_idx = 0
    constructed_tree = construct_tree(inorder_seq, preorder_seq, 0, len(inorder_seq) - 1)
    dfs(constructed_tree)
