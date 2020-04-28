class new_node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, key):
    # Traverse untill root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if key > root.data:
            root = root.right

            # pass left subtree as new tree
        elif key < root.data:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False


def insert(Node, data):
    # If the tree is empty, return
    # a new Node
    if Node == None:
        return new_node(data)

        # Otherwise, recur down the tree
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)

        # return the (unchanged) Node pointer
    return Node

if __name__ == '__main__':

    # Let us create following BST
    # 50
    # 30     70
    # / \ / \
    # 20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    if search(root, 10):
        print("Yes")
    else:
        print("No")