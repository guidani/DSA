class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def method1(root):

    if root:

        method1(root.left)

        print(root.val),

        method1(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if __name__ == "__main__":
    """
    from timeit import timeit

    print(timeit(lambda: method1(root), number=10000))  # 0.3417354199991678
    """
