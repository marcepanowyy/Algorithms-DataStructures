from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None

def find_min(root):
  if not root.left: return root
  return find_min(root.left)

def find_max(root):
  if not root.right: return root
  return find_max(root.right)

def find_predecessor_node(root):  # poprzednik (najwieksza liczba mniejsza niz zadana)
  if root.left: return find_max(root.left)
  while root.parent:
    if root.parent.right == root:
      return root.parent
    root = root.parent
  return None

def find_successor_node(root):  # nastepnik (najmniejsza liczba wieksza niz zadana)
  if root.right: return find_min(root.right)
  while root.parent:
    if root.parent.left == root:
      return root.parent
    root = root.parent
  return None


def sol(root, T):

    return 0
    
runtests(sol, all_tests = True)