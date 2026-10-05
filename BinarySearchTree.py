class TreeNode:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    """Inserts a new value into the BST following the structural rules."""
    # If the tree/subtree is empty, create and return a new node
    if root is None:
        return TreeNode(key)

    # Recur down the left side if the value is smaller
    if key < root.val:
        root.left = insert(root.left, key)
    # Recur down the right side if the value is larger or equal
    else:
        root.right = insert(root.right, key)
        
    return root

def inorder_traversal(root, result=None):
    """Traverses the tree (Left, Root, Right) to fetch elements in ascending order."""
    if result is None:
        result = []
        
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
        
    return result

# --- Main Interactive Program ---
def main():
    print("=== Interactive Binary Search Tree (BST) ===")
    print("Enter integers to build your tree. Type 'done' when you are finished.\n")
    
    bst_root = None
    inserted_elements = []
    
    while True:
        user_input = input("Enter a number (or 'done'): ").strip()
        
        # Check if the user wants to exit the input loop
        if user_input.lower() == 'done':
            break
            
        # Error handling to ensure only valid integers are accepted
        try:
            number = int(user_input)
            bst_root = insert(bst_root, number)
            inserted_elements.append(number)
            print(f"-> Added {number} to the BST.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer or type 'done'.")

    # Output results if elements were added
    if inserted_elements:
        print("\n--- Final Results ---")
        print(f"Your input sequence: {inserted_elements}")
        print(f"Sorted Inorder Output: {inorder_traversal(bst_root)}")
    else:
        print("\nNo numbers were added to the tree.")

if __name__ == "__main__":
    main()
