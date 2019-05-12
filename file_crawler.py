import sys
import os
import queue


def is_node_file(node_path: str):
    return os.path.isfile(node_path)


def get_file_size(file_path: str):
    stat_info = os.stat(file_path)
    file_size = stat_info.st_size
    return file_size


def traverse_directories(bfs_queue: queue.Queue):
    max_file_path = ""
    max_file_size = 0
    while (not (bfs_queue.empty())):
        node_path = bfs_queue.get()
        if (is_node_file(node_path)):
            curr_file_size = get_file_size(node_path)
            if (curr_file_size > max_file_size):
                max_file_size = curr_file_size
                max_file_path = node_path
        else:
            for sub_node in os.listdir(node_path):
                bfs_queue.put(node_path + "\\" + sub_node)

    return (max_file_path, max_file_size)


if __name__ == "__main__":
    file_path = str(input().strip())
    bfs_queue = queue.Queue()
    bfs_queue.put(file_path)
    file_info = traverse_directories(bfs_queue)
    file_size = file_info[1] / 1000
    print(file_info[0], " ", '{0} {1}'.format(file_size, "KB"))