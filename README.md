Python File Crawler (Breadth-First)

A simple breadth-first file-system crawler implemented in Python. It uses a queue to traverse directories level by level and prints each file or subdirectory as it encounters them.

How It Works

Start from a given directory.

Use collections.deque to maintain a BFS queue.

For each directory:

List contents in sorted order.

Print file paths.

Enqueue subdirectories for later processing.
